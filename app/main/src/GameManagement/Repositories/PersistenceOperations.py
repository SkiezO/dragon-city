from abc import abstractmethod

from app.main.src.GameManagement.Models import Model


class PersistenceOperations:
    @abstractmethod
    def __init__(self, model: Model):
        raise NotImplemented

    @abstractmethod
    def insert(self, model: Model):
        raise NotImplemented

    @abstractmethod
    def update(self, model: Model):
        raise NotImplemented

    @abstractmethod
    def get(self, model: Model):
        raise NotImplemented

    @abstractmethod
    def __getattr__(self, item):
        raise NotImplemented

    @abstractmethod
    def insert_or_update(self, model: Model):
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> list:
        raise NotImplemented
