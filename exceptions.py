class CalculatorError(Exception):
    """Base exception untuk seluruh error pada aplikasi kalkulator."""


class DivisionByZeroError(CalculatorError):
    """Dilempar ketika terjadi pembagian atau modulus dengan nol."""

    def __init__(self, message: str = "Pembagian dengan nol tidak diperbolehkan.") -> None:
        super().__init__(message)


class NegativeSquareRootError(CalculatorError):
    """Dilempar ketika mencoba menghitung akar dari bilangan negatif."""

    def __init__(self, message: str = "Akar dari bilangan negatif tidak didukung.") -> None:
        super().__init__(message)


class InvalidInputError(CalculatorError):
    """Dilempar ketika input pengguna bukan angka yang valid."""

    def __init__(self, message: str = "Input harus berupa angka yang valid.") -> None:
        super().__init__(message)


class InvalidMenuError(CalculatorError):
    """Dilempar ketika pengguna memilih menu yang tidak tersedia."""

    def __init__(self, message: str = "Pilihan menu tidak tersedia.") -> None:
        super().__init__(message)
