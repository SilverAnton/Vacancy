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


class ConvertVacancyToJson(ABC):
    @abstractmethod
    def add_vacancy_to_json(*args, **kwargs):
        pass

    @abstractmethod
    def get_vacancy_from_json(*args, **kwargs):
        pass

    @abstractmethod
    def del_vacancy_from_json(*args, **kwargs):
        pass
