#!/usr/bin/python3
"""
This module contains unit tests
for the Place class in the models module.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    This class provides unit tests for the Place class.
    """
    def test_place_attributes_default_values(self):
        """
        Tests if the attributes of a Place instance
        have their default values.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_instance(self):
        """
        Tests if an instance of Place is created successfully.
        """
        place = Place()
        self.assertIsInstance(place, Place)


if __name__ == '__main__':
    unittest.main()
