# Import class file
import os
from Sistem import Sistem

# Array menampung data mahasiswa
dataMahasiswa = []
# Masukkan user untuk menjalankan suatu fungsi
fungsi = 0

# Fungsi while untuk menjalankan sistem
while fungsi != 5:
    # Clear command prompt
    os.system('cls' if os.name == 'nt' else 'clear')
    # Menu Fungsi
    print("[", end="")
    for i in range(35):
        print("-", end="")
    print("MENU", end="")
    for i in range(35):
        print("-", end="")
    print("]")
    print("\n(1) Tambah Data | (2) Ubah Data | (3) Hapus Data | (4) Tampil Data | (5) END\n")
    print("[", end="")
    for i in range(74):
        print("-", end="")
    print("]\n")
    # User memilih fungsi yang ingin dijalankan
    fungsi = int(input("Masukkan Angka perintah: "))
    print("---")

    # Menjalankan fungsi add data
    if fungsi == 1:
        Sistem.add_data(dataMahasiswa)

    # Menjalankan fungsi ubah data
    elif fungsi == 2:
        Sistem.ubah_data(dataMahasiswa)

    # Menjalankan fungsi hapus data
    elif fungsi == 3:
        Sistem.hapus_data(dataMahasiswa)
        # dataMahasiswa.pop(index)

    # Menjalankan fungsi menampilkan data
    elif fungsi == 4:
        Sistem.tampilkan_data(dataMahasiswa)

    # Selesai
    else:
        print("Terima Kasih...")
