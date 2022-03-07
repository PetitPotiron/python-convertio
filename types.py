from typing import Any, List, Dict, Optional, TypedDict


class ConversionPostResult(TypedDict):
    code: int
    status: str
    data: 'ConversionPostResultDictData'


class ConversionPostResultDictData(TypedDict):
    id: str
    minutes: str


class ConversionPostDict(TypedDict, total=False):
    apikey: str
    input: str
    file: str
    filename: Optional[str]
    outputformat: str
    options: Optional['ConversionPostDictOptions']


class ConversionPostDictOptions(TypedDict):
    ocr_enabled: bool
    ocr_settings: 'ConversionPostDictOptionsOcrSettings'


class ConversionPostDictOptionsOcrSettings(TypedDict, total=False):
    langs: List[str]
    page_nums: Optional[str]


class ConversionStatusResult(TypedDict):
    code: int
    status: str
    data: 'ConversionStatusResultData'


class ConversionStatusResultData(TypedDict):
    id: str
    step: str
    step_percent: int
    minutes: int
    output: 'ConversionStatusResultDataOutPut'


class ConversionStatusResultDataOutPut(TypedDict):
    url: str
    size: int
    files: Dict[Any, Any]
