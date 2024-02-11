#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a Place.

    Public class attributes:
    - city_id: string (empty string by default, corresponds to City.id)
    - user_id: string (empty string by default, corresponds to User.id)
    - name: string (empty string by default)
    - description: string (empty string by default)
    - number_rooms: integer (0 by default)
    - number_bathrooms: integer (0 by default)
    - max_guest: integer (0 by default)
    - price_by_night: integer (0 by default)
    - latitude: float (0.0 by default)
    - longitude: float (0.0 by default)
    - amenity_ids: list of strings (empty list by default, corresponds to Amenity.id)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []