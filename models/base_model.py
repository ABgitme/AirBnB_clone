#!/usr/bin/python3
"""
Base model class for data persistence and management.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance with a unique ID,
        timestamps, and optional attributes.
        """
        self.id = str(uuid.uuid4())  # Generate a unique UUID for the ID
        self.created_at = datetime.now()  # Set the creation timestamp
        self.updated_at = datetime.now()  # Set the initial

        if kwargs:
            # Handle initialization from a dictionary
            for key, value in kwargs.items():
                if key != "__class__":  # Exclude the __class__ attribute
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        """
        Updates the updated_at timestamp and
        saves the instance to storage.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        dict_repr["__class__"] = self.__class__.__name__
        return dict_repr
