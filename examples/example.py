import os
import convertio
import time

client = convertio.Client(token="INSERT_YOUR_TOKEN_HERE")
conversion_id = client.convert_by_filename('source.txt', 'pdf')
while client.check_conversion(conversion_id).step != 'finish':
    time.sleep(1)
client.download(conversion_id, 'result.pdf')
client.delete(conversion_id)


def convert_with_convertio(input_file: str, output_file: str, api_key: str):
    client = convertio.Client(token=api_key)
    conversion_id = client.convert_by_filename(fp=input_file,
                                               output_format=get_file_extension(output_file))
    while client.check_conversion(conversion_id).step != 'finish':
        time.sleep(1)
    client.download(conversion_id, os.path.abspath(output_file))


convert_with_convertio('source.txt', 'result.pdf', "INSERT_YOUR_TOKEN_HERE")


def get_file_extension(file: str):
    root, extension = os.path.splitext(file)
    return extension[1:]
