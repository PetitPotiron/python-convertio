from os import PathLike
import base64
import urllib.request as request
import json
import time
import os.path as path
from .conversion import *
from .options import *
import urllib.error as weberror


class Client:

    def __init__(self, token) -> None:
        self.token = token

    def convert_by_filename(self, fp: PathLike, output_format: str, output_filename: str = None, options: Options = None):
        """Converts the file found in the path provided.

        Args:
            filename (str): The file's path
            output_format (str): The file format you want the file to be converted to
            options (Options, optional): OCR  Defaults to None.
        """
        if output_filename is None:
            filename = "".join(path.splitext(path.basename(fp)))
        else:
            filename = output_filename
        if options is not None:
            _options = {
                'ocr_enabled': True,
                'ocr_settings': {
                    'langs': options.langs,
                    'page_nums': options.page_nums
                }
            }
        else:
            _options = None
        with open(fp, 'r') as file:
            data = {
                'apikey': self.token,
                'input': 'base64',
                'file': base64.b64encode(file.read().encode('utf8')).decode('utf8'),
                'filename':  filename,
                'outputformat': output_format,
                'options': _options
            }
        if data['options'] is None:
            del data['options']
        else:
            if data['options']['ocr_settings']['page_nums'] is None:
                del data['options']['ocr_settings']['page_nums']

            if data['options']['ocr_enabled'] is False:
                del data['options']
        r = request.Request(
            url='https://api.convertio.co/convert',
            data=json.dumps(data).encode("utf8"),
            method='POST',
        )
        r.add_header('Content-Type', 'application/json')
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
            return data['data']['id']
        except weberror.HTTPError as e:
            if e.code == 401:
                raise ValueError(
                    'This API Key is invalid or there is no convertion minutes left')
            elif e.code == 400:
                raise ValueError("Field `options.langs` required to be non-empty array")
            elif e.code == 422:
                raise ValueError(
                    'CONVERTER: The Type of Output File is not supported yet')

    def convert_by_url(self, url: str, output_format: str, options: Options = None):
        """Converts the file found in the given url.

        Args:
            url (str): The url where the file is
            output_format (str): The file format you want the file to be converted to
            options (Options, optional): OCR Options Defaults to None.
        """
        data = {
            'apikey': self.token,
            'input': 'url',
            'file': url,
            'outputformat': output_format,
            'options': {
                'ocr_enabled': True if options else False,
                'ocr_settings': {
                     'langs': options.langs,
                     'page_nums': options.page_nums
                } if options else None,
            } if options else None
        }
        if data['options'] is None:
            del data['options']
        else:
            if data['options']['ocr_settings']['page_nums'] is None:
                del data['options']['ocr_settings']['page_nums']

            if data['options']['ocr_enabled'] is False:
                del data['options']
        r = request.Request(
            url='https://api.convertio.co/convert',
            data=json.dumps(data).encode("utf8"),
            method='POST',
        )
        r.add_header('Content-Type', 'application/json')
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
            return data['data']['id']
        except weberror.HTTPError as e:
            if e.code == 401:
                raise ValueError(
                    'This API Key is invalid or there is no convertion minutes left')
            elif e.code == 400:
                raise ValueError(
                    "Field `options.langs` required to be non-empty array")
            elif e.code == 422:
                raise ValueError(
                    'CONVERTER: The Type of Output File is not supported yet')

    def check_conversion(self, id: str):
        """Checks the step of a conversion

        Args:
            id (str) : The id of the conversion

        Returns:
            Conversion: The status of the conversion
        """
        r = request.Request(f'https://api.convertio.co/convert/{id}/status')
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
            return Conversion(data)
        except weberror.HTTPError as e:
            if e.code == 404:
                raise ValueError("The system is unable to find the requested action (the conversion isn't found)")
            elif e.code == 422:
                raise ValueError('Input file appears to be corrupted')

    def download(self, id: str, fp: PathLike):
        """Writes the file content to a path."""
        r = request.Request(f'https://api.convertio.co/convert/{id}/status')
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
            if data['status'] == 'error':
                raise ValueError(data['error'])
            data = Conversion(data)
            r = request.Request(data.output_url)
            r = request.urlopen(r)

            with open(fp, "wb") as file:
                file.write(r.read())
        except weberror.HTTPError as e:
            if e.code == 404:
                raise ValueError("The system is unable to find the requested action (the conversion isn't found)")
            elif e.code == 422:
                raise ValueError('Input file appears to be corrupted')
        except ValueError as e:
            raise ValueError("The url isn't available yet")

    def delete(self, id: str):
        """Deletes or cancels a conversion"""
        r = request.Request(
            url='https://api.convertio.co/convert/' + id,
            method='DELETE',
        )
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
        except weberror.HTTPError as e:
            if e.code == 404:
                raise ValueError("File not found")

    def cancel(self, id: str):
        """Cancels a conversion"""
        self.delete(id)

    def conversions_list(self, status='all', count=1):
        """Gets the list of the client's conversions (count=-1 for all the conversions)."""
        data = {
            'apikey': self.token,
            'status': status,
            'count': count
        }

        r = request.Request(url=f'https://api.convertio.co/convert/list',
                            method='POST',
                            data=json.dumps(data).encode('utf8'))
        try:
            r = request.urlopen(r)
            data = json.loads(r.read().decode('utf8'))
            return data['data']
        except weberror.HTTPError as e:
            if e.code == 400:
                raise ValueError('Incorrect status value')
            elif e.code == 401:
                raise ValueError('This API Key is invalid')
