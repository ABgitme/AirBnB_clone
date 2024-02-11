#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a State.

    Public class attributes:
    - name: string (empty string by default)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
