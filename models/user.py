#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """User class inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            # No keyword arguments provided, handle this case specifically
            super().__init__()  # Call BaseModel's __init__ without arguments
            self.email = ''
            self.password = ''
            self.first_name = ''
            self.last_name = ''

        else:
            # Keyword arguments are present, proceed as in snippet 2
            super().__init__(*args, **kwargs)
            self.email = kwargs.get('email', '')
            self.password = kwargs.get('password', '')
            self.first_name = kwargs.get('first_name', '')
            self.last_name = kwargs.get('last_name', '')