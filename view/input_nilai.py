def inputan():
    from model.daftar_nilai import tambah_kontak
    while (True):
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Masukan Nim dengan Angka')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Masukan TUGAS dengan Angka')
        except ValueError:
            print('Masukan TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan UTS dengan Angka')
        except ValueError:
            print('Masukan UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                p('Masukan UAS dengan Angka')
        except ValueError:
            print('Masukan UAS dengan Angka')
        else:
            break
    tambah_kontak(nama, nim, tugas, uts, uas)
    print("\n    (T) Tambah       (U) Ubah      (H) Hapus     (C) Cari      (L) Lihat     (K) Keluar   ")


def ubah():
    from model.daftar_nilai import ubah_kontak
    ubah_kontak(nama=input("Masukan nama untuk ubah data : "))


def hapus():
    from model.daftar_nilai import hapus
    hapus(nama=input("Masukan nama untuk menghapus data : "))
    print("\n    (T)Tambah       (U)Ubah      (H)Hapus     (C)Cari      (L)List     (K)Keluar   ")


def cari():
    from model.daftar_nilai import cari
    cari(nama=input("Masukan nama yang di cari : "))
