def factorial(angka):
    if angka == 0:
        return 1
    else:
        return angka * factorial(angka - 1)

# Fungsi utama
def main():
    print("PROGRAM FAKTORIAL")
    angka = int(input("Masukkan angka: "))

    # Memeriksa apakah angka negatif atau bukan
    if angka < 0:
        print("Angka harus positif!")
    else:
        print("Faktorial dari", angka, "adalah", factorial(angka))

# Memanggil fungsi utama
main()