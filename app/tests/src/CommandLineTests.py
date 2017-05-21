import unittest

from app.main.src import CommandLine


class CommandLineTests(unittest.TestCase):
    def test_with_fire(self):
        commander = CommandLine()
        commander.loadReport("hello")
