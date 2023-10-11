batas_awal = int(input(" Masukkan batas angka awal =  "))
batas_akhir = int(input(" Masukkan batas angka akhir =  "))

for i in range(batas_awal,batas_akhir+1):
    if i > 1 :
        for j in range(2,i): 
            if (i % j) == 0 :
              break
        else :
            print(i, "Adalah Bilangan Prima")