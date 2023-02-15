# Inisialisasi Class
class Mahasiswa:
    # Atribut mahasiswa
    __nama = ""
    __nim = ""
    __prodi = ""
    __fakultas = ""

    # Konstruktor
    def __init__(self, nama="", nim="", prodi="", fakultas=""):
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi
        self.__fakultas = fakultas

    # Setter
    def set_nama(self, nama=""):
        self.__nama = nama

    def set_nim(self, nim=""):
        self.__nim = nim

    def set_prodi(self, prodi=""):
        self.__prodi = prodi

    def set_fakultas(self, fakultas=""):
        self.__fakultas = fakultas

    # Getter
    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def get_prodi(self):
        return self.__prodi
        
    def get_fakultas(self):
        return self.__fakultas