#!/usr/bin/python3
from models.base_model import BaseModel
from models import amenity
from models.amenity import Amenity
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class Amenity"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(amenity.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(Amenity.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_amenity = Amenity()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_amenity, Amenity)
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_attributes(self):
        """Test attributes of Amenity"""
        self.assertTrue(hasattr(self.new_amenity, 'name'))
        self.assertIsInstance(self.new_amenity.name, str)
