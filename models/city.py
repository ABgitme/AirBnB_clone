#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a City.

    Public class attributes:
    - state_id: string (empty string by default, corresponds to State.id)
    - name: string (empty string by default)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
