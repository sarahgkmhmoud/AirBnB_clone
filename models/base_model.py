#!/usr/bin/python3
"""A module defines Base class"""
import uuid
from datetime import datetime
from models import storage #import storage variable


class BaseModel:
    """this defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize the object"""
        if args:
            pass

        elif kwargs:
            for k, v in kwargs.items():
                if (k == "created_at" || k == "updated_at"):
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif (k != "__class__"):
                    setattr(self, k, v)
        
        else:
             storage.new(self)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save(self) #call save method

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        instance_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            if (k == 'created_at' || k == 'updated_at'):
                instance_dict[k] = v.isoformat()
            else:
                instance_dict[k] = v

        return instance_dict

    def __str__(self):
        """returns the object data"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict}"
