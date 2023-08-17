#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            """return a list of city instances with state_id = current"""
            all_instances = models.storage.all(City).values()
            query = []
            for ciudad in all_instances:
                if ciudad.state_id == self.id:
                    query.append(ciudad)
            return query
