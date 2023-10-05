from scripts.scripts import *

"""
Файл, в котором представлена работа всех скриптов поочередно
"""
if __name__== "__main__":
    load_vacancies_to_json()
    print()
    show_vacancies_by_title()
    print()
    delete_vacancy_by_title()
    print()
    show_info_by_title()
    print()
    get_vacancies_by_kwards()
    print()
    get_vacancies_by_salary()
    print()
    sort_vacancies_by_salary()
    print()
    show_top_n()
    print()
    clear_json()