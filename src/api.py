import requests
import json
from abc import abstractclassmethod, ABC

class Api(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_vacancies(self, word):
        pass

class HH_Api(Api):
    
    def __init__(self, page = 1, per_page = 1) -> None:
        self.params = {
            'per_page': per_page,
            'area': 1,
            'page': page,
            'HH-User-Agent': 'MyApp/1.0'
        }
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, words):
        self.params['text'] = words
        r = requests.get(self.url, params=self.params)
        return r
    
