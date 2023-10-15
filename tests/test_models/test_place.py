#!/usr/bin/python3
"""test suit to test base_mode module"""
import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from uuid import uuid4
from datetime import datetime
from models import storage
import os

class test_place_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Base class"""
    @classmethod
    def setUp(self):
        self.P1 = Place()
        dictionary = self.P1.to_dict()
        self.P2 = Place(** dictionary)
        self.U1 = User()
        self.C1 = City()
        self.dictionary2 = self.P2.to_dict()
        self.P3 = Place()
        self.P3.city_id = self.C1.id 
        self.P3.user_id = self.U1.id
        self.P3.name = 'House'
        self.P3.description = 'cozy'
        self.P3.number_rooms = 4
        self.P3.number_bathrooms = 2
        self.P3.max_gues = 5
        self.P3.price_by_night = 10
        self.P3.latitude = 3234.9
        self.P3.longitude = 3245.8
        self.P3.amenity_ids = [2, 4, 5, 6, 9]
        self.dictionary3 = {
                             '__class__': Place,
                             'name': 'Villa',
                             'number_rooms': 9,
                             'max_gues': 20,
                             'price_by_night': 300,
                             'latitude':3405.98890,
                             'longitude': 98080.9889,
                             'amenity_ids': [20, 30, 39]
                             }
        self.P4 = Place(**self.dictionary3)
        self.dictionary4 = self.P4.to_dict()
        self.P5 = Place(**self.dictionary3)
    def test_initialize_PlaceRegular(self):
        self.assertIs(type(self.P1.id), str)
        self.assertIs(type(self.P1.created_at), datetime)
        self.assertIs(type(self.P1.updated_at), datetime)
    
    def test_equality_created_new_Placestances(self):
        self.assertIsNot(self.P1, self.P2)
        self.assertEqual(self.P2.updated_at, self.P1.updated_at)
        self.assertEqual(self.P2.created_at, self.P1.created_at)
        self.assertEqual(self.P2.id, self.P1.id)

    def test_equality_created_from__Placedictionart(self):
        self.assertEqual(self.P4.name, self.P5.name)
        self.assertEqual(self.P4.description, self.P5.description)
        self.assertEqual(self.P4.number_rooms, self.P5.number_rooms)
        self.assertEqual(self.P4.number_bathrooms, self.P5.number_bathrooms)
        self.assertEqual(self.P4.max_gues, self.P5.max_gues)
        self.assertEqual(self.P4.price_by_night, self.P5.price_by_night)
        self.assertEqual(self.P4.latitude, self.P5.latitude)
        self.assertEqual(self.P4.longitude, self.P5.longitude)
        self.assertEqual(self.P4.amenity_ids, self.P5.amenity_ids)
 
          

    def test_equality_created_directly(self):
        self.assertEqual(self.P3.name, 'House')
        self.assertEqual(self.P3.description, 'cozy')
        self.assertEqual(self.P3.number_rooms, 4)
        self.assertEqual(self.P3.number_bathrooms,2)
        self.assertEqual(self.P3.max_gues,5)
        self.assertEqual(self.P3.price_by_night, 10)
        self.assertEqual(self.P3.latitude, 3234.9)
        self.assertEqual(self.P3.longitude, 3245.8)
        self.assertEqual(self.P3.amenity_ids,[2, 4, 5, 6, 9])

class test_PlacelKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.P1 = Place()
        dictionary = self.P1.to_dict()
        self.P2 = Place(** dictionary)   

    def test_UserkwargsNotExist(self):
        self.assertNotIn('__class__', self.P1.__dict__)
        self.assertNotIn('first_name', self.P1.__dict__)
        self.assertNotIn('last_name', self.P1.__dict__)
        self.assertIn('id', self.P1.__dict__)
        self.assertIn('created_at', self.P1.__dict__)
        self.assertIn('updated_at', self.P1.__dict__)

    def test_UserkwargsExist(self):

        self.assertNotIn('__class__', self.P2.__dict__)
        self.assertNotIn('first_name', self.P2.__dict__)
        self.assertNotIn('last_name', self.P2.__dict__)
        self.assertIn('id', self.P2.__dict__)
        self.assertIn('created_at', self.P2.__dict__)
        self.assertIn('updated_at', self.P2.__dict__)

    class test_PlacelStrMethod(unittest.TestCase):
        @classmethod
        def setUp(self):
            self.P1 = Place()
            self.dictionary3 = {
                             '__class__': Place,
                             'name': 'Villa',
                             'number_rooms': 9,
                             'max_gues': 20,
                             'price_by_night': 300,
                             'latitude':3405.98890,
                             'longitude': 98080.9889,
                             'amenity_ids': [20, 30, 39]
                             }
            self.P4 = Place(**self.dictionary3)
        def test_str_method(self):
            expected_str = f"[{self.P1.__class__.__name__}] ({self.U1.id}) {self.U1.__dict__}"
            self.assertEqual(str(self.P1),expected_str)
            expected_str2 = f"[{self.P4.__class__.__name__}] (20) {self.U4.__dict__}"
            self.assertEqual(str(self.P4),expected_str2)

class test_PlaceSaveMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.P3 = Place()
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

    def test_save_RegularUser(self):
        old_updated_at = self.P3.updated_at
        self.P3.name = 'Halaib w Shalateen'
        self.P3.save()
        self.assertNotEqual(self.P3.created_at, self.P3.updated_at)
        self.assertNotEqual(old_updated_at, self.P3.updated_at)

class test_PlaceEquality(unittest.TestCase):
    def test_equality_between_equal_Placeinstances(self):
        P6 = Place()
        P7 = Place()
        self.assertNotEqual(P6, P7)

    def test_inequality_between_different_Placeinstances(self):
        dictionary5 = {
                             '__class__': Place,
                             'name': 'Villa',
                             'number_rooms': 9,
                             'max_gues': 20,
                             'price_by_night': 300,
                             'latitude':3405.98890,
                             'longitude': 98080.9889,
                             'amenity_ids': [20, 30, 39]
                             }
        P8 = User(**dictionary5)
        P9 = User(**dictionary5)

        self.assertNotEqual(P8, P9)

class test_PlaceSerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.P10 = User()
        self.P10_dict = self.P10.to_dict() 
    def test_Placeserialization_to_dict(self):
        self.assertIsInstance(self.P10_dict, dict)
    def test_PlaceformatDateTime(self):
        self.assertIs(type(self.P10_dict['created_at']), str)
        self.assertIs(type(self.P10_dict['updated_at']), str)

class test_BaseModelDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.P1 = User()
        dictionary = self.P1.to_dict()
        self.P2 = User(** dictionary)
    
    def test_desrialization_to_dic(self):
        self.assertIsNot(self.P1, self.P2)
    
    def test_check_type_desrialization(self):
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
    """calling the unit test"""
    unittest.main() 