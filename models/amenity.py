#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        """ Amenity: Class"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                    viewonly=False)
