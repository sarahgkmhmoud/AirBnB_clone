#!/usr/bin/python3
"""Update models/__init__.py: to create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from models import storage
import os 

class test_BaseModelSave(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.all_objs = storage.all()
        for self.obj_id in self.all_objs.keys():
            self.obj = self.all_objs[self.obj_id]

        self.B3 = BaseModel()
        self.B3.name = "My_First_Model"
        self.B3.my_number = 89
        self.B3.save()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_check_obj(self):
        expectedOutPut = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertEqual (self.obj, expectedOutPut)

    
