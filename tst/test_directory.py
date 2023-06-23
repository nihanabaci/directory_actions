import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.directory import Directory


class DirectoryTests(unittest.TestCase):
    def test_add_child(self):
        parent = Directory("parent")
        child = Directory("child")
        parent.add_child(child)
        self.assertIn(child, parent.children)

    def test_find_child_existing(self):
        parent = Directory("parent")
        child = Directory("child")
        parent.add_child(child)
        found_child = parent.find_child("child")
        self.assertEqual(child, found_child)

    def test_find_child_non_existing(self):
        parent = Directory("parent")
        found_child = parent.find_child("child")
        self.assertIsNone(found_child)

    def test_remove_child(self):
        parent = Directory("parent")
        child = Directory("child")
        parent.add_child(child)
        parent.remove_child(child)
        self.assertNotIn(child, parent.children)

    def test_list_children(self):
        parent = Directory("parent")
        child1 = Directory("child1")
        child2 = Directory("child2")
        parent.add_child(child1)
        parent.add_child(child2)

        expected_output = "parent\n  child1\n  child2\n"
        with StringIO() as output, redirect_stdout(output):
            parent.list_children()
            output_string = output.getvalue()

        self.assertEqual(output_string, expected_output)


