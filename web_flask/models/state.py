#!/usr/bin/python3
"""This module defines the State class."""

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class for storing state information"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def cities(self):
        """Returns the list of City objects linked to the current State"""
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
