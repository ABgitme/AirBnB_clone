#!/usr/bin/python3
"""

Module containing the Amenity class, which represents
amenities in a system.

This module defines the Amenity class,
which inherits from the BaseModel class to
provide basic functionalities for data
persistence and management. An Amenity
instance represents a specific amenity
offered by a service or establishment.

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity.

    Public class attributes:
    - name: string (empty string by default)
    """

    name = ""
