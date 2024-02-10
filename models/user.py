#!/usr/bin/python3
"""
Module models/user.py: Defines the User class,
representing users in the system.

This module implements the User class, which inherits
from the BaseModel class to provide
basic functionalities for data persistence
and management. The User class stores information
such as email, password, first name, and last name.

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user within the system.

    This class inherits from the BaseModel class,
    providing functionality for data
    persistence and management. It defines the
    following attributes:

    - email: string - The user's email address (default: "").
    - password: string - The user's password (default: "").
    - first_name: string - The user's first name (default: "").
    - last_name: string - The user's last name (default: "").

    You can create User instances with or without
    providing values for these attributes.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
