#!/usr/bin/python3
"""Represent the NewUser"""
from models.base_model import BaseModel


class User(BaseModel):
    """A specific attribution"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
