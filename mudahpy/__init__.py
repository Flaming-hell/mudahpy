# Fungsi built-in yang disederhanakan
tulis = print
panjang = len
jumlahkan = sum
daftar = list
kamus = dict
setel = input
urutkan = sorted
jenis = type
buka = open

# Tipe data versi Indonesia
Benar = True
Salah = False
TidakAda = None

# Fungsi bantu
def kembali(nilai):
    return nilai

def fungsi(f):
    return f

def muat(modul):
    globals()[modul] = __import__(modul)

# Fungsi matematika sederhana
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b

# Ganti lambda:
def atau(fungsi, *args, **kwargs):
    return lambda: fungsi(*args, **kwargs)

# Struktur logika seperti if-elif-else
def jika(kondisi_utama, aksi_utama, *kondisi_aksi_lain, aksi_default=None):
    if kondisi_utama:
        return aksi_utama()
    
    for i in range(0, len(kondisi_aksi_lain), 2):
        kondisi = kondisi_aksi_lain[i]
        aksi = kondisi_aksi_lain[i + 1]
        if kondisi:
            return aksi()
    
    if aksi_default:
        return aksi_default()

# Perulangan seperti for
def untuk(item, koleksi, aksi):
    for elemen in koleksi:
        aksi(elemen)

# Perulangan seperti while
def selama(kondisi_fungsi, aksi):
    while kondisi_fungsi():
        aksi()

# Struktur kelas
def buat_kelas(nama, basis=(), atribut=None):
    if atribut is None:
        atribut = {}
    return type(nama, basis, atribut)

# Alias untuk __init__
def inisial(self, *args, **kwargs):
    if hasattr(self, 'mulai'):
        self.mulai(*args, **kwargs)

# Fungsi dekorator untuk kelas
def kelas(cls):
    if hasattr(cls, 'mulai'):
        cls.__init__ = cls.mulai
        del cls.mulai
    return cls
