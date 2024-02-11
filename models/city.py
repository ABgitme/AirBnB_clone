#!/usr/bin/python3
"""
Module containing the City class, representing cities within a system.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City.

    Public class attributes:
    - state_id: string (empty string by default, corresponds to State.id)
    - name: string (empty string by default)
    """

    state_id = ""
    name = ""
