print("=== Program Peminjaman Buku Perpustakaan ===")

# Bagian Login nih Ges
# Bisa juga sih langsung while sesuatu == kondidisi, contohnya pada penanganan yah
while True:
    user = input("Masukkan username: ")
    while user == "":
        user = input("Masukkan username ehhh: ")
    pw = input("Masukkan password: ")
    while pw == "":
        pw = input("Masukkan password ehhh: ")

    if user == "admin" and pw == "1234":
        print("Login berhasil!\n")
        break
    else:
        print("Password salah pak. Jangan panik, silahkan coba lagi!\n")

# Kalian kasih nol semua dulu biar nanti bisa kita jadikan variabel penampungan
# Nanti kalian bisa print hasil hasilnya dengan dibedakan gini
total_buku = 0
total_fiksi = 0
total_nonfiksi = 0
total_komik = 0
total_pelajaran = 0



# Nah ini bisa pakai True, ada contoh yang menggunakan kondisi di file perpusKondisi.py
while True:
    print("Masukkan data buku yang dipinjam")
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
        continue

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

    ulang = input("Masih ingin tambah data lagi nda? (ya/tidak): ").lower()
    # Biar mudah kita gunakan not atau negasi buat ngeluarin ini dari perulangan yah
    if ulang != "ya":
        break

# hasil akhir
print("\n=== Laporan Akhir Peminjaman Buku ===")
print("Total buku Fiksi     :", total_fiksi)
print("Total buku Nonfiksi  :", total_nonfiksi)
print("Total buku Komik     :", total_komik)
print("Total buku Pelajaran :", total_pelajaran)
print("Jumlah total buku dipinjam:", total_buku)
