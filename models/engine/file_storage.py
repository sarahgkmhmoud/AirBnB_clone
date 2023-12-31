#!/usr/bin/python3
"""Write a class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary -
    empty but will store all objects by <class name>.id"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        id = obj.id
        key = f"{class_name}.{id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        objs = FileStorage.__objects
        objs_dict = {obj: objs[obj].to_dict()for obj in objs.keys()}
        with open(self.__file_path, mode='w') as file_json:
            json.dump(objs_dict, file_json)

    def reload(self):
        """reload object from file jason"""

        definedClasses = {'BaseModel': BaseModel, 'User': User,
                          'State': State, 'City': City,
                          'Amenity': Amenity, 'Place': Place, 'Review': Review}
        try:
            with open(self.__file_path) as file_json:
                obj_dict = json.load(file_json)
                for value in obj_dict.values():
                    clsName = value['__class__']
                    self.new(definedClasses.get(clsName)(**value))
        except FileNotFoundError:
            pass
