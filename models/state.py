#!/usr/bin/python3
"""Represent State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Aspecific attribution"""
    name = ""

    def __init__(self, **kwargs):
        """Drevin from Base"""
        super().__init__(**kwargs)
