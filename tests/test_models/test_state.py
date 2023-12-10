#!/usr/bin/python3
from models.base_model import BaseModel
from models import state
from models.state import State
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class State"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(state.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(State.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_state = State()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_state, State)
        self.assertIsInstance(self.new_state, BaseModel)

    def test_attributes(self):
        """Test attributes of State"""
        self.assertTrue(hasattr(self.new_state, 'name'))
        self.assertIsInstance(self.new_state.name, str)
