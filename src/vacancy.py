import json


class Vacancy:
    def __init__(self, name, employer, city, salary, description):
        self.name = name
        self.employer = employer
        self.city = city
        self.salary = salary
        self.description = description
        self.vacancies = []

    def __str__(self):
        return (f"должность:{self.name}, работодатель:{self.employer}, город:{self.city}, "
                f"з/п:{self.salary}, обязанности:{self.description}")

    @staticmethod
    def get_obj_list(file_vacancies):
        """ Метод загружает файл json с выбранными профессиями, фильтрует его по значениям SALARY и RESPONSIBILITY.
        Возвращает список экземпляров класса Vacancy"""
        list_vacancies = []
        with open(file_vacancies) as file:
            vacancies = json.load(file)
        for vacancy in vacancies:
            if vacancy['salary'] is None:
                vacancy['salary'] = 0
            else:
                if vacancy['salary']['from'] is None and vacancy['salary']['to'] is not None:
                    vacancy['salary'] = vacancy['salary']['to']
                elif vacancy['salary']['from'] is not None and vacancy['salary']['to'] is None:
                    vacancy['salary'] = vacancy['salary']['from']
                elif vacancy['salary']['from'] is not None and vacancy['salary']['to'] is not None:
                    vacancy['salary'] = vacancy["salary"]["from"]
            if vacancy['snippet']['responsibility'] is None:
                vacancy['snippet']['responsibility'] = 'нет описания'
            if vacancy['area']['name'] is None:
                vacancy['area']['name'] = 'город не указан'
            obj = Vacancy(vacancy['name'], vacancy['employer']['name'], vacancy['area']['name'],
                          vacancy['salary'], vacancy['snippet']['responsibility'])
            list_vacancies.append(obj)
        return list_vacancies

    def __gt__(self, other):
        """ Метод сравнивает две вакансии по зарплате, возвращает экземпляр класса WorkWithVacancy с более высокой
        зарплатой"""
        if self.salary > other.salary:
            return self
        return other

    def salary_validate(self):
        """Метод валидации данных о зарплате, если она не передана при создании экземпляра класса WorkWithVacancy"""
        if self.salary is None:
            self.salary = 0
