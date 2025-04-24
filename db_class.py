from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    modified_date = Column(DateTime, default=datetime.now)

class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    job = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, default=False)

    user = relationship("User", backref="jobs")