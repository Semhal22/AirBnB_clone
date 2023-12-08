#!/usr/bin/python3
"""Class BaseModel defines all commom attributes/methods for other classess"""
from datetime import datetime
import uuid


class BaseModel:
    """A parent class for other classes
    Attributes:
        id: unique id
        created_at: current datetime when an instance is created
        updated_at: datetime when instance is updated
    Methods:
        save: updates the updated_at
        to_dict: returns the dictionary containing all keys/values
            plus __class__, with class name of the object
    """
    def __init__(self):
        """Initialize with id, and datetime instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Define the way it is printed"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        plus __class__, class name of the object"""
        dictionary = {}
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return dictionary
