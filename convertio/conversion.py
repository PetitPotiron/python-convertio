from typing import Optional

from convertio.types import ConversionStatusResult


class Conversion:
    def __init__(self, data: ConversionStatusResult) -> None:
        self.code = data['code']
        self.status = data['status']
        self.id = data['data']['id']
        self.step = data['data']['step']
        self.step_percent = data['data']['step_percent']
        self.minutes = data['data']['minutes']
        try:
            self.output_url: str = data['data']['output']['url']
            self.output_size: Optional[int] = data['data']['output']['size']
        except Exception:
            self.output_url: str = "Url not available yet"
            self.output_size = None

    def __repr__(self):
        return f'<Response [{self.code}]> {self.status} | {self.step} - {self.step_percent} % \n {self.output_url}'
