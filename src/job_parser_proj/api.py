import requests
import json
import os
from abc import abstractclassmethod, ABC
"""
Файл для хранения классов по работе с api
"""
class Api(ABC):
    """
    Абстрактный класс - база
    """
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_vacancies(self, word):
        pass

class HH_Api(Api):
    """
    Класс для работы с апи на hh.ru
    """
    def __init__(self, count) -> None:
        """
        Конструктор с входным параметром количество вакансий, который устанавливает параметры для гет-запросов
        """
        self.params = {
            'per_page': count,
            'area': 1,
            'page': 1           
        }
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, words):
        """
        Метод для получения вакансий и преобразования их из json в словари
        """
        self.params['text'] = words
        r = requests.get(self.url, params=self.params)
        vacancies = json.loads(r.text)['items']
        return vacancies
    
class SuperJob_Api(Api):
    """
    Класс для работы с апи на superjob.ru
    """
    def __init__(self, count):
        """
        Конструктор с входным параметром количества вакансий, который устанавливает параметры и заголовки для гет-запросов
        """
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv("SECRET_KEY"),
        }
        self.params = {
            'count': count,
            'page': 1,
            'town': 'Moscow',
        }
        self.url ='https://api.superjob.ru/2.0/vacancies/'
        

    def get_vacancies(self, words):
        """
        Метод для получения вакансий и преобразования их из json в словари
        """
        self.params['keywords'] = words
        r = requests.get(self.url, params=self.params, headers=self.headers)
        vacancies = json.loads(r.text)['objects']
        return vacancies
    
