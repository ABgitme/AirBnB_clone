#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_attributes_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

if __name__ == '__main__':
    unittest.main()