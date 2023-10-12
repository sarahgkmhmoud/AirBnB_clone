#!/usr/bin/python3
"""test suit to test base_mode module"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
class test_BaseModel_initializing(unittest.TestCase):
    """this class to test the methods under the Base class"""
    def test_initialize_Regular(self):
        B1 = BaseModel()
        B1.id
        B1.name = "My First Model"
        B1.my_number = 89
        self.assertEquals(B1.name, "My First Model")
        self.assertEquals(B1.my_number, 89)

    def test_created_at(self):
        """three args"""


    # def test_twoarg_recreating(self):
    #     """two args"""
    #     pass

    # def test_unique(self):
    #     """unique id"""
    #     pass

    # def test_id_assignment_with_args(self):
    #     """if we put argument(positive, negtive, zero)"""
    #     pass

        
if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
   
