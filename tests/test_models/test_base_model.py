#!/usr/bin/python3
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
import unittest
import uuid
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Tests for the class BaseModel"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(base_model.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(BaseModel.__doc__), 1)

    def method_class_documentation(self):
        """Methods have documentation"""
        self.assertGreater(len(BaseModel.__init__.__doc__), 1)

    def setUp(self):
        """Automatically call this for each test"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_init(self):
        """Test the initialization, when no argument is passed
        and when a dictionary is passed"""
        dictionary = self.model1.to_dict()
        new_model = BaseModel(**dictionary)
        self.assertIsInstance(new_model, BaseModel)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertEqual(str(self.model1), str(new_model))

    def test_attribute_id(self):
        """Uniqueness of an object"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertIsInstance(self.model1.id, str)

        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_attribute_created_at(self):
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertTrue(hasattr(self.model1, 'updated_at'))
        self.assertIsInstance(self.model1.created_at, datetime)
        self.assertIsInstance(self.model1.updated_at, datetime)

    @patch("datetime.datetime")
    @patch('uuid.uuid4')
    def test_str_(self, mock_uuid, mock_datetime):
        # Set the `now()` method to return a fixed datetime
        mock_datetime.now.return_value = datetime(2023, 12, 8, 8, 53, 38)
        # Set the `uuid4()` method to return a fixed UUID
        mock_uuid.return_value = "Mock_ID"

        model3 = BaseModel()
        model3.name = "Third Model"
        model3.number = 89
        self.assertEqual(model3.id, "Mock_ID")

        expected = f"[BaseModel] ({model3.id}) {model3.__dict__}"
        self.assertEqual(str(model3), expected)

    @patch("datetime.datetime")
    @patch('uuid.uuid4')
    def test_to_dict(self, mock_uuid, mock_datetime):
        """Test to_dict method of BaseModel"""
        mock_datetime.now.return_value = datetime(2023, 12, 8, 8, 53, 38)
        mock_uuid.return_value = "Mock_ID"
        model4 = BaseModel()
        dictionary = model4.to_dict()
        self.assertEqual(dictionary, {'__class__': 'BaseModel', 'updated_at':
                                      datetime.isoformat(model4.updated_at),
                                      'id': 'Mock_ID', 'created_at':
                                      datetime.isoformat(model4.created_at)})

    def test_save(self):
        """Test if save updates the updated_at attribute"""
        time_initial = self.model1.updated_at
        self.assertEqual(time_initial, self.model1.updated_at)

        self.model1.save()
        time_updated = self.model1.updated_at
        self.assertIsInstance(time_updated, datetime)
        self.assertNotEqual(time_initial, time_updated)
