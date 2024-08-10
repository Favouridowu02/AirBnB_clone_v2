#!/usr/bin/python3
"""
    This Module contains the DB storage
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

user = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')
dialect = 'mysql'
driver = 'mysqldb'


class DBStorage:
    """
        This is the Database Storage CLass

        Attributes:
            user: the user
            password: the password
            host: the host
            db: the database
            dialect: the dialect
            driver: the driver
    """
    __engine = None
    __session = None


    def __init__(self):
        """
            This is the initialization of the DBstorage
        """
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}"
                                 .format(dialect, driver, user, password, host, db),
                                 pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)


        
    def all(self, cls=None):
        """
            Query on the current database session all objects
            depending of the class name argumnets.

            Attributes:
                cls: the class 
                if cls=None: User, State, City, Amenity, Place and Review.
        """
        from models.amenity import Amenity
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
    
        if cls == None:
            obj = self.__session.query(User).all()
            obj.extend(self.__session.query(State).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
        else:
            cls = eval(cls)
            obj = self.__session.query("{}".format(cls)).all()
        

        return {"{}.{}".format(i.__class__.__name__, i.id): i for i in obj}
    
    def new(self, obj):
        """
            This function adds an object to the current database session

            Argument:
                obj: the object to be added
        """
        self.__session.add(obj)

    def save(self):
        """
            This function commits all the changes of the database session

            Argument:
                None
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            This function delete and object from the current session

            Argument:
                obj: the object to be removed

            if obj is None: nothing is removed
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            Create all tables in the database and the  current databbase session
            from the engine.
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()