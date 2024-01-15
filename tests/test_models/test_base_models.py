#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Module for BaseModel unittest"""

    def test_init(self):
        """ init test """
        Model1 = BaseModel()

        self.assertIsNotNone(Model1.id)
        self.assertIsNotNone(Model1.created_at)
        self.assertIsNotNone(Model1.updated_at)

    def test_save(self):
        """ save test """
        Model1 = BaseModel()
        up_at1 = Model1.updated_at
        last_up_at = Model1.save()
        self.assertNotEqual(up_at1, last_up_at)

    def test_to_dict(self):
        """ to_dict test """
        Model1 = BaseModel()
        Model1_dict = Model1.to_dict()
        self.assertIsInstance(Model1_dict, dict)
        self.assertEqual(Model1_dict["__class__"], 'BaseModel')
        self.assertEqual(Model1_dict['id'], Model1.id)
        self.assertEqual(Model1_dict['created_at'], M.created_at.isoformat())
        self.assertEqual(Model1_dict["updated_at"], M.created_at.isoformat())

    def test_str(self):
        """ Test for string representation """
        Model1 = BaseModel()
        test = str(Model1).startswith('[BaseModel]')
        self.assertTrue(test)
        self.assertIn(Model1.id, str(Model1))
        self.assertIn(str(Model1.__dict__), str(Model1))


if __name__ == "__main__":
    unittest.main()
