from job_parser_proj.api import HH_Api, SuperJob_Api
from job_parser_proj.vacancy_agent import Vacancy_agent
from job_parser_proj.json_agent import JSON_agent
from job_parser_proj.vacancy import Vacancy

def load_vacancies_to_json():
    """
    Функция для загрузки и записи вакансий с сервисов в файл vacancies.json
    """
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
    """
    Выводит в консоль названия вакансий
    """
    JSON_agent.show_vacancies_title()

def delete_vacancy_by_title():
    """
    Удаляет вакансию по названию
    """
    title = input('Введите название вакансии для удаления ')
    if JSON_agent.delete_vacancy_by_title(title):
        print(f'Вакансия {title} удалена')
    else:
        print(f'Вакансия {title} не найдена')

def clear_json():
    """
    Очищает файл vacancies.json
    """
    JSON_agent.clear_json()
    print('Файл очищен')

def show_info_by_title():
    """
    Выводит информацию о вакансии по её названию
    """
    title = input('Введите название вакансии для поиска ')
    JSON_agent.show_info_by_title(title)

def get_vacancies_by_kwards():
    """
    Выводит названия вакансий в консоль по ключевым словам
    """
    kwards = input('Введите ключевые слова для поиска ').split()
    vacancies = Vacancy.all_from_json()
    filtered = Vacancy_agent.filter_vacancies_by_keywords(vacancies, kwards)
    if len(filtered) > 0:
        for title in filtered:
            print(title)
    else:
        print('Вакансий по таким словам не найдено')

def get_vacancies_by_salary():
    """
    Выводит названия вакансий в консоль по диапазону заработной платы
    """
    try:
        sfrom = int(input('Введите заработную плату от '))
    except:
        sfrom = 30000
    try:
        sto = int(input('Введите заработную плату до '))
    except:
        sto = 60000
    vacancies = Vacancy.all_from_json()
    filtered = Vacancy_agent.filter_vacancies_by_salary(vacancies, sfrom, sto)
    if len(filtered) > 0:
        for title in filtered:
            print(title)
    else:
        print('Вакансий по такому диапазону зарплаты не найдено')

def sort_vacancies_by_salary():
    """
    Сортирует вакансии по заработной плате (от большего к меньшему)
    """
    vacancies = Vacancy.all_from_json()
    vacancies = sorted(vacancies, key=lambda x: int(x.pay), reverse=True)
    JSON_agent.clear_json()
    for vacancy in vacancies:
        JSON_agent.add_vacancy(vacancy)
    print('Файл отсортирован')

def show_top_n():
    """
    Выводит в консоль информацию о первых н вакансиях
    """
    try:
        n = int(input('Введите количество вакансий для просмотра '))
    except:
        print('Число введено некорректно')
        exit()
    vacancies = Vacancy.all_from_json()
    counter = 0
    if n > len(vacancies):
        n = len(vacancies)
    while counter < n:
        print(vacancies[counter].title)
        counter += 1


