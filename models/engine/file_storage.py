#!/usr/bin/python3
"""
Serializing and deserializing
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
import os


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_dict_objs = FileStorage.__objects

        dict_objs = {}

        for obj in all_dict_objs.keys():
            dict_objs[obj] = all_dict_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict_objs, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dict_objs = json.load(file)

                    for key, value in dict_objs.items():
                        cls_name, obj_id = key.split('.')

                        cls = eval(cls_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
