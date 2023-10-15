#!/usr/bin/python3
"""Represent City"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Public attribution on city class"""
    name = ""
    state_id = ""

    def __init__(self, **kwargs):
        """Drevin from Parent"""
        super().__init__(**kwargs)
