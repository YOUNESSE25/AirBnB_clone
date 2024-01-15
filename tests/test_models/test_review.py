#!/usr/bin/python3
""" test Review class """
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """ test Review class """

    def test_Type(self):
        Type = type(Review())
        self.assertEqual(Review, Type)

    def test_Type_id(self):
        Type = type(Review().id)
        self.assertEqual(str, Type)

    def test_Type_created_at(self):
        Type = type(Review().created_at)
        self.assertEqual(datetime, Type)

    def test_Type_updated_at(self):
        Type = type(Review().updated_at)
        self.assertEqual(datetime, Type)

    def test_ids(self):
        Model1 = Review()
        Model2 = Review()
        self.assertNotEqual(Model1.id, Model2.id)

    def test_save(self):
        revw = Review()
        sleep(0.1)
        up_at = revw.updated_at
        revw.save()
        self.assertLess(up_at, revw.updated_at)

    def test_to_dict(self):
        revw = Review()
        r_dict = revw.to_dict()
        self.assertEqual(str, type(r_dict["id"]))
        self.assertEqual(str, type(r_dict["created_at"]))
        self.assertEqual(str, type(r_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
