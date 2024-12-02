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
    
    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "username": self.username,
            "password": self.password
        }

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

    fave_characters_id = Column(Integer, ForeignKey('favorite_characters.id'))
    fave_planets_id = Column(Integer, ForeignKey('favorite_planets.id'))
    fave_vehicles_id = Column(Integer, ForeignKey('favorite_vehicles.id'))
    
    def serialize(self):
        return {
            "fave_characters_id": self.fave_characters_id,
            "fave_planets_id": self.fave_planets_id,
            "fave_vehicles_id": self.fave_vehicles_id
        }
    

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250), ForeignKey('characters.name'))
    fave_id = Column(Integer, ForeignKey('characters.character_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250),  ForeignKey('planets.name'))
    fave_id = Column(Integer, ForeignKey('planets.planet_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)

    fave_name = Column(String(250), ForeignKey('vehicles.name'))
    fave_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    
    def serialize(self):
        return {
            "fave_name": self.fave_name,
            "fave_id": self.fave_id
        }

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    
    character_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(250), unique=True, nullable=False)
    birth_year = Column(String(250), unique=False, nullable=False)
    gender = Column(String(250), unique=False, nullable=False)
    height = Column(Integer, unique=False, nullable=False)
    mass = Column(Integer, unique=False, nullable=False)
    skin_color = Column(String(250), unique=False, nullable=False)
    hair_color = Column(String(250), unique=False, nullable=False)
    eye_color = Column(String(250), unique=False, nullable=True)
    films = Column(String(250), unique=False, nullable=True)
    homeworld = Column(String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "character_id": self.character_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "films": self.films,
            "homeworld": self.homeworld
        }
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    
    planet_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(250), unique=True, nullable=False)
    population = Column(Integer, unique=False, nullable=False)
    residents = Column(String(250), unique=False, nullable=False)
    terrain = Column(String(250), unique=False, nullable=False)
    climate = Column(String(250), unique=False, nullable=False)
    surface_water = Column(Integer, unique=False, nullable=False)
    diameter = Column(Integer, unique=False, nullable=False)
    gravity = Column(Integer, unique=False, nullable=False)
    orbital_period = Column(Integer, unique=False, nullable=False)
    rotational_period = Column(Integer, unique=False, nullable=False)
    films = Column(String(250), unique=False, nullable=True)
    url = Column(String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "planet_id": self.planet_id,
            "name": self.name,
            "population": self.population,
            "residents": self.residents,
            "terrain": self.terrain,
            "climate": self.climate,
            "surface_water": self.surface_water,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "rotational_period": self.rotational_period,
            "films": self.films,
            "url": self.url
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    
    vehicle_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(250), unique=True, nullable=False)
    vehicle_class = Column(String(250), unique=False, nullable=False)
    manufacturer = Column(String(250), unique=False, nullable=False)
    model = Column(String(250), unique=False, nullable=False)
    cost_in_credits = Column(Integer, unique=False, nullable=False)
    crew = Column(Integer, unique=False, nullable=False)
    pilots = Column(String(250), unique=False, nullable=False)  # Figure out how to make this an array type...
    passengers = Column(Integer, unique=False, nullable=False)
    length = Column(Integer, unique=False, nullable=False)
    cargo_capacity = Column(Integer, unique=False, nullable=False)
    consumables = Column(String(250), unique=False, nullable=False)
    max_atmosphering_speed = Column(Integer, unique=False, nullable=False)
    films = Column(String(250), unique=False, nullable=True)
    url = Column(String(250), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "vehicle_id": self.vehicle_id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "pilots": self.pilots,
            "passengers": self.passengers,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "films": self.films,
            "url": self.url
        }
    
    
    
    
    
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
