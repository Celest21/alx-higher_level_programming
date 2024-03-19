#!/usr/bin/python3
""" Module to define the State class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """ Class representing states table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, name):
        """ Initializes a state instance """
        self.name = name

