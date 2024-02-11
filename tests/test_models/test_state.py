#!/usr/bin/python3
"""
This module contains unit tests
for the State class in the models module.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    A test case for the State class.
    """
    def test_state_attributes_default_values(self):
        """
        Test if default values are set for state attributes.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_state_instance(self):
        """
        Test if an instance of State is created successfully.
        """
        state = State()
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
