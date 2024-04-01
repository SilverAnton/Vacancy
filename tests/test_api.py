import pytest

from src.api import Api


@pytest.fixture
def api():
    return Api()


def test_add_vacancy(api):
    api.add_vacancy('python')
    assert len(api.vacancies[0]) == 100
