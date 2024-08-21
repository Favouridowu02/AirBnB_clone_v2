#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """
        This is the Amenities Class

        Attributes:
            name: The is the name of the amenities
            place_amenities: This is the place amenities attribute.
    """
    __tablename__="amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity, viewonly=False)