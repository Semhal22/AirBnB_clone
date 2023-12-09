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
    def __init__(self, *args, **kwargs):
        """Initialize with id, and datetime instances
            Extract from the dictionary passed or create a new one
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    new_value = datetime.fromisoformat(value)
                    setattr(self, key, new_value)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
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
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dictionary[key] = datetime.isoformat(value)
            else:
                dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
