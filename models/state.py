#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class 
    
    Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City',  backref='state',
                              cascade='all, delete-orphan')
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            my_list = []
            for i in storage.all('Cities'):
                if i.state_id == State.id:
                    my_list.append(i)
                return my_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
