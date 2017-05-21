from typing import Type, ClassVar

from app.main.src.GameManagement import Model
from app.main.src.GameManagement.Repositories import Repository


class MongoAdapter:

    @staticmethod
    def mongo_to_model(mongo_dict: dict, clazz: Type):
        obj_instance = clazz()
        for prop in clazz.__annotations__:
            if prop == 'id':
                setattr(obj_instance, prop, mongo_dict['_id'])
            elif issubclass(type(clazz.__annotations__[prop]), Type) and issubclass(clazz.__annotations__[prop], Model):
                repository = Repository.Repository(clazz.__annotations__[prop])
                setattr(obj_instance, prop, repository.get_by_id(mongo_dict["{0}_id".format(prop)])[0])
            else:
                setattr(obj_instance, prop, mongo_dict[prop])
        return obj_instance

    @staticmethod
    def model_to_mongo(model: Model):
        prop_list = model.__dict__.copy()
        for prop in prop_list:
            if isinstance(prop_list[prop], Model):
                prop_list["{0}_id".format(prop.lower())] = prop_list[prop].get_id()
                prop_list.pop(prop, None)
            if prop == 'id':
                prop_list['_id'] = prop_list['id']
                prop_list.pop('id', None)
        return prop_list
