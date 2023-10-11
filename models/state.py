#!/usr/bin/python3
"""Document Module here"""
from models.base_model import BaseModel


class State(BaseModel):
    """Document cls here"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
