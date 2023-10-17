#!/usr/bin/python3
"""Document module here"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string"""

    def __init__(self, *args, **kwargs):
        """Document"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
