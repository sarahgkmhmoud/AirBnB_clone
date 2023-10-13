#!/usr/bin/python3
"""Update models/__init__.py: to create a unique FileStorage instance for your application"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os

class test_instantation(unittest.TestCase):
    """Don't Forget the command"""
    def test_with_None_argument(self):
        """Don't forget the doc"""
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def test_without_argument(self):

        self.assertIsInstance(FileStorage(), FileStorage)
    def test_Attribution_type(self):
        storage = FileStorage()
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertEqual(type(storage.all()),dict)

    def test_Attribution_value(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertEqual(storage._FileStorage__objects, {})

    #     storage._FileStorage.__file_path
    #     self.assertEquals(type(file), str)

# class test_BaseModelSave(unittest.TestCase):
#     @classmethod
#     def setUp(self):
#         self.all_objs = storage.all()
#         for self.obj_id in self.all_objs.keys():
#             self.obj = self.all_objs[self.obj_id]

#         self.B3 = BaseModel()
#         self.B3.name = "My_First_Model"
#         self.B3.my_number = 89
#         self.B3.save()
#         try:
#             os.rename("file.json", "tmp")
#         except IOError:
#             pass

#     @classmethod
#     def tearDown(self):
#         try:
#             os.remove("file.json")
#         except IOError:
#             pass
#         try:
#             os.rename("tmp", "file.json")
#         except IOError:
#             pass
 

if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
   