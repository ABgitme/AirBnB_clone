#!/usr/bin/python3
"""
This module contains unit tests
for the Review class in the models module.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    A test case for the Review class.
    """
    def test_review_attributes_default_values(self):
        """
        Test if default values are set for review attributes.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_instance(self):
        """
        Test if an instance of Review is created successfully.
        """
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == '__main__':
    unittest.main()
