import datetime

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tweet(Base):
    __tablename__  = 'tweet'
    id             = Column(Integer, primary_key=True)
    text           = Column(String(140))
    picture_url    = Column(String(140))
    created_at     = Column(DateTime, default=datetime.datetime.now())
    show_location  = Column(Boolean, default=True)
    location       = Column(String(30))
    favorite_count = Column(Integer, default=0)
