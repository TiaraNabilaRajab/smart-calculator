from datetime import datetime
from pathlib import Path


class HistoryManager:
    def __init__(self, file_path: str = "history.txt") -> None:
        self.file_path = Path(file_path)

    def save(self, entry: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with self.file_path.open("a", encoding="utf-8") as file:
                file.write(f"[{timestamp}] {entry}\n")
        except OSError as error:
            print(f"[!] Gagal menyimpan history: {error}")

    def load(self) -> list[str]:
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return [line.rstrip("\n") for line in file if line.strip()]
        except FileNotFoundError:
            return []
        except OSError as error:
            print(f"[!] Gagal membaca history: {error}")
            return []

    def clear(self) -> bool:
        try:
            self.file_path.unlink()
            return True
        except FileNotFoundError:
            return False
        except OSError as error:
            print(f"[!] Gagal menghapus history: {error}")
            return False
