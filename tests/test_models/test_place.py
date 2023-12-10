#!/usr/bin/python3
from models.base_model import BaseModel
from models import place
from models.place import Place
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class State"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(place.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(Place.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_place = Place()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_place, Place)
        self.assertIsInstance(self.new_place, BaseModel)

    def test_attributes(self):
        """Test attributes of State"""
        self.assertTrue(hasattr(self.new_place, 'name'))
        self.assertIsInstance(self.new_place.name, str)

        self.assertTrue(hasattr(self.new_place, 'city_id'))
        self.assertIsInstance(self.new_place.city_id, str)

        self.assertTrue(hasattr(self.new_place, 'user_id'))
        self.assertIsInstance(self.new_place.user_id, str)

        self.assertTrue(hasattr(self.new_place, 'description'))
        self.assertIsInstance(self.new_place.description, str)

        self.assertTrue(hasattr(self.new_place, 'number_rooms'))
        self.assertIsInstance(self.new_place.number_rooms, int)

        self.assertTrue(hasattr(self.new_place, 'number_bathrooms'))
        self.assertIsInstance(self.new_place.number_bathrooms, int)

        self.assertTrue(hasattr(self.new_place, 'max_guest'))
        self.assertIsInstance(self.new_place.max_guest, int)

        self.assertTrue(hasattr(self.new_place, 'price_by_night'))
        self.assertIsInstance(self.new_place.price_by_night, int)

        self.assertTrue(hasattr(self.new_place, 'latitude'))
        self.assertIsInstance(self.new_place.latitude, float)

        self.assertTrue(hasattr(self.new_place, 'longitude'))
        self.assertIsInstance(self.new_place.longitude, float)

        self.assertTrue(hasattr(self.new_place, 'amenity'))
        self.assertIsInstance(self.new_place.amenity, list)
