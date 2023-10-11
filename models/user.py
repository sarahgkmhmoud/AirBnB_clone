#!/usr/bin/python3
"""Document Module here"""
from models.base_model import BaseModel
class User(BaseModel):
    """Document cls here"""
    email = ""
    password = ""
    first_name = ""
    last_name = "" 
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
