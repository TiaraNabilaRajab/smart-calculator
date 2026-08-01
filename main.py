from typing import Callable

from calculator import Calculator
from exceptions import CalculatorError, InvalidMenuError
from history import HistoryManager
from utils import Color, format_number, loading_animation, print_banner, read_number


class Menu:

    def __init__(self) -> None:
        self.calculator = Calculator()
        self.history = HistoryManager()
        self._actions: dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("Tambah", lambda: self._binary_operation("+", self.calculator.add)),
            "2": ("Kurang", lambda: self._binary_operation("-", self.calculator.subtract)),
            "3": ("Kali", lambda: self._binary_operation("*", self.calculator.multiply)),
            "4": ("Bagi", lambda: self._binary_operation("/", self.calculator.divide)),
            "5": ("Pangkat", lambda: self._binary_operation("^", self.calculator.power)),
            "6": ("Akar", self._sqrt_operation),
            "7": ("Modulus", lambda: self._binary_operation("%", self.calculator.modulus)),
            "8": ("Persentase", self._percentage_operation),
            "9": ("Lihat History", self._show_history),
            "10": ("Hapus History", self._clear_history),
        }

    def display(self) -> None:
        print(f"\n{Color.CYAN}{Color.BOLD}===== SMART CALCULATOR ====={Color.RESET}")
        for key, (label, _) in self._actions.items():
            print(f"{Color.GREEN}{key:>2}.{Color.RESET} {label}")
        print(f"{Color.RED} 0.{Color.RESET} Keluar")

    def _binary_operation(self, symbol: str, operation: Callable[[float, float], float]) -> None:
        a = read_number("Masukkan angka pertama : ")
        b = read_number("Masukkan angka kedua   : ")
        result = operation(a, b)
        self._show_result(f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")

    def _sqrt_operation(self) -> None:
        value = read_number("Masukkan angka : ")
        result = self.calculator.sqrt(value)
        self._show_result(f"√{format_number(value)} = {format_number(result)}")

    def _percentage_operation(self) -> None:
        value = read_number("Masukkan nilai dasar   : ")
        percent = read_number("Masukkan persen (%)    : ")
        result = self.calculator.percentage(value, percent)
        self._show_result(f"{format_number(percent)}% dari {format_number(value)} = {format_number(result)}")

    def _show_result(self, entry: str) -> None:
        loading_animation()
        print(f"{Color.GREEN}{Color.BOLD}Hasil: {entry}{Color.RESET}")
        self.history.save(entry)

    def _show_history(self) -> None:
        entries = self.history.load()
        if not entries:
            print(f"{Color.YELLOW}Belum ada riwayat perhitungan.{Color.RESET}")
            return
        print(f"\n{Color.CYAN}{Color.BOLD}----- RIWAYAT PERHITUNGAN -----{Color.RESET}")
        for entry in entries:
            print(entry)

    def _clear_history(self) -> None:
        if self.history.clear():
            print(f"{Color.GREEN}Riwayat berhasil dihapus.{Color.RESET}")
        else:
            print(f"{Color.YELLOW}Tidak ada riwayat untuk dihapus.{Color.RESET}")

    def run(self) -> None:
        print_banner()
        while True:
            self.display()
            choice = input(f"{Color.BOLD}Pilih menu: {Color.RESET}").strip()

            if choice == "0":
                print(f"{Color.CYAN}Terima kasih telah menggunakan Smart Calculator!{Color.RESET}")
                break

            try:
                if choice not in self._actions:
                    raise InvalidMenuError(f"Menu '{choice}' tidak tersedia. Pilih 0-10.")
                _, handler = self._actions[choice]
                handler()
            except CalculatorError as error:
                print(f"{Color.RED}[!] {error}{Color.RESET}")


def main() -> None:
    try:
        Menu().run()
    except KeyboardInterrupt:
        print(f"\n{Color.CYAN}Program dihentikan. Sampai jumpa!{Color.RESET}")

if __name__ == "__main__":
    main()
