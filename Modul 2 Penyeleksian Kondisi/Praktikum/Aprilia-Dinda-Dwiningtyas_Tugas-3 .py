nama = str(input("Masukkan nama mahasiswa = "))
skor = int(input("Masukkan skor mahasiswa = "))
ipk = float(input("Masukkan IPK mahasiswa = "))

if skor > 1100 and ipk >= 3.0 :
    print("Selamat!", nama,"anda lulus persyaratan beasiswa")
    print("dengan skor", skor, "dan ipk", ipk)
else :
    print("Mohon maaf", nama,"anda tidak lulus persyaratan beasiswa")
    print("dikarenakan skor anda", skor,"dan ipk anda", ipk)