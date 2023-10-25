def hitung_kpk(a, b):
    # Mencari FPB (Faktor Persekutuan Terbesar) terlebih dahulu
    def cari_fpb(a, b):
        while b:
            a, b = b, a % b
        return a

    # Rumus KPK = (a * b) / FPB(a, b)
    #// pembagian bilangan bulat agar tidak ada angka desimal
    return (a * b) // cari_fpb(a, b)
# Input dua bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Memanggil fungsi untuk menghitung KPK
kpk = hitung_kpk(bilangan1, bilangan2)
print("KPK dari", bilangan1 ,"dan ", bilangan2 , "adalah", kpk) 