# 🧮 Smart Calculator CLI

Aplikasi kalkulator berbasis terminal (CLI) yang dibangun dengan **Python murni** (tanpa library eksternal). Proyek ini dirancang sebagai portofolio yang menerapkan **OOP, Exception Handling, Modular Programming, Unit Testing, dan Clean Code** sesuai standar PEP8.

---

## ✨ Fitur

### Operasi Dasar
- ➕ Penjumlahan
- ➖ Pengurangan
- ✖️ Perkalian
- ➗ Pembagian

### Operasi Lanjutan
- Pangkat (`x^y`)
- Akar kuadrat (`√x`)
- Modulus (`x % y`)
- Persentase (`n% dari x`)

### Fitur Tambahan
- 📜 **Riwayat perhitungan** — setiap hasil disimpan ke `history.txt` lengkap dengan timestamp
- 🗑️ Lihat & hapus riwayat kapan saja
- 🎨 Tampilan terminal berwarna (ANSI Escape Code)
- ⏳ Animasi loading sederhana
- 🖼️ Banner ASCII saat aplikasi dibuka
- 🛡️ Validasi input & exception handling menyeluruh — program **tidak akan crash**

---

## 🖥️ Preview Menu

```text
===== SMART CALCULATOR =====
 1. Tambah
 2. Kurang
 3. Kali
 4. Bagi
 5. Pangkat
 6. Akar
 7. Modulus
 8. Persentase
 9. Lihat History
10. Hapus History
 0. Keluar
Pilih menu:
```

---

## 📁 Struktur Folder

```text
smart-calculator/
│
├── main.py              # Entry point + class Menu (UI & alur aplikasi)
├── calculator.py        # Class Calculator (seluruh operasi matematika)
├── history.py           # Class HistoryManager (simpan/baca/hapus riwayat)
├── utils.py             # Warna terminal, banner, animasi, validasi input
├── exceptions.py        # Custom exception (DivisionByZeroError, dll.)
├── README.md
├── requirements.txt     # Kosong — hanya standard library
├── .gitignore
└── tests/
    └── test_calculator.py   # Unit test (unittest)
```

---

## 🚀 Instalasi

> Prasyarat: **Python 3.12+**

```bash
# 1. Clone repository
git clone https://github.com/<username>/smart-calculator.git

# 2. Masuk ke folder proyek
cd smart-calculator

# Tidak perlu install dependency — 100% standard library!
```

---

## ▶️ Cara Menjalankan

```bash
python main.py
```

---

## 💡 Contoh Penggunaan

```text
Pilih menu: 1
Masukkan angka pertama : 5
Masukkan angka kedua   : 3
Menghitung...
Hasil: 5 + 3 = 8

Pilih menu: 9
----- RIWAYAT PERHITUNGAN -----
[2026-07-08 10:15:32] 5 + 3 = 8
[2026-07-08 10:15:40] 10 / 2 = 5
[2026-07-08 10:15:55] 9 ^ 2 = 81
```

Contoh penanganan error:

```text
Pilih menu: 4
Masukkan angka pertama : 5
Masukkan angka kedua   : 0
[!] Pembagian dengan nol tidak diperbolehkan.

Pilih menu: 99
[!] Menu '99' tidak tersedia. Pilih 0-10.
```

---

## 🧪 Menjalankan Test

```bash
python -m unittest discover tests -v
```

Hasil: **18 test — OK** ✅ (operasi dasar, pembagian nol, pangkat, akar negatif, history, validasi input)

---

## 📸 Screenshot

> _Placeholder — tambahkan screenshot aplikasi di sini._

![Banner aplikasi](docs/screenshot-banner.png)
![Contoh perhitungan](docs/screenshot-calculation.png)

---

## 🔮 Future Improvement

- [ ] Mode ekspresi bebas (mis. `5 + 3 * 2` dengan parser)
- [ ] Riwayat dalam format JSON/SQLite
- [ ] Konversi satuan & mata uang
- [ ] Operasi ilmiah (sin, cos, log)
- [ ] Konfigurasi tema warna oleh pengguna
- [ ] Distribusi sebagai package (`pip install`)

---

## 🎓 Skill yang Dipelajari

| Konsep | Penerapan |
|---|---|
| **OOP** | `Calculator`, `HistoryManager`, `Menu` — pemisahan tanggung jawab (SRP) |
| **Exception Handling** | Custom exception hierarchy + penanganan terpusat |
| **Function & Type Hint** | Setiap operasi = method terpisah dengan anotasi tipe |
| **File I/O** | Baca/tulis riwayat dengan `pathlib` & context manager |
| **Unit Testing** | 18 test case dengan `unittest` |
| **Clean Code** | PEP8, docstring, naming jelas, tanpa duplikasi |
| **CLI/UX** | ANSI color, banner ASCII, animasi loading, validasi input |

---

## 📄 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan portofolio. Bebas digunakan dan dimodifikasi.
