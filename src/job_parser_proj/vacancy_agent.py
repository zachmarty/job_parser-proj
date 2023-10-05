from job_parser_proj.vacancy import Vacancy


"""
Класс для работы с вакансиями
"""
class Vacancy_agent():
    """
    Метод, который получает на вход словарь из superjob и возвращает массив Vacancy
    """
    @staticmethod
    def pars_super_job(vacancies):
        output = []
        for vacancy in vacancies:
            if vacancy['payment_from'] != None:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], vacancy['payment_from'], vacancy['candidat'])
            elif vacancy['payment_to'] != None:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], vacancy['payment_to'], vacancy['candidat'])
            else:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], '0', vacancy['candidat'])
            output.append(tmp)
        return output
    
    """
    Метод, который получает на вход словарь из hh.ru и возвращает массив Vacancy
    """
    @staticmethod
    def pars_hh_ru(vacancies):
        output = []
        for vacancy in vacancies:
            if vacancy['salary'] != None:
                if vacancy['salary']['from'] != None:
                    tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', vacancy['salary']['from'], vacancy['snippet']['requirement'])
                else:
                    tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', vacancy['salary']['to'], vacancy['snippet']['requirement'])
            else:
                tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', "0", vacancy['snippet']['requirement'])
            output.append(tmp)
        return output
    
    """
    Метод, который возвращает названия вакансий по заданным словам для поиска
    """
    @staticmethod
    def filter_vacancies_by_keywords(vacancies:list, key_words = []):
        output = []
        for vacancy in vacancies:
            title = [x.lower() for x in vacancy.title.split()]
            try:
                requiremets = [x.lower() for x in vacancy.requirement.split()]
            except:
                requiremets = []
            for key_word in key_words:
                if key_word.lower() in title or key_word.lower() in requiremets:
                    output.append(vacancy.title)
                    break
        return output
    
    """
    Метод, который возвращает названия вакансий по заданному диапазону заработной платы
    """
    @staticmethod
    def filter_vacancies_by_salary(vacancies: list, sfrom, sto):
        output = []
        for vacancy in vacancies:
            try:
                if vacancy.pay >= sfrom and vacancy.pay <= sto:
                    output.append(vacancy.title)
            except:
                pass
        return output

