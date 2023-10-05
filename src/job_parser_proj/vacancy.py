import json
FILE = 'vacancies.json'

"""
Класс для хранения информации по вакансиям
"""
class Vacancy():
    """
    Конструктор, принимает название, ссылку, заработную плату, требования
    """
    def __init__(self, title, url, pay, requirement) -> None:
        self.title = title
        self.url = url
        self.pay = pay
        self.requirement = requirement

    """
    Метод, который возвращает информацию о вакансии в виде словаря
    """
    def json(self):
        return {
            'title':self.title,
            'url':self.url,
            'pay':self.pay,
            'requirement':self.requirement,
        }
    
    """
    КлассМетод, который создает вакансию на основе словаря
    """
    @classmethod
    def from_json(cls, params):
        return cls(params['title'], params['url'], params['pay'], params['requirement'])
    
    """
    КлассМетод, который создает массив вакансий на основе информации из json файла
    """
    @classmethod
    def all_from_json(cls):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        output = []
        for vacancy in vacancies:
            tmp = Vacancy.from_json(vacancy)
            output.append(tmp)
        return output
    
    """
    Метод, который выводит в консоль ифнормацию о вакансии
    """
    def show_info(self):
        print(self.title)
        print(self.url)
        print(f'Заработная плата {self.pay}')
        print(self.requirement)

    def __repr__(self) -> str:
        return f"{self.title}\n{self.pay}\n{self.url}\n{self.requirement}"