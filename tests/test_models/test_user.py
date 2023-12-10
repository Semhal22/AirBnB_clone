#!/usr/bin/python3
from models.base_model import BaseModel
from models import user
from models.user import User
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class User"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(user.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(User.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_user = User()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_user, User)
        self.assertIsInstance(self.new_user, BaseModel)

    def test_attributes(self):
        """Test attributes of User"""
        self.assertTrue(hasattr(self.new_user, 'first_name'))
        self.assertIsInstance(self.new_user.first_name, str)

        self.assertTrue(hasattr(self.new_user, 'last_name'))
        self.assertIsInstance(self.new_user.last_name, str)

        self.assertTrue(hasattr(self.new_user, 'email'))
        self.assertIsInstance(self.new_user.email, str)

        self.assertTrue(hasattr(self.new_user, 'password'))
        self.assertIsInstance(self.new_user.password, str)
