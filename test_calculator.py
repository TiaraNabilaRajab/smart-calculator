import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculator import Calculator
from exceptions import DivisionByZeroError, InvalidInputError, NegativeSquareRootError
from history import HistoryManager
from utils import format_number, parse_number


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_add(self) -> None:
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self) -> None:
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_multiply(self) -> None:
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_divide(self) -> None:
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(DivisionByZeroError):
            self.calc.divide(5, 0)

    def test_power(self) -> None:
        self.assertEqual(self.calc.power(9, 2), 81)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)

    def test_sqrt(self) -> None:
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(0), 0)

    def test_sqrt_negative(self) -> None:
        with self.assertRaises(NegativeSquareRootError):
            self.calc.sqrt(-9)

    def test_modulus(self) -> None:
        self.assertEqual(self.calc.modulus(10, 3), 1)

    def test_modulus_by_zero(self) -> None:
        with self.assertRaises(DivisionByZeroError):
            self.calc.modulus(10, 0)

    def test_percentage(self) -> None:
        self.assertEqual(self.calc.percentage(200, 10), 20)
        self.assertEqual(self.calc.percentage(50, 50), 25)


class TestHistoryManager(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.history = HistoryManager(str(Path(self.temp_dir.name) / "history.txt"))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_save_and_load(self) -> None:
        self.history.save("5 + 3 = 8")
        entries = self.history.load()
        self.assertEqual(len(entries), 1)
        self.assertIn("5 + 3 = 8", entries[0])

    def test_load_missing_file(self) -> None:
        self.assertEqual(self.history.load(), [])

    def test_clear(self) -> None:
        self.history.save("10 / 2 = 5")
        self.assertTrue(self.history.clear())
        self.assertEqual(self.history.load(), [])

    def test_clear_missing_file(self) -> None:
        self.assertFalse(self.history.clear())


class TestUtils(unittest.TestCase):

    def test_parse_number_valid(self) -> None:
        self.assertEqual(parse_number("42"), 42.0)
        self.assertEqual(parse_number("3,5"), 3.5)
        self.assertEqual(parse_number(" -7 "), -7.0)

    def test_parse_number_invalid(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_number("abc")

    def test_format_number(self) -> None:
        self.assertEqual(format_number(8.0), "8")
        self.assertEqual(format_number(2.5), "2.5")

if __name__ == "__main__":
    unittest.main()
