#!/usr/bin/python3
from models.base_model import BaseModel
from models import review
from models.review import Review
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the class Review"""
    def test_module_documentation(self):
        """Module has documentation"""
        self.assertGreater(len(review.__doc__), 1)

    def test_class_documentation(self):
        """Class has documentation"""
        self.assertGreater(len(Review.__doc__), 1)

    def setUp(self):
        """Runs before every test"""
        self.new_review = Review()

    def test_instances(self):
        """Test if the instance belogns to a parent class"""
        self.assertIsInstance(self.new_review, Review)
        self.assertIsInstance(self.new_review, BaseModel)

    def test_attributes(self):
        """Test attributes of Review"""
        self.assertTrue(hasattr(self.new_review, 'place_id'))
        self.assertIsInstance(self.new_review.place_id, str)

        self.assertTrue(hasattr(self.new_review, 'user_id'))
        self.assertIsInstance(self.new_review.user_id, str)

        self.assertTrue(hasattr(self.new_review, 'text'))
        self.assertIsInstance(self.new_review.text, str)
