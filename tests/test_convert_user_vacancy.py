import pytest

from src.convert_user_vacancy import ConvertUserVacancy
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy.get_obj_list('vacancies.json')


@pytest.fixture
def convert_user_vacancy(vacancy):
    return ConvertUserVacancy.add_vacancy_to_json(vacancy)


def test_get_vacancy_by_keyword(convert_user_vacancy):

    assert ConvertUserVacancy.get_vacancy_by_keyword('Самара') == ''


def test_sort_vacancies_by_salary(convert_user_vacancy):

    assert print(ConvertUserVacancy.sort_vacancies_by_salary(1)) == print(
        'работодатель: OOO UZGPS\nвакансия: Junior Front-End разработчик JS\nгород: Ташкент\nзаработная плата: '
        '3500000\nописание вакансии: нет описания\n')
