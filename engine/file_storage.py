#!/usr/bin/python3
"""Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
import json


class FileStorage:
    """Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id"""

    def __init__(self):
        """iniailize the private attributions"""
        self.__file_path = 'cls__name__'+'.json'
        self.__objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects;

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.cls__name__
        id = obj.id
        key = "{0}.{1}".format(class_name, id)
        self.__objects['key'] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open (self.__file_path, mode='w', encoding='utf-8')  as file_json:
            json_string = json.dumps(self.__objects)
            file_json.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open (self.__file_path, mode='r', encoding='utf-8')  as file_json:
                json_string = file_json.read()
                return json.loads(json_string)
        except FileNotFoundError:
            pass
