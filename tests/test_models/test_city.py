#!/usr/bin/python3
from models.base_model import BaseModel
from models import city
from models.city import City
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class City"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(city.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(City.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_city = City()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_city, City)
        self.assertIsInstance(self.new_city, BaseModel)

    def test_attributes(self):
        """Test attributes of City"""
        self.assertTrue(hasattr(self.new_city, 'name'))
        self.assertIsInstance(self.new_city.name, str)

        self.assertTrue(hasattr(self.new_city, 'state_id'))
        self.assertIsInstance(self.new_city.state_id, str)
