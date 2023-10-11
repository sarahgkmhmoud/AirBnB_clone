<<<<<<< HEAD
#!/usr/bin/python3
"""A module defines Base class"""
import uuid
from datetime import datetime


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

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
=======
#!/usr/bin/python3
>>>>>>> f840a1a3be83277a935ca46d67983b9485ee6a04
