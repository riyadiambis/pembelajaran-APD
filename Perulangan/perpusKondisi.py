print("=== Program Peminjaman Buku Perpustakaan ===")

# inisialisasi variabel total
total_buku = 0
total_fiksi = 0
total_nonfiksi = 0
total_komik = 0
total_pelajaran = 0

# mulai dengan variabel yang akan mengontrol jalannya cerita kita
ulang = "y"

while ulang == "y":
    print("\nMasukkan data buku yang dipinjam")
    kategori = input("Kategori buku (Fiksi/Nonfiksi/Komik/Pelajaran): ").lower()

    # nested if untuk kondisi buku
    if kategori == "fiksi":
        kondisi = input("Kondisi buku (baru/lama): ").lower()
        if kondisi == "baru":
            print("Kategori: Fiksi (Baru)")
        else:
            print("Kategori: Fiksi (Lama)")

    elif kategori == "nonfiksi":
        kondisi = input("Kondisi buku (baru/lama): ").lower()
        if kondisi == "baru":
            print("Kategori: Nonfiksi (Baru)")
        else:
            print("Kategori: Nonfiksi (Lama)")

    elif kategori == "komik":
        kondisi = input("Kondisi buku (baru/lama): ").lower()
        if kondisi == "baru":
            print("Kategori: Komik (Baru)")
        else:
            print("Kategori: Komik (Lama)")

    elif kategori == "pelajaran":
        kondisi = input("Kondisi buku (baru/lama): ").lower()
        if kondisi == "baru":
            print("Kategori: Pelajaran (Baru)")
        else:
            print("Kategori: Pelajaran (Lama)")

    else:
        print("Kategori tidak valid!\n")
        continue  # kembali ke atas loop jika salah input

    # input jumlah buku
    jumlah = int(input("Masukkan jumlah buku yang dipinjam: "))
    print("Jumlah buku:", jumlah, "\n")

    # tambahkan ke total berdasarkan kategori
    if kategori == "fiksi":
        total_fiksi += jumlah
    elif kategori == "nonfiksi":
        total_nonfiksi += jumlah
    elif kategori == "komik":
        total_komik += jumlah
    elif kategori == "pelajaran":
        total_pelajaran += jumlah

    total_buku += jumlah
    # nah di sini kita tidak usah memanfaatkan break, jadinya lebih sederhana
    ulang = input("Masih ingin tambah data lagi nda? (y/t): ").lower()

# laporan akhir
print("\n=== Laporan Akhir Peminjaman Buku ===")
print("Total buku Fiksi     :", total_fiksi)
print("Total buku Nonfiksi  :", total_nonfiksi)
print("Total buku Komik     :", total_komik)
print("Total buku Pelajaran :", total_pelajaran)
print("Jumlah total buku dipinjam:", total_buku)
