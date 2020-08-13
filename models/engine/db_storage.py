#!/usr/bin/python3
"""atabase manager for Airbnb clone"""

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Manage storage using JSON"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor"""

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, db),
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            db_query = self.__session.query(User,
                                            State,
                                            City,
                                            Amenity,
                                            Place,
                                            Review).all()
            db_dict = {}
            for obj in db_query:
                db_dict.update(
                    {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return db_dict
        else:
            db_query = self.__session.query(cls).all()
            db_dict = {}
            for obj in db_query:
                db_dict.update(
                    {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return db_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        current = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current)
