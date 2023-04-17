#!/usr/bin/env python3

# we don't need to import everything from sqlalchemy below but we can import all of these things...

# you will create_engine, Column, Integer
from sqlalchemy import (create_engine, Column, Integer, String)
# these two down here you will always need
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Student id={self.id} name={self.name}>"

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Teacher id={self.id} name={self.name}>"
