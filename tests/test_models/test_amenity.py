#!/usr/bin/python3
""" Amenity class test save """
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_save(unittest.TestCase):
    """ Amenity class test save """

    def test_save(self):
        Model1 = Amenity()
        up_at = Model1.updated_at
        Model1.save()
        self.assertLess(up_at, Model1.updated_at)


if __name__ == "__main__":
    unittest.main()
