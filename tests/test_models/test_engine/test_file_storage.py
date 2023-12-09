#!/usr/bin/python3
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import uuid
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):
    """Tests for the class FileStorage"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(file_storage.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(FileStorage.__doc__), 1)

    def test_method_documentation(self):
        """Methods have documentation"""
        self.assertGreater(len(FileStorage.all.__doc__), 1)

    def test_initialization(self):
        """Test the initialization of FileStorage"""
        storage1 = FileStorage()
        self.assertIsInstance(storage1, FileStorage)
        self.assertTrue(storage1._FileStorage__file_path, "file.json")
        self.assertIsInstance(storage1._FileStorage__objects, dict)

    def test_all(self):
        """Test the method all of FileStorage"""
        storage1 = FileStorage()
        storage1_all = storage1.all()
        self.assertIsInstance(storage1_all, dict)

    def test_new(self):
        """Test method new that sets obj in __objects"""
        storage1 = FileStorage()
        model1 = BaseModel()

        storage1.new(model1)
        self.assertIn(f"BaseModel.{model1.id}", storage1._FileStorage__objects)

    def test_save(self):
        """Test method save that serializes __objects to the JSON file"""
        storage1 = FileStorage()
        model2 = BaseModel()

        storage1.save()
        self.assertIn(f"BaseModel.{model2.id}", storage1._FileStorage__objects)

    @patch("datetime.datetime")
    @patch('uuid.uuid4')
    def test_str_(self, mock_uuid, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 12, 8, 8, 53, 38)
        mock_uuid.return_value = "Mock_ID"
