#!/usr/bin/python3
"""test suit to test base_mode module"""
import unittest
from models.user import User
from uuid import uuid4
from datetime import datetime
from models import storage
import os

class test_User_Constructor_averageCase(unittest.TestCase):
    """this class to test the methods under the Base class"""
    @classmethod
    def setUp(self):
        self.U1 = User()
        dictionary = self.U1.to_dict()
        self.U2 = User(** dictionary)
        self.dictionary2 = self.U2.to_dict()
        self.U3 = User()
        self.U3.email = "manar@gmail.com"
        self.U3.first_name = 'Manar'
        self.U3.last_name = 'Elsaid'
        self.U3.password = '123'
        self.U3.id = 20
        self.dictionary3 = {
                             '__class__': User,
                             'first_name': 'Sarah',
                             'last_name': 'Gad',
                             'email': 'sarah@gmail.com',
                             'password': '345' 
                             }
        self.U4 = User(**self.dictionary3)
        self.dictionary4 = self.U4.to_dict()
        self.U5 = User(**self.dictionary3)
    def test_initialize_userRegular(self):
        self.assertIs(type(self.U1.id), str)
        self.assertIs(type(self.U1.created_at), datetime)
        self.assertIs(type(self.U1.updated_at), datetime)
    
    def test_equality_created_new_Userinstances(self):
        self.assertIsNot(self.U1, self.U2)
        self.assertEqual(self.U2.updated_at, self.U1.updated_at)
        self.assertEqual(self.U2.created_at, self.U1.created_at)
        self.assertEqual(self.U2.id, self.U1.id)

    def test_equality_created_from__Userdictionart(self):
        self.assertEqual(self.U4.first_name, self.U5.first_name)
        self.assertEqual(self.U4.last_name, self.U5.last_name)
        self.assertEqual(self.U4.email, self.U5.email)
        self.assertEqual(self.U4.password, self.U5.password)
     

    def test_equality_created_directly(self):
        self.assertEqual(self.U3.first_name, 'Manar')
        self.assertEqual(self.U3.last_name, 'Elsaid')
        self.assertEqual(self.U3.id, 20 )
        self.assertEqual(self.U3.email,'manar@gmail.com')
        self.assertEqual(self.U3.password,'123')

class test_UserlKwargsValidation(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.U1 = User()
        dictionary = self.U1.to_dict()
        self.U2 = User(** dictionary)
    
    def test_UserkwargsNotExist(self):
        self.assertNotIn('__class__', self.U1.__dict__)
        self.assertNotIn('first_name', self.U1.__dict__)
        self.assertNotIn('last_name', self.U1.__dict__)
        self.assertIn('id', self.U1.__dict__)
        self.assertIn('created_at', self.U1.__dict__)
        self.assertIn('updated_at', self.U1.__dict__)
    

    def test_UserkwargsExist(self):

        self.assertNotIn('__class__', self.U2.__dict__)
        self.assertNotIn('first_name', self.U2.__dict__)
        self.assertNotIn('last_name', self.U2.__dict__)
        self.assertIn('id', self.U2.__dict__)
        self.assertIn('created_at', self.U2.__dict__)
        self.assertIn('updated_at', self.U2.__dict__)

class test_UserlStrMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.U1 = User()
        self.dictionary3 = {
                             '__class__': User,
                             'first_name': 'Sarah',
                             'last_name': 'Gad',
                             'email': 'sarah@gmail.com',
                             'password': '345',
                             'id': '20'
                             }
        self.U4 = User(**self.dictionary3)
    def test_str_method(self):
        expected_str = f"[{self.U1.__class__.__name__}] ({self.U1.id}) {self.U1.__dict__}"
        self.assertEqual(str(self.U1),expected_str)
        expected_str2 = f"[{self.U4.__class__.__name__}] (20) {self.U4.__dict__}"
        self.assertEqual(str(self.U4),expected_str2)

class test_UserSaveMethod(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.U3 = User()
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
        old_updated_at = self.U3.updated_at
        self.U3.first_name = 'Madiha'
        self.U3.save()
        self.assertNotEqual(self.U3.created_at, self.U3.updated_at)
        self.assertNotEqual(old_updated_at, self.U3.updated_at)

class test_UserEquality(unittest.TestCase):
    def test_equality_between_equal_Userinstances(self):
        U6 = User()
        U7 = User()
        self.assertNotEqual(U6, U7)
    def test_inequality_between_different_Userinstances(self):
        dictionary5 = {
        '__class__': User, 'first_name': 'Sarah', 'last_name': 'Gad'}

        U8 = User(**dictionary5)
        U9 = User(**dictionary5)

        self.assertNotEqual(U8, U9)

class test_UserSerialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.U10 = User()
        self.U10_dict = self.U10.to_dict() 
    def test_Userserialization_to_dict(self):
        self.assertIsInstance(self.U10_dict, dict)
    def test_UserformatDateTime(self):
        self.assertIs(type(self.U10_dict['created_at']), str)
        self.assertIs(type(self.U10_dict['updated_at']), str)


class test_BaseModelDeserialization(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.U1 = User()
        dictionary = self.U1.to_dict()
        self.U2 = User(** dictionary)
    
    def test_desrialization_to_dic(self):
        self.assertIsNot(self.U1, self.U2)
    
    def test_check_type_desrialization(self):
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
    """calling the unit test"""
    unittest.main() 