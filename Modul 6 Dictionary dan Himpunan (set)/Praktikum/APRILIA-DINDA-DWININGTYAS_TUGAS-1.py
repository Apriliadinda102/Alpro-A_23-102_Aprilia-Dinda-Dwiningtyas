print("Pada hari pertama Siska meminjam 3 buku pelajaran")
buku_pelajaran = set() 
for i in range (1,4): 
    buku_pelajaran.add(input(f"Masukkan buku pelajaran {i} : "))
print("Buku pelajaran yang dipinjam : ",buku_pelajaran)
print()

print("Hari selanjutnya Siska meminjam 5 buku cerita")
buku_cerita = set() 
for i in range (1,6): 
    buku_cerita.add(input(f"Masukkan buku cerita {i} : "))
print("Buku cerita yang dipinjam : ",buku_cerita) 
print() 

print("Setelah 1 minggu, Siska membawa 2 buku pelajaran dan 3 buku cerita untuk ditukarkan") 
for i in range (1,3):
    buku_pelajaran.remove(input(f"Buku yang ingin dikembalikan {i} : "))
print("Sisa buku pelajaran yang di pinjam Siska : ",buku_pelajaran) 
print()
for j in range (1,4): 
    buku_cerita.remove(input(f"Buku cerita yang ingin dikembalikan {j} : ")) 
print("Sisa buku cerita yang di pinjam Siska : ", buku_cerita) 
print()

print("Kemudian Siska menukarkan 5 buku pelajaran dan 2 buku cerita ")
for i in range (1,6): 
    buku_pelajaran.add(input(f"Masukkan buku pelajaran yang di pinjam {i} : ")) 
print("Hasil buku pelajaran setelah ditukarkan Siska", buku_pelajaran) 
print()
for j in range (1,3): 
   buku_cerita.add(input(f"Masukkan buku cerita yang di pinjam {j} : ")) 
print("Hasil buku cerita setelah ditukarkan Siska", buku_cerita) 
print()
print("Buku yang dipinjam Siska saat ini adalah : ", buku_cerita)
print("Buku yang dipinjam Siska saat ini adalah : ", buku_pelajaran)