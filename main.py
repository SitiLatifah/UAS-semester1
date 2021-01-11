from view.view_nilai import cari,cetak,header,notoption
from view.input_nilai import inputan,ubah,hapus
header()
while True:

    c = input("\nPilih Opsi: ")

    # EXIT PROGRAM
    if c.lower() == 'k':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.\n"
              "               Siti Latifah                 \n"
              "                 TI.20.A2                 ")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    # PRINT DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 't':
        inputan()

    # UBAH DATA
    elif c.lower() == 'u':
        ubah()

    # MENCARI DATA
    elif c.lower() == 'c':
        cari()

    # HAPUS DATA
    elif c.lower() == 'h':
        hapus()

    else:
        notoption()

