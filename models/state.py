#!/usr/bin/python3
"""
Module containing the State class for
representing states within a system.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a State.

    Public class attributes:
    - name: string (empty string by default)
    """

    name = ""
