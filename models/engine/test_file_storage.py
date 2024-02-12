#!/usr/bin/python3
"""
This module contains unit tests for
the FileStorage class in the models module.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Unittests for testing save method of the BaseModel class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment by renaming
        the file.json to tmp if it exists.
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDownClass(cls):
        """
        Cleans up the test environment by removing file.json
        if it exists and renaming tmp to file.json if tmp exists.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

        # Rename tmp to file.json if tmp exists
        if os.path.exists("tmp"):
            os.rename("tmp", "file.json")

    def setUp(self):
        """
        Sets up the individual test case by creating
        an instance of the BaseModel class.
        """
        self.bm = BaseModel()

    def test_one_save(self):
        """
        Tests if the save method successfully
        updates the updated_at attribute.
        """
        first_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertLess(first_updated_at, self.bm.updated_at)

    def test_two_saves(self):
        """
        Tests if multiple calls to the save method
        correctly update the updated_at attribute.
        """
        first_updated_at = self.bm.updated_at
        self.bm.save()
        second_updated_at = self.bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.bm.save()
        self.assertLess(second_updated_at, self.bm.updated_at)

    def test_save_with_arg(self):
        """
        Tests if the save method raises
        a TypeError when passed an argument.
        """
        with self.assertRaises(TypeError):
            self.bm.save(None)

    def test_save_updates_file(self):
        """
        Tests if the save method updates the file.json
        with the correct information.
        """
        self.bm.save()
        bmid = "BaseModel." + self.bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_all(self):
        """
        Tests the 'all' method of FileStorage.
        """
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """
        Tests the 'new' method of FileStorage.
        """
        model = BaseModel()
        storage.new(model)
        all_objects = storage.all()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", all_objects)

    def test_save_reload(self):
        """
        Test the 'save' and 'reload' methods of FileStorage
        """
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
        """
        Test if the file contents match the expected format
        """
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        storage.new(model)
        storage.save()

        with open(self.test_file, "r") as f:
            file_contents = json.load(f)
            self.assertIn(
                f"{model.__class__.__name__}.{model.id}", file_contents
            )
            self.assertEqual(
                file_contents[
                    f"{model.__class__.__name__}.{model.id}"
                ]["name"], "Test Model"
            )
            self.assertEqual(
                file_contents[
                    f"{model.__class__.__name__}.{model.id}"
                    ]["my_number"], 42
            )


if __name__ == '__main__':
    unittest.main()
