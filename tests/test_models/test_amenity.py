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
        self.assertIs(type(self.A1.id), str)
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
       self.A2 = Amenity(** self.dictionary3)

    def test_kwargsNotExist(self):
        self.assertNotIn('__class__', self.A1.__dict__)
        self.assertNotIn('name', self.A1.__dict__)
        self.assertNotIn('number', self.A1.__dict__)
        self.assertIn('id', self.A1.__dict__)
        self.assertIn('created_at', self.A1.__dict__)
        self.assertIn('updated_at', self.A1.__dict__)


    def test_kwargsExist(self):

        self.assertNotIn('__class__', self.A2.__dict__)
        self.assertIn('name', self.A2.__dict__)
        self.assertIn('number', self.A2.__dict__)
        self.assertNotIn('id', self.A2.__dict__)
        self.assertNotIn('created_at', self.A2.__dict__)
        self.assertNotIn('updated_at', self.A2.__dict__)

class test_AmenityStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.A1 = Amenity()
        self.dictionary3 = {
        '__class__': Amenity, 'name': 'free Wifi', 'id': '20'}
        self.A5 = Amenity(**self.dictionary3)

    def test_str_method(self):
        expected_str = f"[{self.A1.__class__.__name__}] ({self.A1.id}) {self.A1.__dict__}"
        self.assertEqual(str(self.A1),expected_str)
        expected_str2 = f"[{self.A5.__class__.__name__}] (20) {self.A5.__dict__}"
        self.assertEqual(str(self.A5),expected_str2)

class test_AmenitySaveMethod(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.A3 = Amenity()
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
        old_updated_at = self.A3.updated_at
        self.A3.name = 'Air condition'
        self.A3.save()
        self.assertNotEqual(self.A3.created_at, self.A3.updated_at)
        self.assertNotEqual(old_updated_at, self.A3.updated_at)

class test_AmenityEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        A6 = Amenity()
        A7 = Amenity()
        self.assertNotEqual(A6, A7)
    def test_inequality_between_different_instances(self):
        dictionary5 = {
        '__class__': Amenity, 'name': 'Garden'}

        A8 = Amenity(**dictionary5)
        A9 = Amenity(**dictionary5)

        self.assertNotEqual(A8, A9)


class test_AmenitySerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.A10 = Amenity()
        self.A10_dict = self.A10.to_dict()
    def test_serialization_to_dict(self):
        self.assertIsInstance(self.A10_dict, dict)
    def test_formatDateTime(self):
        self.assertIs(type(self.A10_dict['created_at']), str)
        self.assertIs(type(self.A10_dict['updated_at']), str)


class test_AmenityDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.A1 = Amenity()
        dictionary = self.A1.to_dict()
        self.A2 = Amenity(** dictionary)

    def test_desrialization_to_dic(self):
        self.assertIsNot(self.A1, self.A2)

    def test_check_type_desrialization(self):
        self.assertIs(type(self.A1.id), str)
        self.assertIs(type(self.A1.created_at), datetime)
        self.assertIs(type(self.A1.updated_at), datetime)
        self.assertIs(type(self.A2.id), str)
        self.assertIs(type(self.A2.created_at), datetime)
        self.assertIs(type(self.A2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.A2.id, self.A1.id)
        self.assertEqual(self.A2.updated_at, self.A1.updated_at)
        self.assertEqual(self.A2.created_at, self.A1.created_at)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()

