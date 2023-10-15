#!/usr/bin/python3
"""Test suite to test the base_model module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModelConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the Base class"""

    @classmethod
    def setUp(cls):
        """setup method for test class"""
        cls.B1 = BaseModel()
        dictionary = cls.B1.to_dict()
        cls.B2 = BaseModel(**dictionary)
        cls.dictionary2 = cls.B2.to_dict()
        cls.B3 = BaseModel()
        cls.B3.name = 'assign directly'
        cls.B3.my_number = 90
        cls.B3.id = 20
        cls.dictionary3 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}
        cls.B4 = BaseModel(**cls.dictionary3)
        cls.dictionary4 = cls.B4.to_dict()
        cls.B5 = BaseModel(**cls.dictionary3)

    def test_initialize_regular(self):
        """Test if BaseModel is initialized with the correct types"""
        self.assertIs(type(self.B1.id), str)
        self.assertIs(type(self.B1.created_at), datetime)
        self.assertIs(type(self.B1.updated_at), datetime)

    def test_equality_created_new_instances(self):
        """Test equality between newly created instances"""
        self.assertIsNot(self.B1, self.B2)
        self.assertEqual(self.B2.updated_at, self.B1.updated_at)
        self.assertEqual(self.B2.created_at, self.B1.created_at)
        self.assertEqual(self.B2.id, self.B1.id)

    def test_equality_created_from_dictionary(self):
        """Test equality between instances created from dictionaries"""
        self.assertEqual(self.B4.name, self.B5.name)
        self.assertEqual(self.B4.number, self.B5.number)

    def test_equality_created_directly(self):
        """Test equality for instances created directly"""
        self.assertEqual(self.B3.name, 'assign directly')
        self.assertEqual(self.B3.my_number, 90)
        self.assertEqual(self.B3.id, 20)


class TestBaseModelKwargsValidation(unittest.TestCase):
    """test kwargs"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.B1 = BaseModel()
        cls.dictionary3 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}
        cls.B2 = BaseModel(**cls.dictionary3)

    def test_kwargs_not_exist(self):
        """Test if attributes not present in kwargs are set"""
        self.assertNotIn('__class__', self.B1.__dict__)
        self.assertNotIn('name', self.B1.__dict__)
        self.assertNotIn('number', self.B1.__dict__)
        self.assertIn('id', self.B1.__dict__)
        self.assertIn('created_at', self.B1.__dict__)
        self.assertIn('updated_at', self.B1.__dict__)

    def test_kwargs_exist(self):
        """Test if attributes in kwargs are set"""
        self.assertNotIn('__class__', self.B2.__dict__)
        self.assertIn('name', self.B2.__dict__)
        self.assertIn('number', self.B2.__dict__)
        self.assertNotIn('id', self.B2.__dict__)
        self.assertNotIn('created_at', self.B2.__dict__)
        self.assertNotIn('updated_at', self.B2.__dict__)


class TestBaseModelStrMethod(unittest.TestCase):
    """test str method"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.B1 = BaseModel()
        cls.dictionary3 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98,
            'id': '20'}
        cls.B5 = BaseModel(**cls.dictionary3)

    def test_str_method(self):
        """set str method"""
        s = f"[{self.B1.__class__.__name__}] ({self.B1.id}) {self.B1.__dict__}"
        self.assertEqual(str(self.B1), s)
        s2 = f"[{self.B5.__class__.__name__}] (20) {self.B5.__dict__}"
        self.assertEqual(str(self.B5), s2)


class TestBaseModelSaveMethod(unittest.TestCase):
    """test save method"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.B3 = BaseModel()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """tear down method"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_regular(self):
        """test save regular"""
        old_updated_at = self.B3.updated_at
        self.B3.name = 'second module'
        self.B3.save()
        self.assertNotEqual(self.B3.created_at, self.B3.updated_at)
        self.assertNotEqual(old_updated_at, self.B3.updated_at)


class TestBaseModelEquality(unittest.TestCase):
    """test equality"""
    def test_equality_between_equal_instances(self):
        """test equal instances"""
        B6 = BaseModel()
        B7 = BaseModel()
        self.assertNotEqual(B6, B7)

    def test_inequality_between_different_instances(self):
        """test differenet instances"""
        dictionary5 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}

        B8 = BaseModel(**dictionary5)
        B9 = BaseModel(**dictionary5)

        self.assertNotEqual(B8, B9)


class TestBaseModelSerialization(unittest.TestCase):
    """test serialization"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.B10 = BaseModel()
        cls.B10_dict = cls.B10.to_dict()

    def test_serialization_to_dict(self):
        """test ser to dict"""
        self.assertIsInstance(self.B10_dict, dict)

    def test_format_datetime(self):
        """test date time format"""
        self.assertIs(type(self.B10_dict['created_at']), str)
        self.assertIs(type(self.B10_dict['updated_at']), str)


class TestBaseModelDeserialization(unittest.TestCase):
    """test deserialization"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.B1 = BaseModel()
        dictionary = cls.B1.to_dict()
        cls.B2 = BaseModel(**dictionary)

    def test_desrialization_to_dict(self):
        """test deserialization to dict"""
        self.assertIsNot(self.B1, self.B2)

    def test_check_type_desrialization(self):
        """check type """
        self.assertIs(type(self.B1.id), str)
        self.assertIs(type(self.B1.created_at), datetime)
        self.assertIs(type(self.B1.updated_at), datetime)
        self.assertIs(type(self.B2.id), str)
        self.assertIs(type(self.B2.created_at), datetime)
        self.assertIs(type(self.B2.updated_at), datetime)

    def test_check_value_equality(self):
        """check value equality"""
        self.assertEqual(self.B2.id, self.B1.id)
        self.assertEqual(self.B2.updated_at, self.B1.updated_at)
        self.assertEqual(self.B2.created_at, self.B1.created_at)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
