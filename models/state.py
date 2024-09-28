#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
   
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """FileStorage relationship between State and City"""
            city =[]
            all_cities = storage.all(City)
            for i in all_cities.values():
                if self.id == i.state_id:
                    city.append(i)
            return city
