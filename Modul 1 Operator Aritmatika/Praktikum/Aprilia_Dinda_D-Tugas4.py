import math

# Mencari volume kerucut dijadikan ke liter
# Diketahui
selimut_kerucut = 967.12
tinggi_kerucut = 20
garis_pelukis = 22
phi = math.pi  # Gunakan math.pi untuk nilai π yang lebih akurat

# Mencari Jari-Jari
r = garis_pelukis / (2 * phi)

print("Jari-Jari= ", r, "cm")

# Menghitung Volume Kerucut dengan satuan cm kubik
volume_kerucut = (1/3) * phi * r**2 * tinggi_kerucut

print("Volume Kerucut = ", volume_kerucut, "cm^3")

# Konversikan ke liter
liter = volume_kerucut / 1000

print("Kerucut dapat menampung sebanyak = ", liter, "Liter")