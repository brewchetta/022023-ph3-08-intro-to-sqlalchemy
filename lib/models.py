#!/usr/bin/env python3

# we don't need to import everything from sqlalchemy below but we can import all of these things...
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Student id={self.id} name={self.name}>"
