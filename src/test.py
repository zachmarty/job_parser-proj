from src.api import SuperJob_Api, HH_Api
from json_agent import JSON_agent
from src.vacancy import Vacancy
from vacancy_agent import Vacancy_agent

#if __name__ == "__main__":
hh_vacancies_count = int(input('Введите количество вакансий для сайта hh.ru '))
sj_vacancies_count = int(input('Введите количество вакансий для сайта superjob '))
search_words = input('Введите ключевые слова для поиска ').split()

print()

hh_api = HH_Api(hh_vacancies_count)
sj_api = SuperJob_Api(sj_vacancies_count)

hh_vacancies = Vacancy_agent.pars_hh_ru(hh_api.get_vacancies(search_words))
sj_vacancies = Vacancy_agent.pars_super_job(sj_api.get_vacancies(search_words))

for vacancy in hh_vacancies + sj_vacancies:
    JSON_agent.add_vacancy(vacancy)

JSON_agent.show_vacancies_title()
print()
title = input('Введите название вакансии для удаления ')
JSON_agent.delete_vacancy_by_title(title)
