#!/usr/bin/python3
"""
This module contains unit tests for
the City class in the models.city module.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    This class provides unit tests for the City class.
    """
    def test_city_attributes_default_values(self):
        """
        Tests if the attributes of a City instance
        have the default values upon instantiation.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_instance(self):
        """
        Tests if an instance of the City
        class is created successfully.
        """
        city = City()
        self.assertIsInstance(city, City)


if __name__ == '__main__':
    unittest.main()
