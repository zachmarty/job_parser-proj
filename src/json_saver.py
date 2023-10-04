import json
from src.vacancy import Vacancy
FILE = 'vacancies.json'

class JSON_saver():
    def check_for_repeat(self, vacancy:Vacancy):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
            if vacancy.json() in vacancies:
                return False
            else:
                return True

    def add_vacancy(self, vacancy:Vacancy):
        if self.check_for_repeat(vacancy):
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
            vacancies.append(vacancy.json())
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)

    def get_vacancies_by_salary(self, params):
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
    
    def delete_vacancy(self, vacancy):
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        for item in vacancies:
            if item == vacancy.json():
                vacancies.remove(vacancy.json())
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False)