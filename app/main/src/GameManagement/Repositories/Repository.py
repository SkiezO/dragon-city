from app import PERSISTENCE_ENGINE
from app.main.src.GameManagement import Model
from app.main.src.GameManagement.Repositories.PersistenceOperations import PersistenceOperations


class Repository(PersistenceOperations):
    def __init__(self, model: Model):
        self.engine = getattr(__import__('app').main.src.GameManagement.Repositories.Engines, PERSISTENCE_ENGINE)(model)

    def __getattr__(self, item):
        return self.engine.__getattr__(item)

    def insert(self, model: Model):
        return self.engine.insert(model)

    def update(self, model: Model):
        return self.engine.insert(model)

    def insert_or_update(self, model: Model):
        return self.engine.insert_or_update(model)

    def get(self, model: Model):
        return self.engine.get(model)

    def get_all(self) -> list:
        return self.engine.get_all()
