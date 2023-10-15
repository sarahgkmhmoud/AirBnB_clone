#!/usr/bin/python3
import unittest
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from models import storage
import os

class test_Review_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Amenity class"""
    @classmethod
    def setUp(self):
        self.R1 = Review()
        self.P1 = Place()
        self.U1 = User()
        dictionary = self.R1.to_dict()
        self.R2 = Review(** dictionary)
        self.dictionary2 = self.R2.to_dict()
        self.R3 = Review()
        self.R3.text = 'Nice'
        self.R3.place_id = self.P1.id
        self.R3.user_id = self.U1.id
        self.R3.id = 20
        self.dictionary3 = {
                             '__class__': Review,
                             'text': 'Nice'
                             }
        self.R4 = Review(**self.dictionary3)
        self.dictionary4 = self.R4.to_dict()
        self.R5 = Review(**self.dictionary3)


    def test_initialize_ReviewRegular(self):
        self.assertIs(type(self.R1.id), str)
        self.assertIs(type(self.R1.created_at), datetime)
        self.assertIs(type(self.R1.updated_at), datetime)

    def test_equality_created_new_Reviewinstances(self):
        self.assertIsNot(self.R1, self.R2)
        self.assertEqual(self.R2.updated_at, self.R1.updated_at)
        self.assertEqual(self.R2.created_at, self.R1.created_at)
        self.assertEqual(self.R2.id, self.R1.id)

    def test_equality_created_from__Reviewdictionary(self):
        self.assertEqual(self.R4.text, self.R5.text)

    def test_equality_created_directly(self):
        self.assertEqual(self.R3.text, 'Nice')
        self.assertEqual(self.R3.id, 20)
        self.assertEqual(self.R3.place_id, self.P1.id)
        self.assertEqual(self.R3.user_id, self.U1.id)

class test_RevieKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
       self.R1 = Review()
       self.dictionary3 = {
        '__class__': Review, 'text': 'Bad'}
       self.R2 = Review(** self.dictionary3)

    def test_kwargsNotExist(self):
        self.assertNotIn('__class__', self.R1.__dict__)
        self.assertNotIn('text', self.R1.__dict__)
        self.assertIn('id', self.R1.__dict__)
        self.assertIn('created_at', self.R1.__dict__)
        self.assertIn('updated_at', self.R1.__dict__)


    def test_kwargsExist(self):

        self.assertNotIn('__class__', self.R2.__dict__)
        self.assertIn('text', self.R2.__dict__)
        self.assertNotIn('id', self.R2.__dict__)
        self.assertNotIn('created_at', self.R2.__dict__)
        self.assertNotIn('updated_at', self.R2.__dict__)

class test_CityStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.R1 = Review()
        self.dictionary3 = {
        '__class__': Review, 'text': 'Good', 'id': '20'}
        self.R5 = Review(**self.dictionary3)

    def test_str_method(self):
        expected_str = f"[{self.R1.__class__.__name__}] ({self.R1.id}) {self.R1.__dict__}"
        self.assertEqual(str(self.R1),expected_str)
        expected_str2 = f"[{self.R5.__class__.__name__}] (20) {self.R5.__dict__}"
        self.assertEqual(str(self.R5),expected_str2)

class test_ReviewSaveMethod(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.R3 = Review()
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
        old_updated_at = self.R3.updated_at
        self.R3.text = 'Nice'
        self.R3.save()
        self.assertNotEqual(self.R3.created_at, self.R3.updated_at)
        self.assertNotEqual(old_updated_at, self.R3.updated_at)

class test_ReviewEquality(unittest.TestCase):
    def test_equality_between_equal_instances(self):
        R6 = Review()
        R7 = Review()
        self.assertNotEqual(R6, R7)
    def test_inequality_between_different_instances(self):
        dictionary5 = {
        '__class__': Review, 'text': 'nice'}

        R8 = Review(**dictionary5)
        R9 = Review(**dictionary5)

        self.assertNotEqual(R8, R9)


class test_ReviewSerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.R10 = Review()
        self.R10_dict = self.R10.to_dict()
    def test_serialization_to_dict(self):
        self.assertIsInstance(self.R10_dict, dict)
    def test_formatDateTime(self):
        self.assertIs(type(self.R10_dict['created_at']), str)
        self.assertIs(type(self.R10_dict['updated_at']), str)


class test_ReviewDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.R1 = Review()
        dictionary = self.R1.to_dict()
        self.R2 = Review(** dictionary)

    def test_desrialization_to_dic(self):
        self.assertIsNot(self.R1, self.R2)

    def test_check_type_desrialization(self):
        self.assertIs(type(self.R1.id), str)
        self.assertIs(type(self.R1.created_at), datetime)
        self.assertIs(type(self.R1.updated_at), datetime)
        self.assertIs(type(self.R2.id), str)
        self.assertIs(type(self.R2.created_at), datetime)
        self.assertIs(type(self.R2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.R2.id, self.R1.id)
        self.assertEqual(self.R2.updated_at, self.R1.updated_at)
        self.assertEqual(self.R2.created_at, self.R1.created_at)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()