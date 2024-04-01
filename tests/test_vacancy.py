import pytest

from src.vacancy import Vacancy
from src.api import Api

obj1 = Api()
obj_vacancy = Vacancy('python developer', 'Capcom', 'Osaka', None, 'you will be crying')


@pytest.fixture
def list_obj_vacancy():
    obj1.add_vacancy('junior')
    obj1.save_as_json()
    return Vacancy.get_obj_list('vacancies.json')


def test_get_obj_list(list_obj_vacancy):
    assert isinstance(list_obj_vacancy[0], Vacancy)


def test__gt__(list_obj_vacancy):
    assert list_obj_vacancy[0].__gt__(list_obj_vacancy[5]) == list_obj_vacancy[0]


def test__str__(list_obj_vacancy):
    assert print(list_obj_vacancy[0]) == print('должность:Junior Frontend-разработчик (React), работодатель: Upsilon, '
                                               'город: Алматы, з/п:150000, обязанности:нет описания')


def test_salary_validate():
    obj_vacancy.salary_validate()
    assert obj_vacancy.salary == 0


def test__init__(list_obj_vacancy):
    assert list_obj_vacancy[0].name == 'Junior Frontend-разработчик (React)'
    assert list_obj_vacancy[0].employer == 'Upsilon'
    assert list_obj_vacancy[0].city == 'Алматы'
    assert list_obj_vacancy[0].salary == 150000
    assert list_obj_vacancy[0].description == 'нет описания'
