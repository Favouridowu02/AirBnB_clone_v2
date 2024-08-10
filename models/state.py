#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage
from models import city


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "state"

    name = Column(String(128), nullable=False)
    if (storage.__class__.__name__ == 'DBStorage'):
        cities = relationship('City',  backref='state',
                              cascade='all, delete-orphan')
    elif (storage.__class__.__name__ == 'FileStorage'):
        @property
        def cities(self):
            my_list = []
            for i in storage.all('Cities'):
                if i.state_id == State.id:
                    list.append(i)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
