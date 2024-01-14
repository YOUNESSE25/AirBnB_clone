#!/usr/bin/python3
""" test Place class """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace(unittest.TestCase):
    """ test Place class """

    def test_inst(self):
        Type = type(Place())
        self.assertEqual(Place, Type) 

    def test_created_at(self):
        Type = type(Place().created_at)
        self.assertEqual(datetime,Type)

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))
    
    def test_unique_ids(self):
        Model1 = Place()
        Model2 = Place()
        self.assertNotEqual(Model1.id, Model2.id)

    def test_created_at(self):
        Model1 = Place()
        sleep(0.1)
        Model2 = Place()
        self.assertLess(Model1.created_at, Model2.created_at)

    def test_updated_at(self):
        Model1 = Place()
        sleep(0.1)
        Model2 = Place()
        self.assertLess(Model1.updated_at, Model2.updated_at)

    def test_save(self):
        Model = Place()
        sleep(0.1)
        up_at = Model.updated_at
        Model.save()
        self.assertLess(up_at, Model.updated_at)

    def test_to_dict_type(self):
        Type = type(Place().to_dict())
        self.assertTrue(dict, Type)

    def test_to_dict(self):
        Model = Place()
        m_dict = Model.to_dict()
        self.assertEqual(str, type(m_dict["id"]))
        self.assertEqual(str, type(m_dict["created_at"]))
        self.assertEqual(str, type(m_dict["updated_at"]))

if __name__ == "__main__":
    unittest.main()