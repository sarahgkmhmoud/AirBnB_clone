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


