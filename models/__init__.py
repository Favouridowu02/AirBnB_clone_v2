#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
__all__ = ['State', 'Amenity', 'City', 'Place', 'User', 'Review']
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
HBNB_TYPE_STORAGE = 'fs'
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
__all__.append('storage')