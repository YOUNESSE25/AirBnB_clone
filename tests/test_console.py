#!/usr/bin/python3
"""
tests for console
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand_testing(unittest.TestCase):
    """tests for console"""

    def test_prompt_string(self):
        h = HBNBCommand.prompt
        self.assertEqual("(hbnb) ", h)


if __name__ == "__main__":
    unittest.main()
