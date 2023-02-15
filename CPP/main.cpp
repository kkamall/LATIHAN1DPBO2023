// Import library dan file.
#include <bits/stdc++.h>
#include "Mahasiswa.cpp"
#include <cstdio>

// Standard namespace.
using namespace std;

int main()
{
    int i, fungsi = 0;
    string nama, prodi, fakultas, nim, nim_ubah;
    Mahasiswa temp;

    // List kumpulan data mahasiswa.
    list<Mahasiswa> dataMahasiswa;

    do
    {
        system("cls");
        // Nampilin menu.
        cout << "[";
        for(i = 0; i < 35; i++)
        {
            cout << "-";
        }
        cout << "MENU";
        for(i = 0; i < 35; i++)
        {
            cout << "-";
        }
        cout << "]\n";
        cout << "\n(1) Tambah Data | (2) Ubah Data | (3) Hapus Data | (4) Tampil Data | (5) END\n";
        cout << "\n[";
        for(i = 0; i< 74; i++)
        {
            cout << "-";
        }
        cout << "]\n\nMasukkan Angka Perintah: ";
        // Meminta user untuk menjalankan suatu perintah.
        cin >> fungsi;
        cout << "---\n";
        // Tambah Data.
        if (fungsi == 1)
        {
            // Input atribut.
            cout << "Masukkan Nama Mahasiswa: ";
            cin >> nama;
            cout << "Masukkan NIM Mahasiswa: ";
            cin >> nim;
            cout << "Masukkan Prodi Mahasiswa: ";
            cin >> prodi;
            cout << "Masukkan Fakultas Mahasiswa: ";
            cin >> fakultas;

            // Assign attribut.
            temp.set_nama(nama);
            temp.set_prodi(prodi);
            temp.set_fakultas(fakultas);
            temp.set_nim(nim);

            // Push ke list.
            dataMahasiswa.push_back(temp);
        }
        // Ubah data.
        else if (fungsi == 2)
        {
            // Input NIM data atribut mahasiswa yang ingin diubah datanya.
            cout << "Masukkan NIM Mahasiswa yang Ingin Diubah: ";
            cin >> nim_ubah;

            // Input data atribut mahasiswa yang baru.
            cout << "Masukkan Nama Mahasiswa: ";
            cin >> nama;
            cout << "Masukkan NIM Mahasiswa: ";
            cin >> nim;
            cout << "Masukkan Prodi Mahasiswa: ";
            cin >> prodi;
            cout << "Masukkan Fakultas Mahasiswa: ";
            cin >> fakultas;

            // Proses pengubahand data atribut mahasiswa.
            for (list<Mahasiswa>::iterator it = dataMahasiswa.begin(); it != dataMahasiswa.end(); it++)
            {
                if (it->get_nim() == nim_ubah)
                {
                    it->set_nama(nama);
                    it->set_nim(nim);
                    it->set_prodi(prodi);
                    it->set_fakultas(fakultas);
                }
            }
        }
        // Hapus Data.
        else if (fungsi == 3)
        {
            // Input data NIM mahasiswa yang ingin dihapus datanya.
            cout << "Masukkan NIM Mahasiswa yang Ingin Dihapus: ";
            cin >> nim_ubah;

            for (list<Mahasiswa>::iterator it = dataMahasiswa.begin(); it != dataMahasiswa.end(); it++)
            {
                if (it->get_nim() == nim_ubah)
                {
                    it = dataMahasiswa.erase(it);
                }
            }
        }
        // Menampilkan Data
        else if (fungsi == 4)
        {
            cout << "Press Enter to Continue...\n---\n";

            if(dataMahasiswa.empty())
            {
                cout << "Belum Terdapat Data Mahasiswa\n";
            }
            else
            {
                cout << "Data Mahasiswa\n";
                // Mencari String Terpanjang
                int panjang[4] = {3, 4, 13, 8};
                for(list<Mahasiswa>::iterator it = dataMahasiswa.begin(); it != dataMahasiswa.end(); it++)
                {
                    if(it->get_nim().length() > panjang[0])
                    {
                        panjang[0] = it->get_nim().length();
                    }
                    if(it->get_nama().length() > panjang[1])
                    {
                        panjang[1] = it->get_nama().length();
                    }
                    if(it->get_prodi().length() > panjang[2])
                    {
                        panjang[2] = it->get_prodi().length();
                    }
                    if(it->get_fakultas().length() > panjang[3])
                    {
                        panjang[3] = it->get_fakultas().length();
                    }
                }

                // Menampilkan Header Tabel.
                // Bagian Atas.
                cout << "+";
                // Header NIM.
                for(i = 0; i < panjang[0]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header nama.
                for(i = 0; i < panjang[1]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[2]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[3]+2; i++)
                {
                    cout << "-";
                }
                cout << "+\n";

                // Bagian tengah.
                cout << "| NIM";
                for(i = 0; i < panjang[0]-2; i++)
                {
                    cout << " ";
                }
                cout << "| Nama";
                for(i = 0; i < panjang[1]-3; i++)
                {
                    cout << " ";
                }
                cout << "| Program Studi";
                for(i = 0; i < panjang[2]-12; i++)
                {
                    cout << " ";
                }
                cout << "| Fakultas";
                for(i = 0; i < panjang[3]-7; i++)
                {
                    cout << " ";
                }
                cout << "|\n";

                // Bagian bawah.
                cout << "+";
                // Header NIM.
                for(i = 0; i < panjang[0]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header nama.
                for(i = 0; i < panjang[1]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[2]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[3]+2; i++)
                {
                    cout << "-";
                }
                cout << "+\n";

                // Output data mahasiswa.
                for (list<Mahasiswa>::iterator it = dataMahasiswa.begin(); it != dataMahasiswa.end(); it++)
                {
                    cout << "| " << it->get_nim();
                    for(i = 0; i < panjang[0]-it->get_nim().length()+1; i++)
                    {
                        cout << " ";
                    }
                    cout << "| " << it->get_nama();
                    for(i = 0; i < panjang[1]-it->get_nama().length()+1; i++)
                    {
                        cout << " ";
                    }
                    cout << "| " << it->get_prodi();
                    for(i = 0; i < panjang[2]-it->get_prodi().length()+1; i++)
                    {
                        cout << " ";
                    }
                    cout << "| " << it->get_fakultas();
                    for(i = 0; i < panjang[3]-it->get_fakultas().length()+1; i++)
                    {
                        cout << " ";
                    }
                    cout << "|\n";
                }

                // Bagian footer.
                cout << "+";
                // Header NIM.
                for(i = 0; i < panjang[0]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header nama.
                for(i = 0; i < panjang[1]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[2]+2; i++)
                {
                    cout << "-";
                }
                cout << "+";
                // Header program studi.
                for(i = 0; i < panjang[3]+2; i++)
                {
                    cout << "-";
                }
                cout << "+\n";
            }
            fflush(stdin);
            getchar();
        }
        else if(fungsi == 5)
        {
            cout << "Terima Kasih...\n";
        }

    } while (fungsi != 5);

    return 0;
}