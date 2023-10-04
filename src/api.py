import requests
import json
import os
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
    
class SuperJob_Api(Api):

    def __init__(self, page = 1, per_page = 1):
        self.headers = {
            #'Host': 'api.superjob.ru',
            'X-Api-App-Id': "v3.r.137511187.43b2d170d93e8717645a6aabd242773662724682.24451774d02e043398092236be85ed1b03fbbe3e",
            #'Authorization': "Bearer v3.r.137863226.1638199ac6ab29d551c10c41173bccd82beccc6a.67d32d4aa518ded5d1679637a99a807cde8e5494",
            #
            #
            #'
        }
        self.params = {
            'count': per_page,
            'page': page,
            'town': 'Moscow',
        }
        r = requests.post('https://api.superjob.ru/2.0/vacancies/', headers=self.headers)
        print(r.text)
        self.url ='https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, words):
        self.params['keywords'] = words
        r = requests.get(self.url, params=self.params)
        return r
    
