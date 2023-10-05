import json
FILE = 'vacancies.json'

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
    
    @classmethod
    def all_from_json(cls):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        output = []
        for vacancy in vacancies:
            tmp = Vacancy.from_json(vacancy)
            output.append(tmp)
        return output
    
    def show_info(self):
        print(self.title)
        print(self.url)
        print(f'Заработная плата {self.pay}')
        print(self.requirement)