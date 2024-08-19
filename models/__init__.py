#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
HBNB_TYPE_STORAGE = "db"

print(HBNB_TYPE_STORAGE)
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print(HBNB_TYPE_STORAGE)
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()