#!/usr/bin/python3
"""test suit to test base_mode module"""
import unittest
from models.base_model import BaseModel
from models.state import State
from uuid import uuid4
from datetime import datetime
from models import storage
import os

class test_State_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Amenity class"""
    @classmethod
    def setUp(self):
        self.S1 = State()
        dictionary = self.S1.to_dict()
        self.S2 = State(** dictionary)
        self.dictionary2 = self.S2.to_dict()
        self.S3 = State()
        self.S3.name = 'Egypt'
        self.S3.id = 20
        self.dictionary3 = {
                             '__class__': State,
                             'name': 'Palastine'
                             }
        self.S4 = State(**self.dictionary3)
        self.dictionary4 = self.S4.to_dict()
        self.S5 = State(**self.dictionary3)


    def test_initialize_StateRegular(self):
        self.assertIs(type(self.S1.id), str)
        self.assertIs(type(self.S1.created_at), datetime)
        self.assertIs(type(self.S1.updated_at), datetime)

    def test_equality_created_new_Stateinstances(self):
        self.assertIsNot(self.S1, self.S2)
        self.assertEqual(self.S2.updated_at, self.S1.updated_at)
        self.assertEqual(self.S2.created_at, self.S1.created_at)
        self.assertEqual(self.S2.id, self.S1.id)

    def test_equality_created_from__Statedictionary(self):
        self.assertEqual(self.S4.name, self.S5.name)

    def test_equality_created_directly(self):
        self.assertEqual(self.S3.name, 'Egypt')
        self.assertEqual(self.S3.id, 20)

class test_StateKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
       self.S1 = State()
       self.dictionary3 = {
        '__class__': State, 'name': 'Palastine'}
       self.S2 = State(** self.dictionary3)

    def test_kwargsNotExist(self):
        self.assertNotIn('__class__', self.S1.__dict__)
        self.assertNotIn('name', self.S1.__dict__)
        self.assertIn('id', self.S1.__dict__)
        self.assertIn('created_at', self.S1.__dict__)
        self.assertIn('updated_at', self.S1.__dict__)


    def test_kwargsExist(self):

        self.assertNotIn('__class__', self.S2.__dict__)
        self.assertIn('name', self.S2.__dict__)
        self.assertNotIn('id', self.S2.__dict__)
        self.assertNotIn('created_at', self.S2.__dict__)
        self.assertNotIn('updated_at', self.S2.__dict__)

class test_StateStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.S1 = State()
        self.dictionary3 = {
        '__class__': State, 'name': 'Egypt', 'id': '20'}
        self.S5 = State(**self.dictionary3)

    def test_str_method(self):
        expected_str = f"[{self.S1.__class__.__name__}] ({self.S1.id}) {self.S1.__dict__}"
        self.assertEqual(str(self.S1),expected_str)
        expected_str2 = f"[{self.S5.__class__.__name__}] (20) {self.S5.__dict__}"
        self.assertEqual(str(self.S5),expected_str2)

class test_StateSaveMethod(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.S3 = State()
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
        old_updated_at = self.S3.updated_at
        self.S3.name = 'Palstine'
        self.S3.save()
        self.assertNotEqual(self.S3.created_at, self.S3.updated_at)
        self.assertNotEqual(old_updated_at, self.S3.updated_at)

class test_StateEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        S6 = State()
        S7 = State()
        self.assertNotEqual(S6, S7)
    def test_inequality_between_different_instances(self):
        dictionary5 = {
        '__class__': State, 'name': 'Egypt'}

        S8 = State(**dictionary5)
        S9 = State(**dictionary5)

        self.assertNotEqual(S8, S9)


class test_StateSerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.S10 = State()
        self.S10_dict = self.S10.to_dict()
    def test_serialization_to_dict(self):
        self.assertIsInstance(self.S10_dict, dict)
    def test_formatDateTime(self):
        self.assertIs(type(self.S10_dict['created_at']), str)
        self.assertIs(type(self.S10_dict['updated_at']), str)


class test_StateDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.S1 = State()
        dictionary = self.S1.to_dict()
        self.S2 = State(** dictionary)

    def test_desrialization_to_dic(self):
        self.assertIsNot(self.S1, self.S2)

    def test_check_type_desrialization(self):
        self.assertIs(type(self.S1.id), str)
        self.assertIs(type(self.S1.created_at), datetime)
        self.assertIs(type(self.S1.updated_at), datetime)
        self.assertIs(type(self.S2.id), str)
        self.assertIs(type(self.S2.created_at), datetime)
        self.assertIs(type(self.S2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.S2.id, self.S1.id)
        self.assertEqual(self.S2.updated_at, self.S1.updated_at)
        self.assertEqual(self.S2.created_at, self.S1.created_at)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
