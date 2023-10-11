print("NIM Terakhir Saya adalah 102")
baris = int(input("Masukkan size = ")) 
kolom = int(baris/2)

# angka 1
for i in range(1, baris+1): 
    print(" " * (baris-3)+"x")
print()

# angka 0
print("x" * baris) 
for i in range(1, kolom+4): 
    print("x" + " "* (baris-2) + "x") 
print("x" * baris)
print()

# angka 2
print("x" * baris)
for i in range(1, kolom+1):
    print(" " * (baris-1) + "x") 
print("x" * baris)
for i in range(1, kolom+1):
    print("x" + " ")
print("x" * baris)
