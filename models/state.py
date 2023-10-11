#!/usr/bin/python3
"""Document Module here"""
from models.base_model import BaseModel


class State(BaseModel):
    """Document cls here"""
    name = ""
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
