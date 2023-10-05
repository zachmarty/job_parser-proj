import json
from job_parser_proj.vacancy import Vacancy
FILE = 'vacancies.json'

"""
Класс для взаимодействия с json файлом, содержит статические методы
"""
class JSON_agent():
    """
    Метод для проверки на уже существующие вакансии в файле json
    """
    @staticmethod
    def check_for_repeat(vacancy:Vacancy):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
            if vacancy.json() in vacancies:
                return False
            else:
                return True
            
    """
    Метод для добавления вакансии в файл json
    """
    @staticmethod
    def add_vacancy(vacancy:Vacancy):
        if JSON_agent.check_for_repeat(vacancy):
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
            vacancies.append(vacancy.json())
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)
            return True
        else:
            return False

    """
    Метод, который удаляет вакансию из файла по её названию. Возвращает true если вакансия найдена и удалена, иначе false
    """
    @staticmethod
    def delete_vacancy_by_title(title):
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        f = False
        for vacancy in vacancies:
            if vacancy['title'] == title:
                vacancies.remove(vacancy)
                f = True
                break
        if f:
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)
            return True
        else:
            return False

    """
    Метод, который выводит в консоль названия всех вакансий в файле
    """
    @staticmethod
    def show_vacancies_title():
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        for vacancy in vacancies:
            print(vacancy['title'])

    """
    Метод, который очищает json файл
    """
    @staticmethod
    def clear_json():
        with open(FILE, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)

    """
    Метод, который выводит в консоль информацию о найденной по названию вакансии
    """
    @staticmethod
    def show_info_by_title(title):
        with open (FILE, 'r', encoding='utf-8') as f:
            vacancies = Vacancy.all_from_json()
        for vacancy in vacancies:
            if vacancy.title == title:
                vacancy.show_info()
                break