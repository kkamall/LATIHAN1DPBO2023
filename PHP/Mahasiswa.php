<?php 

// Inisialisasi kelas.
class Mahasiswa
{
    // Private attribute:
    private $nama = '';
    private $nim = '';
    private $prodi = '';
    private $fakultas = '';
    private $gambar = '';

    // Konstruktor.
    public function __construct($nama = '', $nim = '', $prodi = '', $fakultas = '', $gambar = '')
    {
        $this->nama = $nama;
        $this->nim = $nim;
        $this->prodi = $prodi;
        $this->fakultas = $fakultas;
        $this->gambar = $gambar;
    }

    // Setter.
    // Nama mahasiswa.
    public function set_nama($nama)
    {
        $this->nama = $nama;
    }
    // Program strudi.
    public function set_prodi($prodi)
    {
        $this->prodi = $prodi;
    }
    // NIM.
    public function set_nim($nim)
    {
        $this->nim = $nim;
    }
    // Fakultas.
    public function set_fakultas($fakultas)
    {
        $this->fakultas = $fakultas;
    }
    // Gambar.
    public function set_gambar($gambar)
    {
        $this->gambar = $gambar;
    }

    // Getter.
    // Nama mahasiswa.
    public function get_nama()
    {
        return $this->nama;
    }
    // NIM.
    public function get_nim()
    {
        return $this->nim;
    }
    // Program studi.
    public function get_prodi()
    {
        return $this->prodi;
    }
    // Fakultas
    public function get_fakultas()
    {
        return $this->fakultas;
    }
    // Gambar
    public function get_gambar()
    {
        return $this->gambar;
    }

    // Destruktor.
    function __destruct()
    {
    }
}

?>