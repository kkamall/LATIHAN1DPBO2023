// Import library:
import java.util.Scanner;
import java.util.ArrayList;

class Main
{
    public static void main(String[] args)
    {
        // Inisialisasi list.
        ArrayList<Mahasiswa> dataMahasiswa = new ArrayList<>();

        // Inisialisasi scanner.
        Scanner sc = new Scanner(System.in);

        int fungsi = 0, i;
        String nama, prodi, fakultas, nim, nim_ubah;

        do 
        {
            // Clear console.
            System.out.print("\033[H\033[2J");
            System.out.flush();

            // Menampilkan menu.
            System.out.print("[");
            for(i = 0; i < 35 ; i++)
            {
                System.out.print("-");
            }
            System.out.print("MENU");
            for(i = 0; i < 35 ; i++)
            {
                System.out.print("-");
            }
            System.out.println("]");
            System.out.println("\n(1) Tambah Data | (2) Ubah Data | (3) Hapus Data | (4) Tampil Data | (5) END\n");
            System.out.print("[");
            for(i = 0; i < 74 ; i++)
            {
                System.out.print("-");
            }
            System.out.println("]\n");

            // Meminta masukkan user untuk menjalankan suatu fungsi
            System.out.print("Masukkan Angka Perintah: ");
            fungsi = sc.nextInt();
            System.out.println("---");
            
            // Menambah data.
            if(fungsi == 1)
            {
                System.out.print("Masukkan Nama Mahasiswa: ");
                nama = sc.next();
                System.out.print("Masukkan NIM Mahasiswa: ");
                nim = sc.next();
                System.out.print("Masukkan Program Studi Mahasiswa: ");
                prodi = sc.next();
                System.out.print("Masukkan Fakultas Mahasiswa: ");
                fakultas = sc.next();

                // Object buat menyimpan nilai sementara sebelum dimasukkan ke list.
                Mahasiswa temp = new Mahasiswa();
                temp.setNama(nama); temp.setNIM(nim); temp.setProdi(prodi); temp.setFakultas(fakultas);
                dataMahasiswa.add(temp);
            }
            // Mengubah data.
            else if(fungsi == 2)
            {
                // Meminta NIM mahasiswa yang ingin diubah datanya.
                System.out.print("Masukkan NIM Mahasiswa yang Ingin Diubah: ");
                nim_ubah = sc.next();
                System.out.println("---");

                // Meminta inputan data mahasiswa baru.
                System.out.print("Masukkan Nama Mahasiswa: ");
                nama = sc.next();
                System.out.print("Masukkan NIM Mahasiswa: ");
                nim = sc.next();
                System.out.print("Masukkan Program Studi Mahasiswa: ");
                prodi = sc.next();
                System.out.print("Masukkan Fakultas Mahasiswa: ");
                fakultas = sc.next();

                // Mencari data yang ingin diubah
                for(i = 0; i < dataMahasiswa.size(); i++)
                {
                    // Proses pengubahan data.
                    if(dataMahasiswa.get(i).getNIM().equals(nim_ubah))
                    {
                        dataMahasiswa.get(i).setNama(nama);
                        dataMahasiswa.get(i).setNIM(nim);
                        dataMahasiswa.get(i).setProdi(prodi);
                        dataMahasiswa.get(i).setFakultas(fakultas);
                        break;
                    }
                }
            }
            // Hapus data mahasiswa.
            else if(fungsi == 3)
            {
                // Meminta NIM mahasiswa yang ingin dihapus datanya.
                System.out.print("Masukkan NIM Mahasiswa yang Ingin Dihapus: ");
                nim_ubah = sc.next();

                // Mencari data yang ingin dihapus.
                for(i = 0; i < dataMahasiswa.size(); i++)
                {
                    // Proses penghapusan data.
                    if(dataMahasiswa.get(i).getNIM().equals(nim_ubah))
                    {
                        dataMahasiswa.remove(i);
                    }
                }
            }
            // Selesai.
            else if(fungsi == 5)
            {
                System.out.println("Terima Kasih...");
            }
            // Nampilin data mahasiswa.
            else if(fungsi == 4)
            {
                if(dataMahasiswa.isEmpty())
                {
                    System.out.println("Belum Terdapat Data Mahasiswa...");
                }
                else
                {
                    System.out.println("Press Enter to Continue...\n---\n(NIM - Nama - Program Studi - Fakultas)\n\n[-----------DATA MAHASISWA------------]\n");
                    for(i = 0; i < dataMahasiswa.size(); i++)
                    {
                        System.out.println((i + 1) + ". " + dataMahasiswa.get(i).getNIM() + " - " + dataMahasiswa.get(i).getNama() + " - " + dataMahasiswa.get(i).getProdi() + " - " + dataMahasiswa.get(i).getFakultas());
                    }
                }
                sc.nextLine();
                sc.nextLine();
            }
            else
            {
                System.out.println("Angka Di luar Jangkauan...");
            }
        } while (fungsi != 5);
    }
}
