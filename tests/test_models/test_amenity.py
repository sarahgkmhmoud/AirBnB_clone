#!/usr/bin/python3
"""Test suite to test the Amenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime
import os


class TestAmenityConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the Amenity class"""

    @classmethod
    def setUp(cls):
        cls.A1 = Amenity()
        dictionary = cls.A1.to_dict()
        cls.A2 = Amenity(**dictionary)
        cls.A3 = Amenity()
        cls.A3.name = 'WiFi'
        cls.A3.id = 20
        cls.dictionary3 = {
            '__class__': Amenity,
            'name': 'breakfast'
        }
        cls.A4 = Amenity(**cls.dictionary3)
        cls.A5 = Amenity(**cls.dictionary3)

    def test_initialize_amenity_regular(self):
        self.assertIs(type(self.A1.id), str)
        self.assertIs(type(self.A1.created_at), datetime)
        self.assertIs(type(self.A1.updated_at), datetime)

    def test_equality_created_new_amenity_instances(self):
        self.assertIsNot(self.A1, self.A2)
        self.assertEqual(self.A2.updated_at, self.A1.updated_at)
        self.assertEqual(self.A2.created_at, self.A1.created_at)
        self.assertEqual(self.A2.id, self.A1.id)

    def test_equality_created_from_amenity_dictionary(self):
        self.assertEqual(self.A4.name, self.A5.name)

    def test_equality_created_directly(self):
        self.assertEqual(self.A3.name, 'WiFi')
        self.assertEqual(self.A3.id, 20)


class TestAmenityKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.A1 = Amenity()
        cls.dictionary3 = {
            '__class__': Amenity, 'name': 'this dictionary', 'number': 98
        }
        cls.A2 = Amenity(**cls.dictionary3)

    def test_kwargs_not_exist(self):
        self.assertNotIn('__class__', self.A1.__dict__)
        self.assertNotIn('name', self.A1.__dict__)
        self.assertNotIn('number', self.A1.__dict__)
        self.assertIn('id', self.A1.__dict__)
        self.assertIn('created_at', self.A1.__dict__)
        self.assertIn('updated_at', self.A1.__dict__)

    def test_kwargs_exist(self):
        self.assertNotIn('__class__', self.A2.__dict__)
        self.assertIn('name', self.A2.__dict__)
        self.assertIn('number', self.A2.__dict__)
        self.assertNotIn('id', self.A2.__dict__)
        self.assertNotIn('created_at', self.A2.__dict__)
        self.assertNotIn('updated_at', self.A2.__dict__)


class TestAmenityStrMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.A1 = Amenity()
        cls.dictionary3 = {
            '__class__': Amenity, 'name': 'free WiFi', 'id': '20'
        }
        cls.A5 = Amenity(**cls.dictionary3)

    def test_str_method(self):
        s = f"[{self.A1.__class__.__name__}] ({self.A1.id}) {self.A1.__dict__}"
        self.assertEqual(str(self.A1), s)
        s2 = f"[{self.A5.__class__.__name__}] (20) {self.A5.__dict__}"
        self.assertEqual(str(self.A5), s2)


class TestAmenitySaveMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.A3 = Amenity()
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
        old_updated_at = self.A3.updated_at
        self.A3.name = 'Air condition'
        self.A3.save()
        self.assertNotEqual(self.A3.created_at, self.A3.updated_at)
        self.assertNotEqual(old_updated_at, self.A3.updated_at)


class TestAmenityEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        A6 = Amenity()
        A7 = Amenity()
        self.assertNotEqual(A6, A7)

    def test_inequality_between_different_instances(self):
        dictionary5 = {
            '__class__': Amenity, 'name': 'Garden'
        }

        A8 = Amenity(**dictionary5)
        A9 = Amenity(**dictionary5)

        self.assertNotEqual(A8, A9)


class TestAmenitySerialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.A10 = Amenity()
        cls.A10_dict = cls.A10.to_dict()

    def test_serialization_to_dict(self):
        self.assertIsInstance(self.A10_dict, dict)

    def test_format_date_time(self):
        self.assertIs(type(self.A10_dict['created_at']), str)
        self.assertIs(type(self.A10_dict['updated_at']), str)


class TestAmenityDeserialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.A1 = Amenity()
        dictionary = cls.A1.to_dict()
        cls.A2 = Amenity(**dictionary)

    def test_deserialization_to_dict(self):
        self.assertIsNot(self.A1, self.A2)

    def test_check_type_deserialization(self):
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
    """Calling the unit test"""
    unittest.main()
