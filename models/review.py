#!/usr/bin/python3
"""Document module here"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string"""

    palce_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """Drevin from Parent"""
        super().__init__(**kwargs)
