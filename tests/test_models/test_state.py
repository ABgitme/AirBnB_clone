#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_state_attributes_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)

if __name__ == '__main__':
    unittest.main()
