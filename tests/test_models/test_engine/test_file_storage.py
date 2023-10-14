#!/usr/bin/python3
"""Update models/__init__.py: to create a unique FileStorage instance for your application"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import json
import os

class test_instantation(unittest.TestCase):
    """Don't Forget the command"""
    def test_with_None_argument(self):
        """Don't forget the doc"""
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def test_without_argument(self):

        self.assertIsInstance(FileStorage(), FileStorage)
    def test_Attribution_type(self):
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_Attribution_value(self):
        self.assertEqual(storage._FileStorage__file_path, "file.json")

class test_allMethod(unittest.TestCase):
    """Don't forget the document"""
       
    def test_with_None_argumentAll(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_AllMethod(self):
        self.assertEqual(type(storage.all()),dict)

    def test_allMethodwithNew(self):
        B = BaseModel()
        NewUser = User()
        NewState = State()
        NewCity = City()
        NewPlace = Place()
        NewAmenity = Amenity()
        NewReview = Review()
        dictionay = storage.all()
        self.assertIn("BaseModel." + B.id, dictionay.keys())
        self.assertIn(B, dictionay.values())
        self.assertIn("User." + NewUser.id, dictionay.keys())
        self.assertIn(NewUser, dictionay.values())
        self.assertIn("State." + NewState.id, dictionay.keys())
        self.assertIn(NewState, dictionay.values())
        self.assertIn("City." + NewCity.id, dictionay.keys())
        self.assertIn(NewCity, dictionay.values())
        self.assertIn("Place." + NewPlace.id, dictionay.keys())
        self.assertIn(NewPlace, dictionay.values())
        self.assertIn("Amenity." + NewAmenity.id, dictionay.keys())
        self.assertIn(NewAmenity, dictionay.values())
        self.assertIn("Review." + NewReview.id, dictionay.keys())
        self.assertIn(NewReview, dictionay.values())

class test_saveMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
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
        
    def test_savemethod(self):
        B = BaseModel()
        B.save()
        NewUser = User()
        NewUser.save()
        NewState = State()
        NewState.save()
        NewCity = City()
        NewCity.save()
        NewPlace = Place()
        NewPlace.save()
        NewAmenity = Amenity()
        NewAmenity.save()
        NewReview = Review()
        NewReview.save()
        save_text = ""

        with open ("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + B.id, save_text)
            self.assertIn("User." + NewUser.id, save_text)
            self.assertIn("State." + NewState.id, save_text)
            self.assertIn("City." + NewCity.id, save_text)
            self.assertIn("Place." + NewPlace.id, save_text)
            self.assertIn("Amenity." + NewAmenity.id, save_text)
            self.assertIn("Review." + NewReview.id, save_text)

    def test_Reloadmethod(self):

        B = BaseModel()
        NewUser = User()
        NewState = State()
        NewCity = City()
        NewPlace = Place()
        NewAmenity = Amenity()
        NewReview = Review()
        storage.save()
        storage.reload()
        objs = storage._FileStorage__objects
        self.assertIn("BaseModel." + B.id, objs)
        self.assertIn("User." + NewUser.id, objs)
        self.assertIn("State." + NewState.id, objs)
        self.assertIn("City." + NewCity.id, objs)
        self.assertIn("Place." + NewPlace.id, objs)
        self.assertIn("Amenity." + NewAmenity.id, objs)
        self.assertIn("Review." + NewReview.id, objs)

    def test_checkRaises(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            storage.new(None)
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.reload(None)
 
if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
   