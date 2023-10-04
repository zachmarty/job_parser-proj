import json
from src.vacancy import Vacancy
FILE = 'vacancies.json'

class JSON_agent():
    @staticmethod
    def check_for_repeat(vacancy:Vacancy):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
            if vacancy.json() in vacancies:
                return False
            else:
                return True
    @staticmethod
    def add_vacancy(vacancy:Vacancy):
        if JSON_agent.check_for_repeat(vacancy):
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
            vacancies.append(vacancy.json())
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)

    @staticmethod
    def get_vacancies_by_salary(params):
        params['currency'] = 'RUR'
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        output = []
        for item in vacancies:
            if item['pay'] == params:
                output.append(Vacancy.from_json(item))
                break
        if len(output)==0:
            return None
        else:
            return output[0]
    
    @staticmethod
    def delete_vacancy_by_title(title):
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        for vacancy in vacancies:
            if vacancy['title'] == title:
                vacancies.remove(vacancy)
                break
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False)

    @staticmethod
    def show_vacancies_title():
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        for vacancy in vacancies:
            print(vacancy['title'])