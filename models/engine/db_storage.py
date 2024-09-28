#!/usr/bin/python3
"""DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}')
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query database"""
        from models.user import User
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        obj = {}
        classes = [User, City, State, Review, Amenity, Place]
        if not cls:
            for i in classes:
                query = self.__session.query(i).all()
                for j in query:
                    obj[f'{j.__class__.__name__}.{j.id}'] = j
        else:
            query = self.__session.query(cls).all()
            for j in query:
                obj[f'{j.__class__.__name__].{j.id}'] = j
        return obj

    def new(self, obj):
        """new instance"""
        self.__session.add(obj)

    def save(self):
        """save instance"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete instance"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
