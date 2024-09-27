#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = (String(128), nullable=False)
    
    cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        from models import storage
        from models.city import City
        """FileStorage relationship between State and City"""
        city =[]
        all_cities = storage.all(City)
        for i in all_cities.values():
            if self.id == city.state_id:
                city.append(i)
        return city
