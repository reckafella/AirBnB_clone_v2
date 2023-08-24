#!/usr/bin/python3

"""Database storage"""
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage:
    """Database storage class
    Attributes: __engine, __session
    """
    __engine = None
    __session = None

    db_user = os.getenv('HBNB_MYSQL_USER')
    db_pwd = os.getenv('HBNB_MYSQL_PWD')
    db_host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getenv('HBNB_MYSQL_DB')
    env = os.getenv('HBNB_ENV', 'none')

    def __init__(self):
        self.__db_url = 'mysql+mysqldb://{}:{}@{}/{}'\
            .format(self.db_user, self.db_pwd, self.db_host, self.db)
        self.__engine = create_engine(self.__db_url, pool_pre_ping=True)

        if self.env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of the specified objects """
        result = {}
        if cls is None:
            objs = [User, City, Place, Amenity, Review, State]
            for obj in objs:
                query = self.__session.query(obj).all()
                for item in query:
                    key = '{}.{}'.format(type(item).__name__, item.id)
                    result[key] = item
        else:
            query = self.__session.query(cls).all()
            for item in query:
                key = '{}.{}'.format(type(item).__name__, item.id)
                result[key] = item

        return (result)

    def new(self, obj):
        """Method that adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Method that commits all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method that deletes from the current database
        session obj if not None"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Method that creates all tables in the database"""

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """Method that closes the session"""
        self.__session.close()

""" Module implementing tools to connect with a MySQL database """

from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
import os


class DBStorage():
    """ Class managing data storage in a MySQL database """
    __engine = None
    __session = None

    db_user = os.getenv('HBNB_MYSQL_USER')
    db_pwd = os.getenv('HBNB_MYSQL_PWD')
    db_host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getenv('HBNB_MYSQL_DB')
    env = os.getenv('HBNB_ENV', 'none')

    def __init__(self):
        self.__db_url = 'mysql+mysqldb://{}:{}@{}/{}'\
            .format(self.db_user, self.db_pwd, self.db_host, self.db)
        self.__engine = create_engine(self.__db_url, pool_pre_ping=True)

        if self.env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of the specified objects """
        result = {}
        if cls is None:
            objs = [User, City, Place, Amenity, Review, State]
            for obj in objs:
                query = self.__session.query(obj).all()
                for item in query:
                    key = '{}.{}'.format(type(item).__name__, item.id)
                    result[key] = item
        else:
            query = self.__session.query(cls).all()
            for item in query:
                key = '{}.{}'.format(type(item).__name__, item.id)
                result[key] = item

        return (result)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not `None`
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
