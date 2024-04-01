from src.base_class import BaseVacancy
import requests
import json


class Api(BaseVacancy):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        super().__init__(self)
        self.vacancies = []

    def add_vacancy(self, keyword):
        self.params['text'] = keyword
        response = requests.get(self.__url, headers=self.__headers, params=self.params)
        vacancies = response.json()['items']
        self.vacancies.append(vacancies)

    def save_as_json(self):
        with open('vacancies.json', 'w', encoding="UTF8") as file:
            json.dump(self.vacancies[0], file, ensure_ascii=False, indent=4)
