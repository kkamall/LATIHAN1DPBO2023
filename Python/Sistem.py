# Import class
from Mahasiswa import Mahasiswa

# Inisialisasi class
class Sistem:
    # Method menambah data atribut ke dalam objek list
    def add_data(dataMahasiswa):
        # Input data atribut mahasiswa
        nama = str(input("Masukkan Nama Mahasiswa: "))
        nim = str(input("Masukkan NIM Mahasiswa: "))
        prodi = str(input("Masukkan Prodi Mahasiswa: "))
        fakultas = str(input("Masukkan Fakultas Mahasiswa: "))
        # Memasukkan data mahasiswa ke dalam objek list
        dataMahasiswa.append(Mahasiswa(nama, nim, prodi, fakultas))

    # Method mengubah data atribut ke dalam objek list
    def ubah_data(dataMahasiswa):
        # Input data atribut NIM mahasiswa yang ingin diubah
        nim_ubah = str(input("Masukkan NIM Mahasiswa yang Ingin Diubah: "))
        i = 0
        flag = 0
        # Looping mencari index data atribut mahasiswa berdasarkan NIM inputan user
        while flag == 0:
            if dataMahasiswa[i].get_nim() == nim_ubah:
                index = i
                flag = 1
            i += 1
        # Input data atribut mahasiswa kembali
        nama = str(input("Masukkan Nama Mahasiswa: "))
        nim = str(input("Masukkan NIM Mahasiswa: "))
        prodi = str(input("Masukkan Prodi Mahasiswa: "))
        fakultas = str(input("Masukkan Fakultas Mahasiswa: "))
        # Re-Assign nilai pada objek list
        dataMahasiswa[index].set_nama(nama)
        dataMahasiswa[index].set_prodi(prodi)
        dataMahasiswa[index].set_nim(nim)
        dataMahasiswa[index].set_fakultas(fakultas)

    # Method menghapus data atribut mahasiswa
    def hapus_data(dataMahasiswa):
        # Input data atribut NIM mahasiswa yang ingin dihapus
        nim_hapus = str(input("Masukkan NIM Mahasiswa yang Ingin Dihapus: "))
        flag = 0
        i = 0
        # Looping mencari index data atribut mahasiswa berdasarkan NIM inputan user
        while flag == 0:
            if dataMahasiswa[i].get_nim() == nim_hapus:
                index = i
                flag = 1
            i += 1
        # Menghapus data atribut mahasiswa dari objek list
        dataMahasiswa.pop(index)

    # Method untuk menampilkan data mahasiswa
    def tampilkan_data(dataMahasiswa):
        print("Press Enter to Continue...\n---")

        # Mencari String Terpanjang
        if len(dataMahasiswa) == 0:
            print("Belum Ada Data Mahasiswa yang Terekam...")
        else:
            print("Data Mahasiswa:")
            panjang = [3, 4, 13, 8]
            for pembelajar in dataMahasiswa:
                # String NIM terpanjang
                if len(pembelajar.get_nim()) > panjang[0]:
                    panjang[0] = len(pembelajar.get_nim())
                # String Nama terpanjang
                if len(pembelajar.get_nama()) > panjang[1]:
                    panjang[1] = len(pembelajar.get_nama())
                # String Program Studi terpanjang
                if len(pembelajar.get_prodi()) > panjang[2]:
                    panjang[2] = len(pembelajar.get_prodi())
                # String Fakultas terpanjang
                if len(pembelajar.get_fakultas()) > panjang[3]:
                    panjang[3] = len(pembelajar.get_fakultas())
            
            # Menampilkan Header Tabel
            # Bagian Atas
            print("+", end="")
            # NIM
            for i in range(panjang[0] + 2):
                print("-", end="")
            print("+", end="")
            # Nama
            for i in range(panjang[1] + 2):
                print("-", end="")
            print("+", end="")
            # Program Studi
            for i in range(panjang[2] + 2):
                print("-", end="")
            print("+", end="")
            # Fakultas
            for i in range(panjang[3] + 2):
                print("-", end="")
            print("+")

            # Bagian Tengah
            print("| NIM",end="")
            for i in range(panjang[0]-2):
                print(" ", end="")
            print("| Nama", end="")
            for i in range(panjang[1]-3):
                print(" ", end="")
            print("| Program Studi", end="")
            for i in range(panjang[2]-12):
                print(" ", end="")
            print("| Fakultas", end="")
            for i in range(panjang[3]-7):
                print(" ", end="")
            print("|")

            # Bagian Bawah
            print("+", end="")
            # NIM
            for i in range(panjang[0] + 2):
                print("-", end="")
            print("+", end="")
            # Nama
            for i in range(panjang[1] + 2):
                print("-", end="")
            print("+", end="")
            # Program Studi
            for i in range(panjang[2] + 2):
                print("-", end="")
            print("+", end="")
            # Fakultas
            for i in range(panjang[3] + 2):
                print("-", end="")
            print("+")

            # Mengeluarkan Output Data Mahasiswa
            i = 1
            for pembelajar in dataMahasiswa:
                # NIM
                print(f"| {pembelajar.get_nim()}", end="")
                for i in range(panjang[0]-len(pembelajar.get_nim())+1):
                    print(" ", end="")
                # Nama
                print(f"| {pembelajar.get_nama()}", end="")
                for i in range(panjang[1]-len(pembelajar.get_nama())+1):
                    print(" ", end="")
                # Program Studi
                print(f"| {pembelajar.get_prodi()}", end="")
                for i in range(panjang[2]-len(pembelajar.get_prodi())+1):
                    print(" ", end="")
                # Fakultas
                print(f"| {pembelajar.get_fakultas()}", end="")
                for i in range(panjang[3]-len(pembelajar.get_fakultas())+1):
                    print(" ", end="")
                print("|")
                i += 1

            # Mengeluarkan Output Footer Tabel
            print("+", end="")
            # NIM
            for i in range(panjang[0] + 2):
                print("-", end="")
            print("+", end="")
            # Nama
            for i in range(panjang[1] + 2):
                print("-", end="")
            print("+", end="")
            # Program Studi
            for i in range(panjang[2] + 2):
                print("-", end="")
            print("+", end="")
            # Fakultas
            for i in range(panjang[3] + 2):
                print("-", end="")
            print("+")

        # Agar tidak langsung ke menu setelah nge-print tabel
        input()