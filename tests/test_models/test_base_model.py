import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
import os

class TestBaseModel(unittest.TestCase):
    #Basemodel test cases
    def test_id_generation(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertEqual(len(instance.id), 36)  # UUID length

    def test_created_at_assignment(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_assignment(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_update_on_save(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_str_representation(self):
        instance = BaseModel()
        expected_str = f"[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_to_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], instance.__class__.__name__)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)
    #Create BaseModel from dictionary
    def test_init_with_kwargs(self):
        instance_dict = {
            'id': '4f5b5b38-2c50-4495-b54a-69de54a5c54a',
            '__class__': 'BaseModel',
            'created_at': '2023-11-21T15:38:41.546758',
            'updated_at': '2023-11-22T08:15:22.354642',
            'name': 'Test Model',  # Additional attribute for testing
        }
        instance = BaseModel(**instance_dict)

        self.assertEqual(instance.id, instance_dict['id'])
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.name, instance_dict['name'])

    def test_init_without_kwargs(self):
        instance = BaseModel()

        self.assertIsInstance(instance.id, str)
        self.assertEqual(len(instance.id), 36)  # UUID length
        self.assertIsInstance(instance.created_at, datetime)
        self.assertNotEqual(instance.updated_at, instance.created_at)

class TestFileStorage(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        # Rename file.json to tmp if it exists
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDownClass(cls):
        # Remove file.json if it exists
        if os.path.exists("file.json"):
            os.remove("file.json")

        # Rename tmp to file.json if tmp exists
        if os.path.exists("tmp"):
            os.rename("tmp", "file.json")

    def setUp(self):
        self.bm = BaseModel()

    def test_one_save(self):
        first_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertLess(first_updated_at, self.bm.updated_at)

    def test_two_saves(self):
        first_updated_at = self.bm.updated_at
        self.bm.save()
        second_updated_at = self.bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.bm.save()
        self.assertLess(second_updated_at, self.bm.updated_at)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.bm.save(None)

    def test_save_updates_file(self):
        self.bm.save()
        bmid = "BaseModel." + self.bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == '__main__':
    unittest.main()
