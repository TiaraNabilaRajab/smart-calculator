import math

from exceptions import DivisionByZeroError, NegativeSquareRootError


class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError()
        return a / b

    def power(self, base: float, exponent: float) -> float:
        return base ** exponent

    def sqrt(self, value: float) -> float:
        if value < 0:
            raise NegativeSquareRootError()
        return math.sqrt(value)

    def modulus(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Modulus dengan nol tidak diperbolehkan.")
        return a % b

    def percentage(self, value: float, percent: float) -> float:
        return (value * percent) / 100
