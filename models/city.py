#!/usr/bin/python3
"""Document Module here"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Document cls here"""
    name = ""
    state_id = ""
    def __init__(self, **kwargs ):
        super().__init__( **kwargs)

