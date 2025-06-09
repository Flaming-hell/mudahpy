from mudahpy import *

# Percabangan
jika(
    5 > 3,
    aksi_utama=lambda: tulis("5 lebih besar dari 3"),
    aksi_default=lambda: tulis("5 tidak lebih besar dari 3")
)

# Perulangan for
tulis("\nContoh perulangan:")
untuk("angka", [1, 2, 3], lambda x: tulis("Angka ke:", x))

# Perulangan while
tulis("\nContoh selama:")
x = 0
selama(lambda: x < 3, lambda: (
    tulis("Nilai x =", x),
    globals().__setitem__("x", x + 1)
))

# Fungsi dan matematika
def halo(nama):
    tulis("Halo,", nama)

halo("Suji")

tulis("Penjumlahan:", tambah(4, 5))
tulis("Perkalian:", kali(3, 7))

# Kelas
@kelas
class Orang:
    def mulai(self, nama):
        self.nama = nama
        tulis("Objek dibuat untuk:", self.nama)

    def sapa(self):
        tulis("Hai,", self.nama)

# Pakai kelas
p = Orang("Rina")
p.sapa()
