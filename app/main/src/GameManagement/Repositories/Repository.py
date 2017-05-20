from pymongo import MongoClient
from pymongo.database import Database

from app.main.src.GameManagement.Models.IModel import IModel


class Repository:
    def __init__(self):
        self.conn = MongoClient('mongodb://localhost:27017/')
        self.session = self.conn['dragonCity']
        self.collection = self.__class__.__name__.replace('Repository', '').lower()

    def __get_collection(self) -> Database:
        return self.session[self.collection]

    def insert(self, model: IModel):
        self.__get_collection.insert(model)

    def update(self, model: IModel):
        return self.__get_collection().update({'id': model.get_id()}, model)

    def get(self, model: IModel):
        return self.__get_collection().find({'id': model.get_id()})

    def insert_or_update(self, model: IModel):
        return self.__get_collection().update({'id': model.get_id()}, model, upsert=True)

    def get_all(self) -> list:
        return self.__get_collection().find()
