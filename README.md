# convertio
[![Convertio version on pypi](https://img.shields.io/pypi/v/convertio.svg)](https://pypi.org/project/convertio)
[![Discord support server](https://discord.com/api/guilds/800032961525317693/embed.png)](https://discord.gg/t2dxrXMKya)

An API wrapper for convertio.co. Before starting, make sure [you've got an API key](https://developers.convertio.co/user/registration/api?utm_source=api_top_btn). The full API reference can be found on [convertio.co/api/docs](https://convertio.co/api/docs), but I'll make a documentation for this package soon.

## Get started
- Sign-up to [developers.convertio.co](https://developers.convertio.co/user/registration/api?utm_source=api_top_btn).
- Get your free API key from [the homepage](https://developers.convertio.co)
- Install this module : run `python -m pip install convertio -U` for Windows or `python3 -m pip install convertio -U` for Linux and Macos. You can also download it from github `pip install git+https://github.com/PetitPotiron/python-convertio.git`

## Quick start
```python
import convertio
import time

client = convertio.Client(token="INSERT_YOUR_TOKEN_HERE")
conversion_id = client.convert_by_filename('source.txt', 'pdf')
while client.check_conversion(conversion_id).step != 'finish':
    time.sleep(1)
client.download(conversion_id, 'result.pdf')
client.delete(conversion_id)
```


## Notes

Version `1.1.0`

This module is neither created nor managed by convertio.co. It represents services faithful to the API and documentation from their website. This API is not unofficial, and it can be payable if you exceed a certain usage. Notice that you must respect convertio.co's [terms of use](https://convertio.co/terms).

### Links
- [Get an API key](https://developers.convertio.co/user/registration/api?utm_source=api_top_btn)
- [API pricing](https://developers.convertio.co/api/pricing)
- [API reference](https://developers.convertio.co/api/docs)
- [OCR (options) pricing](https://developers.convertio.co/ocr/pricing)
- [Conversion types](https://convertio.co/formats)
- [GitHub](https:/github.com/PetitPotiron/python-convertio)
- [PHP module by convertio.co](https://github.com/convertio/convertio-php)
- [CLI for convertio.co, by themselves](https://developers.convertio.co/cli)

### Changelog
- [Add some type to the project](https://github.com/PetitPotiron/python-convertio/pull/3)
