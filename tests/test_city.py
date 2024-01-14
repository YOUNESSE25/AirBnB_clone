#!/usr/bin/python3
""" City testing """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_myInst(unittest.TestCase):
    """ City testing """

    def test_no_args_instantiates(self):
        Model1 = City()
        cc = type(Model1)
        self.assertEqual(City, cc)

    def test_state_id_is_public_class_attribute(self):
        Model1 = City()
        typ = type(City.state_id)
        self.assertEqual(str, typ)

    def test_two_cities_different_created_at(self):
        Model11 = City()
        Model12 = City()
        self.assertNotEqual(Model11.id, Model12.id)


class TestCity_save(unittest.TestCase):
    """ tests save City class """

    def test_save(self):
        Model1 = City()
        sleep(0.1)
        up_at = Model1.updated_at
        Model1.save()
        self.assertLess(up_at, Model1.updated_at)

class TestCity_to_dict(unittest.TestCase):
    """ tests to_dict City class"""

    def test_type(self):
        typ = type(City().to_dict())
        self.assertTrue(dict, typ)


if __name__ == "__main__":
    unittest.main()