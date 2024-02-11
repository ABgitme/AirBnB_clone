#!/usr/bin/python3
"""
This module contains unit tests for the
Amenity class in the models.amenity module.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This class provides unit
    tests for the Amenity class.
    """
    def test_amenity_attributes_default_values(self):
        """
        Tests if the attributes of an Amenity instance
        have the default values upon instantiation.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance(self):
        """
        Tests if an instance of the Amenity
        class is created successfully.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
