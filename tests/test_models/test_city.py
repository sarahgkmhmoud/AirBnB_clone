#!/usr/bin/python3
"""test suit to test base_mode module"""
import unittest
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from models import storage
import os

class test_City_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Amenity class"""
    @classmethod
    def setUp(self):
        self.C1 = City()
        self.S1 = State()
        dictionary = self.C1.to_dict()
        self.C2 = City(** dictionary)
        self.dictionary2 = self.C2.to_dict()
        self.C3 = City()
        self.C3.name = 'Cairo'
        self.C3.state_id = self.S1.id
        self.C3.id = 20
        self.dictionary3 = {
                             '__class__': City,
                             'name': 'Luxer'
                             }
        self.C4 = City(**self.dictionary3)
        self.dictionary4 = self.C4.to_dict()
        self.C5 = City(**self.dictionary3)


    def test_initialize_CityRegular(self):
        self.assertIs(type(self.C1.id), str)
        self.assertIs(type(self.C1.created_at), datetime)
        self.assertIs(type(self.C1.updated_at), datetime)

    def test_equality_created_new_Cityinstances(self):
        self.assertIsNot(self.C1, self.C2)
        self.assertEqual(self.C2.updated_at, self.C1.updated_at)
        self.assertEqual(self.C2.created_at, self.C1.created_at)
        self.assertEqual(self.C2.id, self.C1.id)

    def test_equality_created_from__Citydictionary(self):
        self.assertEqual(self.C4.name, self.C5.name)

    def test_equality_created_directly(self):
        self.assertEqual(self.C3.name, 'Cairo')
        self.assertEqual(self.C3.id, 20)
        self.assertEqual(self.C3.state_id, self.S1.id)

class test_CityKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
       self.C1 = City()
       self.dictionary3 = {
        '__class__': City, 'name': 'Daraw'}
       self.C2 = City(** self.dictionary3)

    def test_kwargsNotExist(self):
        self.assertNotIn('__class__', self.C1.__dict__)
        self.assertNotIn('name', self.C1.__dict__)
        self.assertIn('id', self.C1.__dict__)
        self.assertIn('created_at', self.C1.__dict__)
        self.assertIn('updated_at', self.C1.__dict__)


    def test_kwargsExist(self):

        self.assertNotIn('__class__', self.C2.__dict__)
        self.assertIn('name', self.C2.__dict__)
        self.assertNotIn('id', self.C2.__dict__)
        self.assertNotIn('created_at', self.C2.__dict__)
        self.assertNotIn('updated_at', self.C2.__dict__)

class test_CityStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.C1 = City()
        self.dictionary3 = {
        '__class__': City, 'name': 'Qena', 'id': '20'}
        self.C5 = City(**self.dictionary3)

    def test_str_method(self):
        expected_str = f"[{self.C1.__class__.__name__}] ({self.C1.id}) {self.C1.__dict__}"
        self.assertEqual(str(self.C1),expected_str)
        expected_str2 = f"[{self.C5.__class__.__name__}] (20) {self.C5.__dict__}"
        self.assertEqual(str(self.C5),expected_str2)

class test_CitySaveMethod(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.C3 = City()
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
        old_updated_at = self.C3.updated_at
        self.C3.name = 'Alexandria'
        self.C3.save()
        self.assertNotEqual(self.C3.created_at, self.C3.updated_at)
        self.assertNotEqual(old_updated_at, self.C3.updated_at)

class test_CityEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        C6 = City()
        C7 = City()
        self.assertNotEqual(C6, C7)
    def test_inequality_between_different_instances(self):
        dictionary5 = {
        '__class__': City, 'name': 'Alex'}

        C8 = City(**dictionary5)
        C9 = City(**dictionary5)

        self.assertNotEqual(C8, C9)


class test_CitySerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.C10 = City()
        self.C10_dict = self.C10.to_dict()
    def test_serialization_to_dict(self):
        self.assertIsInstance(self.C10_dict, dict)
    def test_formatDateTime(self):
        self.assertIs(type(self.C10_dict['created_at']), str)
        self.assertIs(type(self.C10_dict['updated_at']), str)


class test_CityDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.C1 = City()
        dictionary = self.C1.to_dict()
        self.C2 = City(** dictionary)

    def test_desrialization_to_dic(self):
        self.assertIsNot(self.C1, self.C2)

    def test_check_type_desrialization(self):
        self.assertIs(type(self.C1.id), str)
        self.assertIs(type(self.C1.created_at), datetime)
        self.assertIs(type(self.C1.updated_at), datetime)
        self.assertIs(type(self.C2.id), str)
        self.assertIs(type(self.C2.created_at), datetime)
        self.assertIs(type(self.C2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.C2.id, self.C1.id)
        self.assertEqual(self.C2.updated_at, self.C1.updated_at)
        self.assertEqual(self.C2.created_at, self.C1.created_at)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
