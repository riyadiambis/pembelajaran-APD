# for i in range (10):
#     print(f"ini perulangan ke {i}")
# # f= menggabungkan semua tipe data , tanpa koma gunakan kurung{}


# for ulang in range (23):
#     print(f"* yang ke {ulang}")

# b1=["ajis","mujahid", "tian"]
# print(b1)

# for i in  b1:
#     print (f"isi dari list adalah",i)

# perulangan terbatas
# ngekasih kondisi khusus = while

# baris dan kolom
# for i in range (10):
#     print("+", end="-")


# print("*")
# for i in range(7):
#     for j in range (4):
#         print("*", end=" ")
#     print()


# for i in range(0, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(0, 5):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}', end=" ")
#     print('')


# dompet = [1000, 2000, 3000, 4000]
# panjang = len(dompet)
# for uang in range(panjang):
#     print(dompet[uang])

# laporan_keuangan = [
# 2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
# -5000000, 7500000, 10000000, -1500000, 25000000, -2500000
# ]

# total_pengeluaran, total_pemasukan = 0, 0
# for dana in laporan_keuangan:
#     if dana > 0:
#         total_pemasukan += dana
#     else:
#         total_pengeluaran += dana
# hutang = total_pengeluaran * -1 
# print(hutang) 
# print(total_pemasukan)


# i = 5
# while i < 10:
#     i = i + 1
#     print (i)


# ==
# <=
# >=


# username = input('masukkan username : ')
# while username == "":
#     username = input('masukkan WOY: ')

# print(username)

# jawab = input('Jawaban : ').upper()
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")


# angka = [2, 5, 8, 12, 15, 7, 20]
# # print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n % 2 == 0:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         continue
# print("Program selesai.")


# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print(f"Angka genap ditemukan: {i}")
# print("\nProgram selesai.")



# Jawab Gak? Hey

# while True:
#     nama=input("masukkan nama")
#     if nama=="mujahid":
#         print("kereen")
#         break
# print("program selesai")




