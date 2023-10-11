#!/usr/bin/python3
"""Document module here"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Document class here"""
    name = ""
    def __init__(self, **kwargs):
        super().__init__( **kwargs)

