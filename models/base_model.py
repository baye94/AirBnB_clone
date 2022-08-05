#!/usr/bin/env python3
""" Defines all common attributes/methodes for other class. """

import uuid
import time
from datetime import date
from datetime import datetime, timezone
import models


class BaseModel:
    " Represent the base class."""

    def __init__(self, *args, **kwargs):
        """ Init alise Base class."""      
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            self.__set_attribute(kwargs)
        else:
            models.storage.new(self)

    def __str__(self):
        txt = "[" + self.__class__.__name__ +"] "
        txt += "(" + str(self.id) +") " + str(self.__dict__)

        return(txt)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        dic['created_at'] = datetime.isoformat(self.created_at)
        return (dic)

    def __set_attribute(self, attr):
        """ set each key of this dictionary like an attribute.
            each value of this dictionary is the value of this attribute name.
        
        Args:
            attr(dictionary): is the dictionary of attribute.
        
        """
        dt_form = "%Y-%m-%dT%H:%M:%S.%f"
        for k,v in attr.items():
            if k == 'created_at' or k == 'updated_at':
                self.__dict__[k] = datetime.strptime(v, dt_form)
            elif k == '__class__':
                pass
            else:
                self.__dict__[k] = v
