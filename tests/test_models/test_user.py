#!/usr/bin/python3
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):

    def test_user_attributes_default_values(self):
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")

    def test_user_attributes_assigned_values(self):
        my_user = User(email="airbnb@mail.com", password="password123",
                        first_name="John", last_name="Dear")
        my_user.first_name = "John"
        my_user.last_name = "Dear"
        my_user.email = "airbnb@mail.com"
        my_user.password = "password123"
        my_user.save()
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.password, "password123")
        self.assertEqual(my_user.first_name, "John")
        self.assertEqual(my_user.last_name, "Dear")

    def test_userInst_to_dict(self):
        my_user = User(email="airbnb@mail.com", password="password123",
                        first_name="John", last_name="Dear")
        my_dict = my_user.to_dict()
        self.assertEqual(my_dict['first_name'], "John")
        self.assertEqual(my_dict['last_name'], "Dear")
        self.assertEqual(my_dict['email'], "airbnb@mail.com")
        self.assertEqual(my_dict['password'], "password123")

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

if __name__ == '__main__':
    unittest.main()