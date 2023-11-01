kendaraan = input("Masukkan 5 nama kendaraan ( dan dipisahkan dengan koma ) = ")
T1 = tuple(kendaraan.split(','))
T2 = (10,30,45,21,12,13,31,90)
T3 = ("pRaktikum", "praktikum", "Praktikum", "PraKtIkuM", "PRAKTIKUM")

output1 = (T3[1], T3[3], T3[4], T1[4], T1[2])
print("Output 1 = ", output1)

output2 = (T2[3], T2[5]) * 3
print("Output 2 = ", output2)