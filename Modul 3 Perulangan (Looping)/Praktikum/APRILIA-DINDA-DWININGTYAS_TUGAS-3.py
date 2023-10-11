ulang = str("iya")

while (ulang=="iya") :
    Harian = 2000
    Mingguan = 5000
    Total = 0

    Hari = int(input(" Masukkan total hari peminjaman = "))

    for i in range (1,Hari+1) :
        if i >7 :
            Total += Harian
            if i % 7 == 0 :
                Total += Mingguan
    if Hari > 7 :
        print(" Pengembalian buku sudah lewat 1 minggu dan terlambat selama ",Hari-7,"hari dan wajib membayar denda sebesar Rp.",Total)
        ulang = input('Ulangi program (iya/tidak) = ')
        
    else :
        print(" Terimakasih telah mengembalikan buku tepat waktu sehingga anda tidak dikenai denda apapun. ")
        ulang = input('Ulangi program (iya/tidak) = ')