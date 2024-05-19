#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from os import path

class FileStorage:
    """Serializes and deserializes instances to/from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City

                classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City}
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name in classes:
                        FileStorage.__objects[key] = classes[class_name](**value)

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects."""
        self.reload()
