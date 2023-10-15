#!/usr/bin/python3
"""Test suite to test base_mode module"""

import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from datetime import datetime
import os


class TestPlaceConstructorAverageCase(unittest.TestCase):
    """This class is used to test the methods under the Place class"""

    @classmethod
    def setUp(cls):
        cls.P1 = Place()
        dictionary = cls.P1.to_dict()
        cls.P2 = Place(**dictionary)
        cls.U1 = User()
        cls.C1 = City()
        cls.dictionary2 = cls.P2.to_dict()
        cls.P3 = Place()
        cls.P3.city_id = cls.C1.id
        cls.P3.user_id = cls.U1.id
        cls.P3.name = 'House'
        cls.P3.description = 'cozy'
        cls.P3.number_rooms = 4
        cls.P3.number_bathrooms = 2
        cls.P3.max_guests = 5
        cls.P3.price_by_night = 10
        cls.P3.latitude = 3234.9
        cls.P3.longitude = 3245.8
        cls.P3.amenity_ids = [2, 4, 5, 6, 9]
        cls.dictionary3 = {
            '__class__': Place,
            'name': 'Villa',
            'number_rooms': 9,
            'max_guests': 20,
            'price_by_night': 300,
            'latitude': 3405.98890,
            'longitude': 98080.9889,
            'amenity_ids': [20, 30, 39]
        }
        cls.P4 = Place(**cls.dictionary3)
        cls.dictionary4 = cls.P4.to_dict()
        cls.P5 = Place(**cls.dictionary3)

    def test_initialize_place_regular(self):
        """Test if Place is initialized with the correct types"""
        self.assertIs(type(self.P1.id), str)
        self.assertIs(type(self.P1.created_at), datetime)
        self.assertIs(type(self.P1.updated_at), datetime)

    def test_equality_created_new_place_instances(self):
        """Test equality between newly created instances"""
        self.assertIsNot(self.P1, self.P2)
        self.assertEqual(self.P2.updated_at, self.P1.updated_at)
        self.assertEqual(self.P2.created_at, self.P1.created_at)
        self.assertEqual(self.P2.id, self.P1.id)

    def test_equality_created_from_place_dictionary(self):
        """Test equality between instances created from dictionaries"""
        self.assertEqual(self.P4.name, self.P5.name)
        self.assertEqual(self.P4.description, self.P5.description)
        self.assertEqual(self.P4.number_rooms, self.P5.number_rooms)
        self.assertEqual(self.P4.number_bathrooms, self.P5.number_bathrooms)
        self.assertEqual(self.P4.max_guests, self.P5.max_guests)
        self.assertEqual(self.P4.price_by_night, self.P5.price_by_night)
        self.assertEqual(self.P4.latitude, self.P5.latitude)
        self.assertEqual(self.P4.longitude, self.P5.longitude)
        self.assertEqual(self.P4.amenity_ids, self.P5.amenity_ids)

    def test_equality_created_directly(self):
        """Test equality for instances created directly"""
        self.assertEqual(self.P3.name, 'House')
        self.assertEqual(self.P3.description, 'cozy')
        self.assertEqual(self.P3.number_rooms, 4)
        self.assertEqual(self.P3.number_bathrooms, 2)
        self.assertEqual(self.P3.max_guests, 5)
        self.assertEqual(self.P3.price_by_night, 10)
        self.assertEqual(self.P3.latitude, 3234.9)
        self.assertEqual(self.P3.longitude, 3245.8)
        self.assertEqual(self.P3.amenity_ids, [2, 4, 5, 6, 9])


class TestPlaceKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.P1 = Place()
        dictionary = cls.P1.to_dict()
        cls.P2 = Place(**dictionary)

    def test_place_kwargs_not_exist(self):
        """Test if attributes not present in kwargs are set"""
        self.assertNotIn('__class__', self.P1.__dict__)
        self.assertNotIn('name', self.P1.__dict__)
        self.assertIn('id', self.P1.__dict__)
        self.assertIn('created_at', self.P1.__dict__)
        self.assertIn('updated_at', self.P1.__dict__)

    def test_place_kwargs_exist(self):
        """Test if attributes in kwargs are set"""
        self.assertNotIn('__class__', self.P2.__dict__)
        self.assertNotIn('name', self.P2.__dict__)
        self.assertIn('id', self.P2.__dict__)
        self.assertIn('created_at', self.P2.__dict__)
        self.assertIn('updated_at', self.P2.__dict__)


class TestPlaceStrMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.P1 = Place()
        cls.dictionary3 = {
            '__class__': Place,
            'name': 'Villa',
            'number_rooms': 9,
            'max_guests': 20,
            'price_by_night': 300,
            'latitude': 3405.98890,
            'longitude': 98080.9889,
            'amenity_ids': [20, 30, 39],
            'id': '20'
        }
        cls.P4 = Place(**cls.dictionary3)

    def test_place_str_method(self):
        s = f"[{self.P1.__class__.__name__}] ({self.P1.id}) {self.P1.__dict__}"
        self.assertEqual(str(self.P1), s)
        s2 = f"[{self.P4.__class__.__name__}] (20) {self.P4.__dict__}"
        self.assertEqual(str(self.P4), s2)


class TestPlaceSaveMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.P3 = Place()
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

    def test_place_save_regular_user(self):
        old_updated_at = self.P3.updated_at
        self.P3.name = 'Halaib w Shalateen'
        self.P3.save()
        self.assertNotEqual(self.P3.created_at, self.P3.updated_at)
        self.assertNotEqual(old_updated_at, self.P3.updated_at)


class TestPlaceEquality(unittest.TestCase):
    def test_equality_between_equal_place_instances(self):
        P6 = Place()
        P7 = Place()
        self.assertNotEqual(P6, P7)

    def test_inequality_between_different_place_instances(self):
        dictionary5 = {
            '__class__': Place,
            'name': 'Villa',
            'number_rooms': 9,
            'max_guests': 20,
            'price_by_night': 300,
            'latitude': 3405.98890,
            'longitude': 98080.9889,
            'amenity_ids': [20, 30, 39]
        }
        P8 = User(**dictionary5)
        P9 = User(**dictionary5)

        self.assertNotEqual(P8, P9)


class TestPlaceSerialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.P10 = User()
        cls.P10_dict = cls.P10.to_dict()

    def test_place_serialization_to_dict(self):
        self.assertIsInstance(self.P10_dict, dict)

    def test_place_format_date_time(self):
        self.assertIs(type(self.P10_dict['created_at']), str)
        self.assertIs(type(self.P10_dict['updated_at']), str)


class TestBaseModelDeserialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.P1 = User()
        dictionary = cls.P1.to_dict()
        cls.P2 = User(**dictionary)

    def test_deserialization_to_dict(self):
        self.assertIsNot(self.P1, self.P2)

    def test_check_type_deserialization(self):
        self.assertIs(type(self.P1.id), str)
        self.assertIs(type(self.P1.created_at), datetime)
        self.assertIs(type(self.P1.updated_at), datetime)
        self.assertIs(type(self.P2.id), str)
        self.assertIs(type(self.P2.created_at), datetime)
        self.assertIs(type(self.P2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.P2.id, self.P1.id)
        self.assertEqual(self.P2.updated_at, self.P1.updated_at)
        self.assertEqual(self.P2.created_at, self.P1.created_at)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
