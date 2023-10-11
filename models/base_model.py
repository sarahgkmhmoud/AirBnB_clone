#!/usr/bin/python3
"""A module defines Base class"""
import uuid
from datetime import datetime
from models import storage #import storage variable


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the object data"""
        return f"[{class name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save(self) #call save method

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        pass

    def __init__(self, *args, **kwargs):
            """Don't forget the documentation"""
            if args:
                 pass
            elif kwargs: 
                 pass
            else:
                storage.new(self) #call new method in case of if it’s a new instance (not from a dictionary representation)

