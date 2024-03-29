#!/usr/bin/python3
"""
FilStorage test
"""
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_testing(unittest.TestCase):
    """FilStorage test"""
    def test_FileStorage_instantiation_no_args(self):
        Type = type(FileStorage())
        self.assertEqual(Type, FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        Type = type(FileStorage._FileStorage__file_path)
        self.assertEqual(Type, str)

    def testFileStorage_objects_is_private_dict(self):
        Type = type(FileStorage._FileStorage__objects)
        self.assertEqual(Type, dict)


if __name__ == "__main__":
    unittest.main()
