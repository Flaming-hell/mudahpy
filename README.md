---

📦 README.md

# 🇮🇩 mudahpy

**mudahpy** adalah pustaka Python yang mempermudah penulisan program menggunakan kata-kata dalam bahasa Indonesia. Cocok untuk pemula atau pembelajar yang ingin lebih cepat memahami logika pemrograman tanpa terhambat istilah asing.

---

## ✨ Fitur

- Ganti kata kunci/fungsi umum ke dalam Bahasa Indonesia
- Sintaks seperti `jika`, `untuk`, `selama`, `kembali`, `tulis`, dll.
- Dukungan struktur `if-elif-else`, `for`, `while`, dan `class`
- Fungsi matematika dasar (`tambah`, `kurang`, `kali`, `bagi`)
- Perpustakaan ringan dan mudah diperluas

---

## 🔧 Instalasi (Lokal)

Clone dan pasang secara lokal:

```bash
git clone https://github.com/namakamu/mudahpy.git
cd mudahpy
pip install .

Atau mode edit:

pip install -e .


---

🧪 Contoh Penggunaan

contoh.py

from mudahpy import *

jika(Benar,
    aksi_utama=lambda: tulis("Halo, dunia!"),
    aksi_default=lambda: tulis("Ini tidak muncul")
)

untuk("item", [1, 2, 3], lambda x: tulis("Angka:", x))

x = 0
selama(lambda: x < 3, lambda: (
    tulis("x =", x),
    globals().__setitem__("x", x + 1)
))

@kelas
class Sapa:
    def mulai(self, nama):
        self.nama = nama
        tulis("Halo,", self.nama)

orang = Sapa("Rina")


---

🧰 Kata Kunci yang Didukung

Bahasa Indonesia	Python asli

tulis	print
panjang	len
kembali	return
jika	if/elif/else
untuk	for
selama	while
Benar	True
Salah	False
TidakAda	None
kelas + mulai	class + __init__


---

🧑‍💻 Kontribusi

Saran kata baru? Boleh banget! Fork, tambahkan, dan kirim pull request 😄
Contoh ide: cetak, hapus, bandingkan, dll.


---

⚠️ Catatan

Ini adalah pustaka edukatif. Untuk produksi, tetap direkomendasikan menggunakan sintaks Python standar.


---

🪪 Lisensi

MIT © 2025 - Flaming-hell
