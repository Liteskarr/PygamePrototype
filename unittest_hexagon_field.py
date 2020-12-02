"""
Тесты для hexagon_field.py.
"""

import unittest

from hexagon_field import *


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.hexagon_field = HexagonField()

    def test_default_validator(self):
        pass

    def test_case(self):
        value: int = 1
        with self.assertRaises(ValueError):
            self.hexagon_field[HexagonPosition(0, 0)] = value
            self.hexagon_field[HexagonPosition(0, 1)] = value


if __name__ == '__main__':
    unittest.main()
