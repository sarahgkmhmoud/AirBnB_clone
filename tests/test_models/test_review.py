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


class TestReviewConstructorAverageCase(unittest.TestCase):
    """This class tests the methods under the Review class"""

    @classmethod
    def setUp(self):
        """setup method"""
        self.R1 = Review()
        self.P1 = Place()
        self.U1 = User()
        dictionary = self.R1.to_dict()
        self.R2 = Review(**dictionary)
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

    def test_initialize_review_regular(self):
        """test initialization"""
        self.assertIs(type(self.R1.id), str)
        self.assertIs(type(self.R1.created_at), datetime)
        self.assertIs(type(self.R1.updated_at), datetime)

    def test_equality_created_new_review_instances(self):
        """test_equality_created_new_review_instances"""
        self.assertIsNot(self.R1, self.R2)
        self.assertEqual(self.R2.updated_at, self.R1.updated_at)
        self.assertEqual(self.R2.created_at, self.R1.created_at)
        self.assertEqual(self.R2.id, self.R1.id)

    def test_equality_created_from_review_dictionary(self):
        """test_equality_created_from_review_dictionary"""
        self.assertEqual(self.R4.text, self.R5.text)

    def test_equality_created_directly(self):
        """test_equality_created_directly"""
        self.assertEqual(self.R3.text, 'Nice')
        self.assertEqual(self.R3.id, 20)
        self.assertEqual(self.R3.place_id, self.P1.id)
        self.assertEqual(self.R3.user_id, self.U1.id)


class TestReviewKwargsValidation(unittest.TestCase):
    """test kwargs"""
    @classmethod
    def setUp(self):
        """setup method"""
        self.R1 = Review()
        self.dictionary3 = {
            '__class__': Review, 'text': 'Bad'
        }
        self.R2 = Review(**self.dictionary3)

    def test_kwargs_not_exist(self):
        """test kwargs"""
        self.assertNotIn('__class__', self.R1.__dict__)
        self.assertNotIn('text', self.R1.__dict__)
        self.assertIn('id', self.R1.__dict__)
        self.assertIn('created_at', self.R1.__dict__)
        self.assertIn('updated_at', self.R1.__dict__)

    def test_kwargs_exist(self):
        """test kwargs"""
        self.assertIn('__class__', self.R2.__dict__)
        self.assertIn('text', self.R2.__dict__)
        self.assertIn('id', self.R2.__dict__)
        self.assertIn('created_at', self.R2.__dict__)
        self.assertIn('updated_at', self.R2.__dict__)


class TestReviewStrMethod(unittest.TestCase):
    """test str method"""
    @classmethod
    def setUp(self):
        """setup method"""
        self.R1 = Review()
        self.dictionary3 = {
            '__class__': Review, 'text': 'Good', 'id': '20'
        }
        self.R5 = Review(**self.dictionary3)

    def test_str_method(self):
        """test str method"""
        s = f"[{self.R1.__class__.__name__}] ({self.R1.id}) {self.R1.__dict__}"
        self.assertEqual(str(self.R1), s)
        s2 = f"[{self.R5.__class__.__name__}] (20) {self.R5.__dict__}"
        self.assertEqual(str(self.R5), s2)


class TestReviewSaveMethod(unittest.TestCase):
    """test save method"""
    @classmethod
    def setUp(self):
        """setup method"""
        self.R3 = Review()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """tear down method"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_regular(self):
        """test save method"""
        old_updated_at = self.R3.updated_at
        self.R3.text = 'Nice'
        self.R3.save()
        self.assertNotEqual(self.R3.created_at, self.R3.updated_at)
        self.assertNotEqual(old_updated_at, self.R3.updated_at)


class TestReviewEquality(unittest.TestCase):
    """test equality"""
    def test_equality_between_equal_instances(self):
        """test equal instances"""
        R6 = Review()
        R7 = Review()
        self.assertNotEqual(R6, R7)

    def test_inequality_between_different_instances(self):
        """test different instances"""
        dictionary5 = {
            '__class__': Review, 'text': 'nice'
        }

        R8 = Review(**dictionary5)
        R9 = Review(**dictionary5)

        self.assertNotEqual(R8, R9)


class TestReviewSerialization(unittest.TestCase):
    """test serialization"""
    @classmethod
    def setUp(self):
        """setup method"""
        self.R10 = Review()
        self.R10_dict = self.R10.to_dict()

    def test_serialization_to_dict(self):
        """test ser to dict"""
        self.assertIsInstance(self.R10_dict, dict)

    def test_format_date_time(self):
        """check date time format"""
        self.assertIs(type(self.R10_dict['created_at']), str)
        self.assertIs(type(self.R10_dict['updated_at']), str)


class TestReviewDeserialization(unittest.TestCase):
    """test deserialization"""
    @classmethod
    def setUp(self):
        """setup method"""
        self.R1 = Review()
        dictionary = self.R1.to_dict()
        self.R2 = Review(**dictionary)

    def test_deserialization_to_dict(self):
        """test deser. to dict"""
        self.assertIsNot(self.R1, self.R2)

    def test_check_type_deserialization(self):
        """check type"""
        self.assertIs(type(self.R1.id), str)
        self.assertIs(type(self.R1.created_at), datetime)
        self.assertIs(type(self.R1.updated_at), datetime)
        self.assertIs(type(self.R2.id), str)
        self.assertIs(type(self.R2.created_at), datetime)
        self.assertIs(type(self.R2.updated_at), datetime)

    def test_check_value_equality(self):
        """check equality"""
        self.assertEqual(self.R2.id, self.R1.id)
        self.assertEqual(self.R2.updated_at, self.R1.updated_at)
        self.assertEqual(self.R2.created_at, self.R1.created_at)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
