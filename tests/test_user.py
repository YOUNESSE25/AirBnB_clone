#!/usr/bin/python3
"""test User class"""

import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """test User class"""

    def test_Type(self):
        Type = type(User())
        self.assertEqual(User, Type)

    def test_Type_id_Type(self):
        Type = type(User().id)
        self.assertEqual(str, Type)

    def test_created_at_Type(self):
        Type = type(User().created_at)
        self.assertEqual(datetime, Type)

    def test_updated_at_Type(self):
        Type = type(User().updated_at)
        self.assertEqual(datetime, Type)

    def test_email_Type(self):
        Type = type(User.email)
        self.assertEqual(str, Type)

    def test_password_Type(self):
        Type = type(User.password)
        self.assertEqual(str, Type)

    def test_first_name_Type(self):
        Type = type(User.first_name)
        self.assertEqual(str, Type)

    def test_last_name_Type(self):
        Type = type(User.last_name)
        self.assertEqual(str, Type)

    def test_ids(self):
        Model1 = User()
        Model2 = User()
        self.assertNotEqual(Model1.id, Model2.id)

    def test_save(self):
        Model = User()
        sleep(0.1)
        first_updated_at = Model.updated_at
        Model.save()
        self.assertLess(first_updated_at, Model.updated_at)

    def test_to_dict_Type(self):
        Type = type(User().to_dict())
        self.assertTrue(dict, Type)


if __name__ == "__main__":
    unittest.main()
