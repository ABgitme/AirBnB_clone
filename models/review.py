#!/usr/bin/python3
"""
Module defining the Review class,
representing reviews associated with places.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review.

    Public class attributes:
    - place_id: string (empty string by default, corresponds to Place.id)
    - user_id: string (empty string by default, corresponds to User.id)
    - text: string (empty string by default)
    """

    place_id = ""
    user_id = ""
    text = ""
