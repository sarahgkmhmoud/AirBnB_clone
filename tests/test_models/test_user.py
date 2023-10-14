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