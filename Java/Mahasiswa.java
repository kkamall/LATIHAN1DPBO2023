// Deklarasi kelas.
public class Mahasiswa 
{
    // Private atribut:
    private String nama;
    private String nim;
    private String prodi;
    private String fakultas;

    // Konstruktor.
    public Mahasiswa()
    {
        this.nama = "";
        this.nim = "";
        this.prodi = "";
        this.fakultas = "";
    }

    public Mahasiswa(String nama, String prodi, String fakultas, String nim)
    {
        this.nama = nama;
        this.prodi = prodi;
        this.nim = nim;
        this.fakultas = fakultas;
    }

    // Getter dan Setter.
    // Setter.
    public void setNama(String nama)
    {
        this.nama = nama;
    }
    public void setNIM(String nim)
    {
        this.nim = nim;
    }
    public void setProdi(String prodi)
    {
        this.prodi = prodi;
    }
    public void setFakultas(String fakultas)
    {
        this.fakultas = fakultas;
    }

    // Getter.
    public String getNama()
    {
        return this.nama;
    }
    public String getProdi()
    {
        return this.prodi;
    }
    public String getNIM()
    {
        return this.nim;
    }
    public String getFakultas()
    {
        return this.fakultas;
    }
}
