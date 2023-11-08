data_susanti = {    
    "Nama": "Susanti",
    "Alamat": "Surakarta",
    "Prodi": "Sistem Informasi",
    "Semester": 5,
    "Angkatan": 2015
}
print("Data diri Susanti pada tahun 2015 :")
for key, value in data_susanti.items():
    print(f"{key} : {value}")

print()
print("Pada tahun 2018 Susanti pindah ke Madura dan beralih ke prodi Teknik Informatika")
data_susanti["Alamat"] = "Madura"
data_susanti["Prodi"] = "Teknik Informatika"
data_susanti["Semester"] = 1
data_susanti["Angkatan"] = 2018

print("Data diri Susanti pada tahun 2018:")
for key, value in data_susanti.items():
    print(f"{key} : {value}")

print()
print("Pada tahun 2019 Susanti memutuskan untuk berhenti menjadi mahasiswi")
data_susanti["Prodi"] = "Tidak Ada"
data_susanti["Semester"] = "Tidak Ada"
data_susanti["Angkatan"] = "Tidak Ada"

print("Data diri Susanti pada tahun 2019 :")
for key, value in data_susanti.items():
    print(f"{key} : {value}")