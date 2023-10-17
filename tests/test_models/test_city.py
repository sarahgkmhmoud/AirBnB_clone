#!/usr/bin/python3
"""Test suite to test the City module"""

import unittest
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import os


class TestCityConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the City class"""

    @classmethod
    def setUp(cls):
        """setup method"""
        cls.C1 = City()
        cls.S1 = State()
        dictionary = cls.C1.to_dict()
        cls.C2 = City(**dictionary)
        cls.dictionary2 = cls.C2.to_dict()
        cls.C3 = City()
        cls.C3.name = 'Cairo'
        cls.C3.state_id = cls.S1.id
        cls.C3.id = 20
        cls.dictionary3 = {
            '__class__': City,
            'name': 'Luxor'
        }
        cls.C4 = City(**cls.dictionary3)
        cls.dictionary4 = cls.C4.to_dict()
        cls.C5 = City(**cls.dictionary3)

    def test_initialize_city_regular(self):
        """Test if City is initialized with the correct types"""
        self.assertIs(type(self.C1.id), str)
        self.assertIs(type(self.C1.created_at), datetime)
        self.assertIs(type(self.C1.updated_at), datetime)

    def test_equality_created_new_city_instances(self):
        """Test equality between newly created instances"""
        self.assertIsNot(self.C1, self.C2)
        self.assertEqual(self.C2.updated_at, self.C1.updated_at)
        self.assertEqual(self.C2.created_at, self.C1.created_at)
        self.assertEqual(self.C2.id, self.C1.id)

    def test_equality_created_from_city_dictionary(self):
        """Test equality between instances created from dictionaries"""
        self.assertEqual(self.C4.name, self.C5.name)

    def test_equality_created_directly(self):
        """Test equality for instances created directly"""
        self.assertEqual(self.C3.name, 'Cairo')
        self.assertEqual(self.C3.id, 20)
        self.assertEqual(self.C3.state_id, self.S1.id)


class TestCityKwargsValidation(unittest.TestCase):
    """testing kwargs validation"""
    @classmethod
    def setUp(cls):
        """setup method for test class"""
        cls.C1 = City()
        cls.dictionary3 = {
            '__class__': City,
            'name': 'Daraw'
        }
        cls.C2 = City(**cls.dictionary3)

    def test_kwargs_not_exist(self):
        """Test if attributes not present in kwargs are set"""
        self.assertNotIn('__class__', self.C1.__dict__)
        self.assertNotIn('name', self.C1.__dict__)
        self.assertIn('id', self.C1.__dict__)
        self.assertIn('created_at', self.C1.__dict__)
        self.assertIn('updated_at', self.C1.__dict__)

    def test_kwargs_exist(self):
        """Test if attributes in kwargs are set"""
        self.assertIn('__class__', self.C2.__dict__)
        self.assertIn('name', self.C2.__dict__)
        self.assertIn('id', self.C2.__dict__)
        self.assertIn('created_at', self.C2.__dict__)
        self.assertIn('updated_at', self.C2.__dict__)


class TestCityStrMethod(unittest.TestCase):
    """testing str method"""
    @classmethod
    def setUp(cls):
        """setup method for test class"""
        cls.C1 = City()
        cls.dictionary3 = {
            '__class__': City,
            'name': 'Qena',
            'id': '20'
        }
        cls.C5 = City(**cls.dictionary3)

    def test_str_method(self):
        """test str method"""
        s = f"[{self.C1.__class__.__name__}] ({self.C1.id}) {self.C1.__dict__}"
        self.assertEqual(str(self.C1), s)
        s2 = f"[{self.C5.__class__.__name__}] (20) {self.C5.__dict__}"
        self.assertEqual(str(self.C5), s2)


class TestCitySaveMethod(unittest.TestCase):
    """test save method"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.C3 = City()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """teardown method"""
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
        old_updated_at = self.C3.updated_at
        self.C3.name = 'Alexandria'
        self.C3.save()
        self.assertNotEqual(self.C3.created_at, self.C3.updated_at)
        self.assertNotEqual(old_updated_at, self.C3.updated_at)


class TestCityEquality(unittest.TestCase):
    """test city equality"""
    def test_equality_between_equal_instances(self):
        """equal instances"""
        C6 = City()
        C7 = City()
        self.assertNotEqual(C6, C7)

    def test_inequality_between_different_instances(self):
        """different instances"""
        dictionary5 = {
            '__class__': City,
            'name': 'Alex'
        }

        C8 = City(**dictionary5)
        C9 = City(**dictionary5)

        self.assertNotEqual(C8, C9)


class TestCitySerialization(unittest.TestCase):
    """test serialization"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.C10 = City()
        cls.C10_dict = cls.C10.to_dict()

    def test_serialization_to_dict(self):
        """serialization to dict"""
        self.assertIsInstance(self.C10_dict, dict)

    def test_format_datetime(self):
        """format date time"""
        self.assertIs(type(self.C10_dict['created_at']), str)
        self.assertIs(type(self.C10_dict['updated_at']), str)


class TestCityDeserialization(unittest.TestCase):
    """ testing deserialization"""
    @classmethod
    def setUp(cls):
        """setup method"""
        cls.C1 = City()
        dictionary = cls.C1.to_dict()
        cls.C2 = City(**dictionary)

    def test_deserialization_to_dict(self):
        """test to dict"""
        self.assertIsNot(self.C1, self.C2)

    def test_check_type_deserialization(self):
        """check type deserialization"""
        self.assertIs(type(self.C1.id), str)
        self.assertIs(type(self.C1.created_at), datetime)
        self.assertIs(type(self.C1.updated_at), datetime)
        self.assertIs(type(self.C2.id), str)
        self.assertIs(type(self.C2.created_at), datetime)
        self.assertIs(type(self.C2.updated_at), datetime)

    def test_check_value_equality(self):
        """check value equality"""
        self.assertEqual(self.C2.id, self.C1.id)
        self.assertEqual(self.C2.updated_at, self.C1.updated_at)
        self.assertEqual(self.C2.created_at, self.C1.created_at)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
