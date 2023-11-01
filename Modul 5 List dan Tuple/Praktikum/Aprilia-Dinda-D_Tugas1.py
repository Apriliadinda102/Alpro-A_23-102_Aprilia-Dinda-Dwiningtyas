print("== HEWAN BERSAYAP ==")
List1 = []
Hewan = int(input("MASUKKAN INGIN BERAPA KALI ANDA AKAN MENGULANG = "))
for i in range(Hewan):
    Hewan_Bersayap = str(input("MASUKKAN HEWAN BERSAYAP = "))
    List1.append(Hewan_Bersayap)
print(List1)
print(" ")

print("== HEWAN BERKAKI 2 ==")
List2 = []
ulang = int(input("MASUKKAN INGIN BERAPA KALI ANDA AKAN MENGULANG = "))
for i in range(ulang):
    hewan = str(input("MASUKKAN HEWAN BERKAKI 2 = "))
    List2.append(hewan)
print(List2)
print(" ")

print("== NAMA TEMAN TERDEKAT ==")
List3 = []
teman = int(input("MASUKKAN INGIN BERAPA KALI ANDA AKAN MENGULANG = "))
for i in range(teman):
    nama = str(input("MASUKKAN  NAMA TEMAN TERDEKAT ANDA = "))
    List3.append(nama)
print(List3)
print(" ")

print("== TANGGAL LAHIR TEMAN TERDEKAT ==")
List4 = []
tanggal = int(input("MASUKKAN INGIN BERAPA KALI ANDA AKAN MENGULANG = "))
for i in range(tanggal):
    Tanggal_Lahir = int(input("MASUKKAN TANGGAL LAHIR TEMAN TERSEBUT = "))
    List4.append(Tanggal_Lahir)
print(List4)
print(" ")

print("LIST KE LIMA")
List5 = [13, 31, 2, 19, 96]
print("Angka = ", List5)
print(" ")

gabung = List1[:5] + List4
print("Output 1 =", gabung)

List3[4] = 'DINDA'
print("Output 2 = ", List3)

del List5[4]
del List5[2]
# Nilai = List5
print("Output 3 = ", List5)

kombinasi = List4 + List5
max_value = max(kombinasi)
min_value = min(kombinasi)
print(f"Output 4 = {kombinasi} Nilai Maksimal: {max_value}  Nilai Minimal: {min_value}")