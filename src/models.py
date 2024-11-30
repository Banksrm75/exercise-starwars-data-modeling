import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    first_name = Column(String(250), unique=False, nullable=False)
    last_name = Column(String(250), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone_number = Column(String(250), unique=False, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

    fave_characters_id = Column(Integer, ForeignKey('favorite_characters.id'))
    fave_planets_id = Column(Integer, ForeignKey('favorite_planets.id'))
    fave_vehicles_id = Column(Integer, ForeignKey('favorite_vehicles.id'))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250), ForeignKey('characters.name'))
    fave_id = Column(Integer, ForeignKey('characters.id'))

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250),  ForeignKey('planets.name'))
    fave_id = Column(Integer, ForeignKey('planets.id'))

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicless'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250), ForeignKey('vehicles.name'))
    fave_id = Column(Integer, ForeignKey('vehicles.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
