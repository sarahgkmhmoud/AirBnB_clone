#!/usr/bin/python3
"""Represent City"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Public attribution on city class"""
    name = ""
    state_id = ""
