#!/usr/bin/python3
'''This is the State Model Module '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''This is the State class which inherits from Base'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
