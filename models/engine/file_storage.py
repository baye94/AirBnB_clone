#!/usr/bin/env python3
""" Define the serialize instances to JSON file and deserializes JSON file to instance."""


from os import read
import json
from models.base_model import BaseModel

classes = {"BaseModel" : BaseModel}

class FileStorage:
    """ Representation class to Store object."""
    #path json file
    __file_path = "file.json"
    #stores all objects with key <class name>.id 
    __objects = {}

    
    def all(self, cls=None):
        """Return a dictionary of __objects."""
        return (self.__objects)

    def new(self, obj):
        #concatenation between classe name and object id
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_storage = {}

        for k, v in self.__objects.items():
            obj_storage[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            
             with open(self.__file_path, 'r', encoding="utf8") as f:
                my_dict = json.load(f)
             for k, v in my_dict.items():
                self.all()[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
                pass

