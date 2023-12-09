#!/usr/bin/python3
"""serializes instances to a JSON file and
deserializes JSON file to instances"""
import json
import os.path


class FileStorage:
    """Saves and reloads objects to a file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
        path = FileStorage.__file_path
        json_format = {}
        for key, obj in self.__objects.items():
            json_format[key] = obj.to_dict()

        with open(path, 'w') as file:
            json.dump(json_format, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        path = FileStorage.__file_path
        if os.path.exists(path):
            with open(path, "r") as file:
                dictionary = json.load(file)
            for key, obj_dict in dictionary.items():
                class_name, id = key.split('.')
                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    model = BaseModel(**obj_dict)
                    self.new(model)
