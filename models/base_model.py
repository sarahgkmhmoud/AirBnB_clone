#!/usr/bin/python3
"""A module defines Base class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """this defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize the object"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for k, v in kwargs.items():
                if 'name' in kwargs:
                    self.name = kwargs['name']
                if 'my_number' in kwargs:
                    self.my_number = kwargs['my_number']
                if (k == "created_at" or k == "updated_at"):
                    setattr(self, k,
                            datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif (k != "__class__"):
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        instance_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            if (k == 'created_at' or k == 'updated_at'):
                instance_dict[k] = v.isoformat()
            else:
                instance_dict[k] = v

        return instance_dict

    def __str__(self):
        """returns the object data"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
