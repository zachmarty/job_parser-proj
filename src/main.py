from src.api import HH_Api
from src.json_saver import JSON_saver
from src.vacancy import Vacancy
import json

if __name__ == "__main__":
    hh_agent = HH_Api()
    json_saver = JSON_saver()
    vacancies = hh_agent.get_vacancies('Python').text
    vacancies = json.loads(vacancies)
    for raw in vacancies['items']:
        vacancy = Vacancy(raw['name'], f'https://hh.ru/vacancy/{raw["id"]}', raw['salary'], raw['snippet']['requirement'])
        json_saver.add_vacancy(vacancy)