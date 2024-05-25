from .base import BASE
from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime


class Notes(BASE):
    __tablename__ = 'notes'


    id = Column(Integer, primary_key=True)
    heading = Column(String)
    text = Column(Text)
    date = Column(DateTime, default=datetime.now())


    def __init__(self, heading, text):
        self.heading = heading
        self.text = text

    def __str__(self):
        return f'Note {self.heading}'