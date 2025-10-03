# Tagihan

tagihan = [50000, 75000, -15000, 125000, 300000]
i = 0
total_tagihan = len(tagihan)
harus_dibayar = 0

while i < total_tagihan:
    if tagihan [i] < 0:
        i += 1
        continue
    harus_dibayar += tagihan[i]
    i += 1

print(harus_dibayar)



# Jawab Gak? Hey
while True :
    respon = input('Pilihan Y atau T : ').lower().strip()
    if respon in ['ya', 'y', 'tidak', 't']:
        break
    print('Input yang bener donk jangan ngasal')

print(respon)
if respon in ['ya', 'y']:
    print('y')
else :
    print('Ini yang salah')
