nama = str(input("Masukkan nama = "))
nim = int(input("Masukkan nim = "))
nilai_uts = int(input("Masukkan nilai uts = "))
nilai_uas = int(input("Masukkan nilai uas = "))
rata_rata = (nilai_uas + nilai_uts)/2
print("Rata-rata nilai anda = ", rata_rata)

if rata_rata <= 100 and rata_rata >= 80 :
    print("Anda mendapatkan nilai A")
elif rata_rata <= 80 and rata_rata >=70 :
    print("Anda mendapatkan nilai B")
elif rata_rata <= 70 and rata_rata >= 60 :
    print("Anda mendapatkan nilai C")
elif rata_rata <= 60 and rata_rata >= 40 :
    print("Anda mendapatkan nilai D")
else :
    print("Anda mendapatkan nilai E")