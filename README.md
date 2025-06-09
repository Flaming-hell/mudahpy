---

# mudahpy 🇮🇩
```
**mudahpy** adalah pustaka Python berbahasa Indonesia yang bertujuan untuk mempermudah pemrograman bagi pemula atau pengguna yang lebih nyaman dengan bahasa Indonesia.  
Proyek ini mengubah kata kunci, fungsi umum, dan struktur kontrol seperti `if`, `for`, `while`, `def`, `lambda`, dan lainnya agar lebih mudah dipahami.
```
---

## ✨ Contoh Penggunaan

```python
from mudahpy import *

# Percabangan
jika(
    5 > 3,
    aksi_utama=atau(tulis, "5 lebih besar dari 3"),
    aksi_default=atau(tulis, "5 tidak lebih besar dari 3")
)

# Perulangan for
untuk("angka", [1, 2, 3], lambda x: tulis("Angka ke:", x))

# Perulangan while
x = 0
selama(lambda: x < 3, lambda: (
    tulis("Nilai x =", x),
    globals().__setitem__("x", x + 1)
))

# Fungsi dan Matematika
def halo(nama):
    tulis("Halo,", nama)

halo("Suji")
tulis("Penjumlahan:", tambah(3, 5))

```
---

📦 Instalasi

Untuk saat ini, clone dan pasang secara lokal:

git clone https://github.com/username/mudahpy.git
cd mudahpy
pip install .

(Atau langsung dari direktori lokal saat ngoding, tambahkan ke $PYTHONPATH.)


---

📁 Struktur Proyek
```
mudahpy/
│
├── mudahpy/           # Pustaka utama
│   └── __init__.py    # Isi fungsi dan alias dalam bahasa Indonesia
│
├── contoh/            # Contoh penggunaan
│   └── contoh.py
│
├── README.md
├── setup.py
└── LICENSE
```

---

🎯 Tujuan

Mengedukasi dan membiasakan logika pemrograman menggunakan bahasa lokal.

Membantu anak-anak, pelajar, atau masyarakat umum agar lebih cepat memahami Python.

Proyek open-source untuk eksplorasi dan edukasi, bukan untuk pengembangan profesional berskala besar.



---

🤝 Kontribusi

Pull request sangat diterima!
Silakan fork, buat perubahan, dan ajukan PR.
Gunakan issues untuk ide atau perbaikan.


---

📝 Lisensi

Proyek ini menggunakan MIT License.

---

Kalau kamu ingin versi ringan atau ditambahkan badge, dokumentasi PyPI (jika diunggah), atau logo proyek, tinggal beri tahu!
