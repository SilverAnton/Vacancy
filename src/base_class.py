from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Базовый класс для получения вакансий из источника"""

    @abstractmethod
    def __init__(*args, **kwargs):
        pass

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def save_as_json(self):
        pass


class ConvertUserVacancyBase(ABC):
    @abstractmethod
    def add_vacancy_to_json(self, *args):
        pass

    @abstractmethod
    def get_vacancy_by_keyword(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_vacancy_from_json(self, *args, **kwargs):
        pass
