#!/usr/bin/python3
"""Test suite to test the State class"""

import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
import os


class TestStateConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the State class"""

    @classmethod
    def setUp(cls):
        cls.S1 = State()
        dictionary = cls.S1.to_dict()
        cls.S2 = State(**dictionary)
        cls.dictionary2 = cls.S2.to_dict()
        cls.S3 = State()
        cls.S3.name = 'Egypt'
        cls.S3.id = 20
        cls.dictionary3 = {
            '__class__': State,
            'name': 'Palastine'
        }
        cls.S4 = State(**cls.dictionary3)
        cls.dictionary4 = cls.S4.to_dict()
        cls.S5 = State(**cls.dictionary3)

    def test_initialize_state_regular(self):
        self.assertIs(type(self.S1.id), str)
        self.assertIs(type(self.S1.created_at), datetime)
        self.assertIs(type(self.S1.updated_at), datetime)

    def test_equality_created_new_state_instances(self):
        self.assertIsNot(self.S1, self.S2)
        self.assertEqual(self.S2.updated_at, self.S1.updated_at)
        self.assertEqual(self.S2.created_at, self.S1.created_at)
        self.assertEqual(self.S2.id, self.S1.id)

    def test_equality_created_from_state_dictionary(self):
        self.assertEqual(self.S4.name, self.S5.name)

    def test_equality_created_directly(self):
        self.assertEqual(self.S3.name, 'Egypt')
        self.assertEqual(self.S3.id, 20)


class TestStateKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.S1 = State()
        cls.dictionary3 = {
            '__class__': State, 'name': 'Palastine'
        }
        cls.S2 = State(**cls.dictionary3)

    def test_kwargs_not_exist(self):
        self.assertNotIn('__class__', self.S1.__dict__)
        self.assertNotIn('name', self.S1.__dict__)
        self.assertIn('id', self.S1.__dict__)
        self.assertIn('created_at', self.S1.__dict__)
        self.assertIn('updated_at', self.S1.__dict__)

    def test_kwargs_exist(self):
        self.assertNotIn('__class__', self.S2.__dict__)
        self.assertIn('name', self.S2.__dict__)
        self.assertNotIn('id', self.S2.__dict__)
        self.assertNotIn('created_at', self.S2.__dict__)
        self.assertNotIn('updated_at', self.S2.__dict__)


class TestStateStrMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.S1 = State()
        cls.dictionary3 = {
            '__class__': State, 'name': 'Egypt', 'id': '20'
        }
        cls.S5 = State(**cls.dictionary3)

    def test_str_method(self):
        s = f"[{self.S1.__class__.__name__}] ({self.S1.id}) {self.S1.__dict__}"
        self.assertEqual(str(self.S1), s)
        s2 = f"[{self.S5.__class__.__name__}] (20) {self.S5.__dict__}"
        self.assertEqual(str(self.S5), s2)


class TestStateSaveMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.S3 = State()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_regular(self):
        old_updated_at = self.S3.updated_at
        self.S3.name = 'Palstine'
        self.S3.save()
        self.assertNotEqual(self.S3.created_at, self.S3.updated_at)
        self.assertNotEqual(old_updated_at, self.S3.updated_at)


class TestStateEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        S6 = State()
        S7 = State()
        self.assertNotEqual(S6, S7)

    def test_inequality_between_different_instances(self):
        dictionary5 = {
            '__class__': State, 'name': 'Egypt'
        }

        S8 = State(**dictionary5)
        S9 = State(**dictionary5)

        self.assertNotEqual(S8, S9)


class TestStateSerialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.S10 = State()
        cls.S10_dict = cls.S10.to_dict()

    def test_serialization_to_dict(self):
        self.assertIsInstance(self.S10_dict, dict)

    def test_format_date_time(self):
        self.assertIs(type(self.S10_dict['created_at']), str)
        self.assertIs(type(self.S10_dict['updated_at']), str)


class TestStateDeserialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.S1 = State()
        dictionary = cls.S1.to_dict()
        cls.S2 = State(**dictionary)

    def test_deserialization_to_dict(self):
        self.assertIsNot(self.S1, self.S2)

    def test_check_type_deserialization(self):
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
    """Calling the unit test"""
    unittest.main()
