#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Set up a test file path
        self.test_file = "file.json"
        # Set the file path of FileStorage to the test file path
        storage.__file_path = self.test_file

    def tearDown(self):
        # Check if the test file exists before attempting to remove it
        if os.path.exists(self.test_file):
            # Remove the test file after each test
            os.remove(self.test_file)

    def test_all(self):
        # Test the 'all' method of FileStorage
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        # Test the 'new' method of FileStorage
        model = BaseModel()
        storage.new(model)
        all_objects = storage.all()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", all_objects)

    def test_save_reload(self):
        # Test the 'save' and 'reload' methods of FileStorage
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        storage.new(model)
        storage.save()
        # Reload objects from the file
        storage.reload()
        all_objects = storage.all()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", all_objects)

    def test_file_contents(self):
        # Test if the file contents match the expected format
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        storage.new(model)
        storage.save()

        with open(self.test_file, "r") as f:
            file_contents = json.load(f)
            self.assertIn(f"{model.__class__.__name__}.{model.id}", file_contents)
            self.assertEqual(file_contents[f"{model.__class__.__name__}.{model.id}"]["name"], "Test Model")
            self.assertEqual(file_contents[f"{model.__class__.__name__}.{model.id}"]["my_number"], 42)

if __name__ == '__main__':
    unittest.main()

