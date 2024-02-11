#!/usr/bin/python3
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
