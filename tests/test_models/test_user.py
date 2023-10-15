#!/usr/bin/python3
"""Test suite to test the User class"""

import unittest
from models.user import User
from datetime import datetime
import os


class TestUserConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the User class"""

    @classmethod
    def setUp(cls):
        cls.U1 = User()
        dictionary = cls.U1.to_dict()
        cls.U2 = User(**dictionary)
        cls.U3 = User()
        cls.U3.email = "manar@gmail.com"
        cls.U3.first_name = 'Manar'
        cls.U3.last_name = 'Elsaid'
        cls.U3.password = '123'
        cls.U3.id = 20
        cls.dictionary3 = {
            '__class__': User,
            'first_name': 'Sarah',
            'last_name': 'Gad',
            'email': 'sarah@gmail.com',
            'password': '345'
        }
        cls.U4 = User(**cls.dictionary3)
        cls.U5 = User(**cls.dictionary3)

    def test_initialize_user_regular(self):
        self.assertIs(type(self.U1.id), str)
        self.assertIs(type(self.U1.created_at), datetime)
        self.assertIs(type(self.U1.updated_at), datetime)

    def test_equality_created_new_user_instances(self):
        self.assertIsNot(self.U1, self.U2)
        self.assertEqual(self.U2.updated_at, self.U1.updated_at)
        self.assertEqual(self.U2.created_at, self.U1.created_at)
        self.assertEqual(self.U2.id, self.U1.id)

    def test_equality_created_from_user_dictionary(self):
        self.assertEqual(self.U4.first_name, self.U5.first_name)
        self.assertEqual(self.U4.last_name, self.U5.last_name)
        self.assertEqual(self.U4.email, self.U5.email)
        self.assertEqual(self.U4.password, self.U5.password)

    def test_equality_created_directly(self):
        self.assertEqual(self.U3.first_name, 'Manar')
        self.assertEqual(self.U3.last_name, 'Elsaid')
        self.assertEqual(self.U3.id, 20)
        self.assertEqual(self.U3.email, 'manar@gmail.com')
        self.assertEqual(self.U3.password, '123')


class TestUserKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.U1 = User()
        dictionary = cls.U1.to_dict()
        cls.U2 = User(**dictionary)

    def test_user_kwargs_not_exist(self):
        self.assertNotIn('__class__', self.U1.__dict__)
        self.assertNotIn('first_name', self.U1.__dict__)
        self.assertNotIn('last_name', self.U1.__dict__)
        self.assertIn('id', self.U1.__dict__)
        self.assertIn('created_at', self.U1.__dict__)
        self.assertIn('updated_at', self.U1.__dict__)

    def test_user_kwargs_exist(self):
        self.assertNotIn('__class__', self.U2.__dict__)
        self.assertNotIn('first_name', self.U2.__dict__)
        self.assertNotIn('last_name', self.U2.__dict__)
        self.assertIn('id', self.U2.__dict__)
        self.assertIn('created_at', self.U2.__dict__)
        self.assertIn('updated_at', self.U2.__dict__)


class TestUserStrMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.U1 = User()
        cls.dictionary3 = {
            '__class__': User,
            'first_name': 'Sarah',
            'last_name': 'Gad',
            'email': 'sarah@gmail.com',
            'password': '345',
            'id': '20'
        }
        cls.U4 = User(**cls.dictionary3)

    def test_str_method(self):
        s = f"[{self.U1.__class__.__name__}] ({self.U1.id}) {self.U1.__dict__}"
        self.assertEqual(str(self.U1), s)
        s2 = f"[{self.U4.__class__.__name__}] (20) {self.U4.__dict__}"
        self.assertEqual(str(self.U4), s2)


class TestUserSaveMethod(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.U3 = User()
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

    def test_save_regular_user(self):
        old_updated_at = self.U3.updated_at
        self.U3.first_name = 'Madiha'
        self.U3.save()
        self.assertNotEqual(self.U3.created_at, self.U3.updated_at)
        self.assertNotEqual(old_updated_at, self.U3.updated_at)


class TestUserEquality(unittest.TestCase):
    def test_equality_between_equal_user_instances(self):
        U6 = User()
        U7 = User()
        self.assertNotEqual(U6, U7)

    def test_inequality_between_different_user_instances(self):
        dictionary5 = {
            '__class__': User,
            'first_name': 'Sarah',
            'last_name': 'Gad'
        }

        U8 = User(**dictionary5)
        U9 = User(**dictionary5)

        self.assertNotEqual(U8, U9)


class TestUserSerialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.U10 = User()
        cls.U10_dict = cls.U10.to_dict()

    def test_user_serialization_to_dict(self):
        self.assertIsInstance(self.U10_dict, dict)

    def test_user_format_date_time(self):
        self.assertIs(type(self.U10_dict['created_at']), str)
        self.assertIs(type(self.U10_dict['updated_at']), str)


class TestUserDeserialization(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.U1 = User()
        dictionary = cls.U1.to_dict()
        cls.U2 = User(**dictionary)

    def test_deserialization_to_dict(self):
        self.assertIsNot(self.U1, self.U2)

    def test_check_type_deserialization(self):
        self.assertIs(type(self.U1.id), str)
        self.assertIs(type(self.U1.created_at), datetime)
        self.assertIs(type(self.U1.updated_at), datetime)
        self.assertIs(type(self.U2.id), str)
        self.assertIs(type(self.U2.created_at), datetime)
        self.assertIs(type(self.U2.updated_at), datetime)

    def test_check_value_equality(self):
        self.assertEqual(self.U2.id, self.U1.id)
        self.assertEqual(self.U2.updated_at, self.U1.updated_at)
        self.assertEqual(self.U2.created_at, self.U1.created_at)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
