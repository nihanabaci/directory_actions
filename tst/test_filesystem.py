import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.filesystem import FileSystem


class FileSystemTests(unittest.TestCase):
    def test_create_directory(self):
        fs = FileSystem()
        fs.create_directory("child")
        print(fs)
        self.assertIn("child", fs.root.children[0].name)

    def test_move_directory(self):
        fs = FileSystem()
        fs.create_directory("child1")
        fs.create_directory("child2")
        fs.move_directory("child1", "child2")
        self.assertIn("child1", fs.root.children[0].children[0].name)

    def test_delete_directory(self):
        fs = FileSystem()
        fs.create_directory("child1")
        fs.delete_directory("child1")
        self.assertNotIn("child1", fs.root.children)

    def test_list_directory(self):
        fs = FileSystem()
        fs.create_directory("child1")
        fs.create_directory("child2")
        fs.create_directory("child3")

        expected_output = "child1\nchild2\nchild3\n"
        with StringIO() as output, redirect_stdout(output):
            fs.list_directory()
            output_string = output.getvalue()

        self.assertEqual(output_string, expected_output)

