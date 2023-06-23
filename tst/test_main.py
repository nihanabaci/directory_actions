import unittest
from io import StringIO
from contextlib import redirect_stdout

from main import process_commands


class ProcessCommandsTests(unittest.TestCase):
    def test_process_commands(self):
        commands = [
            "CREATE fruits",
            "CREATE vegetables",
            "CREATE grains",
            "CREATE fruits/apples",
            "CREATE fruits/apples/fuji",
            "LIST",
            "CREATE grains/squash",
            "MOVE grains/squash vegetables",
            "CREATE foods",
            "MOVE grains foods",
            "MOVE fruits foods",
            "MOVE vegetables foods",
            "LIST",
            "DELETE fruits/apples",
            "DELETE foods/fruits/apples",
            "LIST",
        ]

        expected_output = """\
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash
"""

        with StringIO() as output, redirect_stdout(output):
            process_commands(commands)
            output_string = output.getvalue()

        self.assertEqual(output_string, expected_output)
