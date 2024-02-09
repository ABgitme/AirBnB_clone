#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            # Handle initialization from a dictionary
            for key, value in kwargs.items():
                if key != "__class__":  # Exclude the __class__ attribute
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)  # Convert string to datetime
                    setattr(self, key, value)
        else:
            # Handle creation of a new instance
            self.id = str(uuid.uuid4())  # Generate a unique UUID for the ID
            self.created_at = datetime.now()  # Set the creation timestamp
            self.updated_at = datetime.now()  # Set the initial update timestamp

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dict_repr = self.__dict__.copy()
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        dict_repr["__class__"] = self.__class__.__name__
        return dict_repr