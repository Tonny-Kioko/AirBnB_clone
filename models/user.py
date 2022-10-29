#!/usr/bin/python3
"""Module that edits the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class representing the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
