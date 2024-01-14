#!/usr/bin/python3
"""state State class"""
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestState(unittest.TestCase):
    """state State class"""

    def test_Type(self):
        Type =  type(State())
        self.assertEqual(State, Type)

    def test_id(self):
        Type = type(State().id)
        self.assertEqual(str, Type)

    def test_created_at(self):
        Type = type(State().created_at)
        self.assertEqual(datetime, Type)

    def test_updated_at(self):
        Type = type(State().updated_at)
        self.assertEqual(datetime, Type)

    def test_ids(self):
        Model1 = State()
        Model2 = State()
        self.assertNotEqual(Model1.id, Model2.id)

    def test_created_at_s(self):
        Model1 = State()
        sleep(0.1)
        Model2 = State()
        self.assertLess(Model1.created_at, Model2.created_at)

    def test_updated_at_s(self):
        Model1 = State()
        sleep(0.1)
        Model2 = State()
        self.assertLess(Model1.updated_at, Model2.updated_at)

    def test_save(self):
        Model = State()
        sleep(0.1)
        first_updated_at = Model.updated_at
        Model.save()
        self.assertLess(first_updated_at, Model.updated_at)

    def test_to_dict(self):
        Type = type(State().to_dict())
        self.assertTrue(dict, Type)


if __name__ == "__main__":
    unittest.main()

