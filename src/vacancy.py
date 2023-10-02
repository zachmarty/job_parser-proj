class Vacancy():
    def __init__(self, title, url, pay, requirement) -> None:
        self.title = title
        self.url = url
        self.pay = pay
        self.requirement = requirement

    def json(self):
        return {
            'title':self.title,
            'url':self.url,
            'pay':self.pay,
            'requirement':self.requirement,
        }
    @classmethod
    def from_json(cls, params):
        return cls(params['title'], params['url'], params['pay'], params['requirement'])