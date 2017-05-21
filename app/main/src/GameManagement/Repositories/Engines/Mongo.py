from pymongo import MongoClient
from pymongo.database import Database

from app.main.src.GameManagement.Adapters import MongoAdapter
from app.main.src.GameManagement.Models.Model import Model
from app.main.src.GameManagement.Repositories.Engines.Engine import Engine


class Mongo(Engine):
    def __init__(self, model: Model):
        self.conn = MongoClient('mongodb://localhost:27017/')
        self.session = self.conn['dragonCity']
        self.model = model
        self.collection = self.model.__name__.lower()

    def __getattr__(self, item):
        field = item.replace('get_by_', '')
        field = '_id' if field == 'id' else field
        return lambda value: [MongoAdapter.mongo_to_model(result, self.model) for result in self.__get_collection().find({field: value})]

    def __get_collection(self) -> Database:
        return self.session[self.collection]

    def insert(self, model: Model):
        return self.__get_collection().insert(MongoAdapter.model_to_mongo(model))

    def update(self, model: Model):
        return self.__get_collection().update({'_id': model.get_id()}, model.serialize())

    def insert_or_update(self, model: Model):
        return self.__get_collection().update({'_id': model.get_id()}, MongoAdapter.model_to_mongo(model), upsert=True)

    def get(self, model: Model):
        return MongoAdapter.mongo_to_model(self.__get_collection().find({'_id': model.get_id()})[0], self.model)

    def get_all(self) -> list:
        return self.__get_collection().find()
