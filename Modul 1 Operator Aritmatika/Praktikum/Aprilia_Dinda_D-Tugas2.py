suku3 = 9
suku7 = 17
selisih = 4
b = (suku7-suku3)/selisih

print(b)

#mencari nilai a dari rumus suku ke- n= a+(n-1)*b caranya dipindah ruas
suku1 = suku3-2*b

print(suku1)

n = (int(input("masukkan suku ke-n yang ingin dicari")))
suku_ke_n = suku1+(n-1)*b
Sn = (n/2)*(2*suku_ke_n)

print("suku ke-n",suku_ke_n)
print("jumlah suku ke-n", Sn)