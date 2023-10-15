#!/usr/bin/python3
"""Module decribe the ameinty of place"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Child Class"""
    name = ""

    def __init__(self, **kwargs):
        """Drevin from parent"""

        super().__init__(**kwargs)
