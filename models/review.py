#!/usr/bin/python3
"""Module for class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class representing a review"""
    place_id = ""
    user_id = ""
    text = ""
