# Fungsi penjumlahan
def penjumlahan(angka1, angka2):
    return angka1 + angka2
# Fungsi pengurangan
def pengurangan(angka1, angka2):
    return angka1 - angka2
# Fungsi perkalian
def perkalian(angka1, angka2):
    return angka1 * angka2
# Fungsi pembagian
def pembagian(angka1, angka2):
    return angka1 / angka2

# Fungsi utama
def main():
    print("KALKULATOR")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    # Meminta input dari pengguna
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Menjalankan operasi sesuai pilihan pengguna
    if pilihan == '1':
        print("Hasil penjumlahan: ", penjumlahan(angka1, angka2))
    elif pilihan == '2':
        print("Hasil pengurangan: ", pengurangan(angka1, angka2))
    elif pilihan == '3':
        print("Hasil perkalian: ", perkalian(angka1, angka2))
    elif pilihan == '4':
        print("Hasil pembagian: ", pembagian(angka1, angka2))
    else:
        print("Pilihan tidak valid!")
# Memanggil fungsi utama
main()