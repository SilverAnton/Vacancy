import json

from src.base_class import ConvertUserVacancyBase


class ConvertUserVacancy(ConvertUserVacancyBase):

    @staticmethod
    def add_vacancy_to_json(vacancies):
        """Метод принимает список экземпляров класса Vacancy и добавляет их объекты в json файл"""
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append({'работодатель': vacancy.employer,
                                   'вакансия': vacancy.name,
                                   'город': vacancy.city,
                                   'заработная плата': vacancy.salary,
                                   'описание вакансии': vacancy.description
                                   })
        with open('user_vacancies.json', 'w', encoding="UTF8") as file:
            json.dump(list_vacancies, file, ensure_ascii=False, indent=4)

    @staticmethod
    def get_vacancy_by_keyword(keyword):
        """Метод сортирует выбранные вакансии по ключевому слову и возвращает отсортированные в формате str"""
        with open('user_vacancies.json', 'r', encoding="UTF8") as file:
            list_vacancies = json.load(file)
            vacancy_by_keyword = []
            result = ''
            for vacancy in list_vacancies:
                if keyword in vacancy["работодатель"] or keyword in vacancy["вакансия"] or keyword in vacancy["город"] or keyword in vacancy["описание вакансии"]:
                    vacancy_by_keyword.append(vacancy)
            for items in vacancy_by_keyword:
                for k, v in items.items():
                    result += f"{k}: {v}\n"
                    if k == "описание вакансии":
                        result += f"\n"
            return result

    @staticmethod
    def sort_vacancies_by_salary(top_count):
        """Метод возвращает выбранное количество вакансий с наибольшей зарплатой """
        with open('user_vacancies.json') as file:
            vacancies = json.load(file)
            sorted_list = sorted(vacancies, key=lambda x: x['заработная плата'], reverse=True)
            result = ''
            for i in sorted_list[0:top_count]:
                for k, v in i.items():
                    result += f"{k}: {v}\n"
                    if k == "описание вакансии":
                        result += f"\n"
            return result

    def del_vacancy_from_json(self, *args, **kwargs):
        pass
