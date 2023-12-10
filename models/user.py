#!/usr/bin/python3
"""Class User inhertis from BaseModel"""
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """Inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
