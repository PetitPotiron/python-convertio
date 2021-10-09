class Conversion:
    def __init__(self, data) -> None:
        self.code = data['code']
        self.status = data['status']
        self.id = data['data']['id']
        self.step = data['data']['step']
        self.step_percent = data['data']['step_percent']
        self.minutes = data['data']['minutes']
        try:
            self.output_url = data['data']['output']['url']
            self.output_size = data['data']['output']['size']
        except:
            self.output_url = "Url not available yet"
            self.output_size = None
    
    def __repr__(self):
        return f'<Response [{self.code}]> {self.status} | {self.step} - {self.step_percent} % \n {self.output_url}'

    
    
