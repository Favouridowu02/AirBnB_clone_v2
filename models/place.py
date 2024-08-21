#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from os import getenv
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews= relationship('Review', backref='place', cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    else:
        
        @property
        def reviews(self):
            """
                A getter Attribute that returns the list of Review instances with
                place_id equals to the current Place.id

                Argument:
                    None

                Return: a list of Review intances with place_id equals to the current Place.id
            """
            from models import storage
            review_list = storage.all(Review)
            new_list = []

            for obj in review_list.values():
                if obj.place_id == self.id:
                    new_list.append(obj)
            return new_list
        
        @property
        def amenities(self):
            """
                A getter Attribute that returns the list of Amenity instances based on the
                attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            from models.amenity import Amenity
            from models import storage
            amenities_list = storage.all(Amenity)
            new_list = []
            for obj in amenities_list.values():
                if obj.id in self.amenity_ids:
                    new_list.append(obj)
            return new_list       

        @amenities.setter
        def amenities(self, obj):
            """
                Setter attribute amenities that handles append method for adding an Amenity.id
                to the attribute amenity_ids. This method should accept only Amenity object,
                otherwise, do nothing.
            """
            from models.amenity import Amenity
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
