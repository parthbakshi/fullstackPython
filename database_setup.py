import sys
from sqlalchemy import \
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaraunt(Base):
      """
      Restaunts db
      """
      __tablename__ = 'restaraunt'
      name = Column(String(80), nullable = False)
      id = Column(Integer, primary_key = True)

class MenuItem(Base):
      """
      Menuitems 
      """
      __tablename__ = 'menu_item'
           
      
      name = Column(String(80), nullable = False)
      id = Column(Integer, primary_key = True)
      course = Column(String(80))
      description = Column(String(80))
      price = Column(String(80))
      restaraunt_id = Column(Integer, ForeignKey('restaraunt.id'))
      restaraunt = relationship(Restaraunt)
      










##Create table 

engine = create_engine('sqlite:///restaraunts.db')

Base.metadata.create_all(engine)
