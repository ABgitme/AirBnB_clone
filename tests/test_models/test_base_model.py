#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel
and FileStorage classes in the models package.
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    # Basemodel test cases
    def test_id_generation(self):
        """
        Tests if the id attribute of a BaseModel
        instance is generated correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertEqual(len(instance.id), 36)  # UUID length

    def test_created_at_assignment(self):
        """
        Tests if the created_at attribute of a BaseModel
        instance is assigned correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_assignment(self):
        """
        Tests if the updated_at attribute of a BaseModel
        instance is assigned correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_update_on_save(self):
        """
        Tests if the updated_at attribute of a BaseModel
        instance is updated upon calling the save() method.
        """
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_str_representation(self):
        """
        Tests if the str() method of a BaseModel
        instance returns the expected string representation.
        """
        instance = BaseModel()
        expected_str = f"[{instance.__class__.__name__}](
            {instance.id}) {instance.__dict__}
        "
        self.assertEqual(str(instance), expected_str)

    def test_to_dict(self):
        """
        Tests if the to_dict() method of a BaseModel
        instance returns the expected dictionary representation.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(
            instance_dict['__class__'], instance.__class__.__name__
        )
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_init_with_kwargs(self):
        """
        Tests if a BaseModel instance can be
        initialized with keyword arguments.
        """
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
        """
        Tests if a BaseModel instance can be
        initialized without keyword arguments.
        """
        instance = BaseModel()

        self.assertIsInstance(instance.id, str)
        self.assertEqual(len(instance.id), 36)  # UUID length
        self.assertIsInstance(instance.created_at, datetime)
        self.assertNotEqual(instance.updated_at, instance.created_at)


if __name__ == '__main__':
    unittest.main()
