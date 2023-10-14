#!/usr/bin/python3
"""test suit to test amenity module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from uuid import uuid4
from datetime import datetime
from models import storage
import os


#don't forget add pycode style test
#don't forget add Doc style test
#don't forget documented the test models


class test_Amenity_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Amenity class"""
    @classmethod
    def setUp(self):
        self.A1 = Amenity()
        dictionary = self.A1.to_dict()
        self.A2 = Amenity(** dictionary)
        self.dictionary2 = self.A2.to_dict()
        self.A3 = Amenity()
        self.A3.name = 'WiFi'
        self.A3.id = 20
        self.dictionary3 = {
                             '__class__': Amenity,
                             'name': 'breakfast'
                             }
        self.A4 = Amenity(**self.dictionary3)
        self.dictionary4 = self.A4.to_dict()
        self.A5 = Amenity(**self.dictionary3)


    def test_initialize_AmenityRegular(self):
        self.assertIs(type(self.U1.id), str)
        self.assertIs(type(self.A1.created_at), datetime)
        self.assertIs(type(self.A1.updated_at), datetime)

    def test_equality_created_new_Amenityinstances(self):
        self.assertIsNot(self.A1, self.A2)
        self.assertEqual(self.A2.updated_at, self.A1.updated_at)
        self.assertEqual(self.A2.created_at, self.A1.created_at)
        self.assertEqual(self.A2.id, self.A1.id)

    def test_equality_created_from__Amenitydictionary(self):
        self.assertEqual(self.A4.name, self.A5.name)

    def test_equality_created_directly(self):
        self.assertEqual(self.A3.name, 'WiFi')
        self.assertEqual(self.A3.id, 20)

class test_AmenityKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
       self.A1 = Amenity()
       self.dictionary3 = {
        '__class__': Amenity, 'name': 'this dictionary', 'number': 98}
       self.B2 = BaseModel(** self.dictionary3)

    def test_kwargsNotExist(self):
        self.assertNotIn('__class__', self.B1.__dict__)
        self.assertNotIn('name', self.B1.__dict__)
        self.assertNotIn('number', self.B1.__dict__)
        self.assertIn('id', self.B1.__dict__)
        self.assertIn('created_at', self.B1.__dict__)
        self.assertIn('updated_at', self.B1.__dict__)


    def test_kwargsExist(self):

        self.assertNotIn('__class__', self.B2.__dict__)
        self.assertIn('name', self.B2.__dict__)
        self.assertIn('number', self.B2.__dict__)
        self.assertNotIn('id', self.B2.__dict__)
        self.assertNotIn('created_at', self.B2.__dict__)
        self.assertNotIn('updated_at', self.B2.__dict__)

class test_BaseModelStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.B1 = BaseModel()
        self.dictionary3 = {
        '__class__': BaseModel, 'name': 'this dictionary', 'number': 98, 'id': '20'}
        self.B5 = BaseModel(**self.dictionary3)

    def test_str_method(self):
        expected_str = f"[{self.B1.__class__.__name__}] ({self.B1.id}) {self.B1.__dict__}"
        self.assertEqual(str(self.B1),expected_str)
        expected_str2 = f"[{self.B5.__class__.__name__}] (20) {self.B5.__dict__}"
        self.assertEqual(str(self.B5),expected_str2)

class test_BaseModelSaveMethod(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.B3 = BaseModel()
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


    def test_save_Regular(self):
        old_updated_at = self.B3.updated_at
        self.B3.name = 'second module'
        self.B3.save()
        self.assertNotEqual(self.B3.created_at, self.B3.updated_at)
        self.assertNotEqual(old_updated_at, self.B3.updated_at)

class test_BaseModelEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        B6 = BaseModel()
        B7 = BaseModel()
        self.assertNotEqual(B6, B7)
    def test_inequality_between_different_instances(self):
        dictionary5 = {
        '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}

        B8 = BaseModel(**dictionary5)
        B9 = BaseModel(**dictionary5)

        self.assertNotEqual(B8, B9)


class test_BaseModelSerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.B10 = BaseModel()
        self.B10_dict = self.B10.to_dict()
    def test_serialization_to_dict(self):
        self.assertIsInstance(self.B10_dict, dict)
    def test_formatDateTime(self):
        self.assertIs(type(self.B10_dict['created_at']), str)
        self.assertIs(type(self.B10_dict['updated_at']), str)


class test_BaseModelDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.B1 = BaseModel()
        dictionary = self.B1.to_dict()
        self.B2 = BaseModel(** dictionary)

    def test_desrialization_to_dic(self):
        self.assertIsNot(self.B1, self.B2)

    def test_check_type_desrialization(self):
        self.assertIs(type(self.B1.id), str)
        self.assertIs(type(self.B1.created_at), datetime)
        self.assertIs(type(self.B1.updated_at), datetime)
        self.assertIs(type(self.B2.id), str)
        self.assertIs(type(self.B2.created_at), datetime)
        self.assertIs(type(self.B2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.B2.id, self.B1.id)
        self.assertEqual(self.B2.updated_at, self.B1.updated_at)
        self.assertEqual(self.B2.created_at, self.B1.created_at)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()

