#!/usr/bin/python3
"""
Module providing a FileStorage class for persisting
and loading BaseModel instances to/from a JSON file.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Manages storage and retrieval of BaseModel
    instances using a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all stored objects,
        keyed by their class name and ID.

        Returns:
            dict: A dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes all stored objects to a JSON file.
        """
        serialized = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """
        Loads stored objects from the JSON file, if it exists.
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            pass  # Do nothing if the file doesn't exist
