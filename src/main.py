from src.api import Api
from src.convert_user_vacancy import ConvertUserVacancy
from src.vacancy import Vacancy


def main_foo():
    obj1 = Api()
    obj1.add_vacancy(input('введите ключевое слово для поиска вакансий'))
    obj1.save_as_json()
    list_vacancies = Vacancy.get_obj_list('vacancies.json')
    ConvertUserVacancy.add_vacancy_to_json(list_vacancies)
    top_count = int(input("введите количество ТОП-вакансий, по уровню зарплаты"))
    if type(top_count) is int:
        print(ConvertUserVacancy.sort_vacancies_by_salary(top_count))
    else:
        print('неверное значение')
    print(ConvertUserVacancy.get_vacancy_by_keyword(str(input('введите ключевое слово '
                                                              'для сортировки списка вакансий'))))


main_foo()
