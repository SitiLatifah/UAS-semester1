kontak = {}


def tambah_kontak(nama,nim,tugas,uts,uas):
    akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    kontak[nama] = nama,nim,tugas,uts,uas,akhir


def ubah_kontak(nama):
    if nama in kontak.keys():
        del kontak[nama]
        print("\n===Masukan Perubahan Data===")
        from view.input_nilai import inputan
        inputan()
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("    (T)Tambah       (U)ubah      (H)Hapus     (C)Cari      (L)Lihat     (K)Keluar   ")


def cari(nama):
    if nama in kontak.keys():
        print("\n=====================================================================")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|=================|==================|=======|=======|===============|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, kontak[nama][1], kontak[nama][2],kontak[nama][3],kontak[nama][4], kontak[nama][5]))
        print("======================================================================")
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


def hapus(nama):
    if nama in kontak.keys():
        del kontak[nama]
        return True
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        return False
