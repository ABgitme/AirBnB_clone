#!/usr/bin/python3
"""
Module containing test cases for the User model.
"""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Tests for the User class, covering attribute values,
    instance creation, and dictionary representation.
    """
    def test_user_attributes_default_values(self):
        """
        Verifies that User attributes are
        initialized with correct default values.
        """
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")

    def test_user_attributes_assigned_values(self):
        """
        Tests that User attributes can be
        assigned and saved correctly.
        """
        my_user = User(
            email="airbnb@mail.com", password="password123",
            first_name="John", last_name="Dear"
        )
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
        """
        Ensures the User's to_dict method produces
        the expected dictionary representation.
        """
        my_user = User(
            email="airbnb@mail.com", password="password123",
            first_name="John", last_name="Dear"
        )
        my_dict = my_user.to_dict()
        self.assertEqual(my_dict['first_name'], "John")
        self.assertEqual(my_dict['last_name'], "Dear")
        self.assertEqual(my_dict['email'], "airbnb@mail.com")
        self.assertEqual(my_dict['password'], "password123")

    def test_user_instance(self):
        """
        Confirms that the User class can be instantiated successfully.
        """
        user = User()
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
