from job_parser_proj.vacancy import Vacancy

class Vacancy_agent():
    @staticmethod
    def pars_super_job(vacancies):
        output = []
        for vacancy in vacancies:
            tmp = Vacancy(vacancy['profession'], vacancy['link'], {'from': vacancy['payment_from'], 'to': vacancy['payment_to'], 'currency': 'RUR', 'gross': False}, vacancy['candidat'])
            output.append(tmp)
        return output
    
    @staticmethod
    def pars_hh_ru(vacancies):
        output = []
        for vacancy in vacancies:
            tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', vacancy['salary'], vacancy['snippet']['requirement'])
            output.append(tmp)
        return output
    
    @staticmethod
    def filter_vacancies_by_keywords(hh_ru_collection: list = [], super_job_collection: list = [], key_words = ['Python']):
        output = []
        for vacancy in hh_ru_collection + super_job_collection:
            title = [x.lower() for x in vacancy.tittle.split()]
            requiremets = [x.lower() for x in vacancy.requirement.split()]
            for key_word in key_words:
                if key_word.lower() in title or key_word.lower() in requiremets:
                    output.append(vacancy)
                    break
        return output
    
    @staticmethod
    def filter_vacancies_by_salary():
        pass

