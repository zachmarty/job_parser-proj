from job_parser_proj.api import HH_Api, SuperJob_Api
from job_parser_proj.vacancy_agent import Vacancy_agent
from job_parser_proj.vacancy import Vacancy
from job_parser_proj.json_agent import JSON_agent

def test():
    print('fine')

def load_vacancies_to_json():
    hh_vacancies_count = int(input('Введите количество вакансий для сайта hh.ru '))
    sj_vacancies_count = int(input('Введите количество вакансий для сайта superjob '))
    search_words = input('Введите ключевые слова для поиска ').split()
    print()
    hh_api = HH_Api(hh_vacancies_count)
    sj_api = SuperJob_Api(sj_vacancies_count)

    hh_vacancies = Vacancy_agent.pars_hh_ru(hh_api.get_vacancies(search_words))
    sj_vacancies = Vacancy_agent.pars_super_job(sj_api.get_vacancies(search_words))

    counter = 0
    for vacancy in hh_vacancies + sj_vacancies:
        if JSON_agent.add_vacancy(vacancy):
            counter += 1
    print(f'Добавлено {counter} вакансий')

def show_vacancies_by_title():
    JSON_agent.show_vacancies_title()

def delete_vacancy_by_title():
    title = input('Введите название вакансии для удаления ')
    if JSON_agent.delete_vacancy_by_title(title):
        print(f'Вакансия {title} удалена')
    else:
        print(f'Вакансия {title} не найдена')
