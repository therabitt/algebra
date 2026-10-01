"""
Exercises: Complex Numbers  |  Phase 1 — Topic 1.18
"""
import math, cmath
print("LATIHAN 1.18 — BILANGAN KOMPLEKS")
print("=" * 50)

# Ex 1: Operations
# KONSEP: Bilangan kompleks memiliki bagian real dan imajiner z = a + bi. Operasi aljabar dilakukan dengan memperlakukan i sebagai variabel dan i^2 = -1.
# LANGKAH:
# 1. Definisikan z1 dan z2
# 2. Hitung penjumlahan, perkalian, dan pembagian
# 3. Hitung modulus dan perkalian dengan konjugat
# IMPLEMENTASIKAN:
print("\n[Ex 1] Hitung:")
z1, z2 = 2+3j, 1-4j
# TODO: Hitung z1+z2, z1*z2, z1/z2, |z1|, dan z1*z1.conjugate()
pass

# Ex 2: Polar form
# KONSEP: Bentuk polar dari z = a + bi adalah r·e^(iθ), di mana r = |z| dan θ = arg(z).
# LANGKAH:
# 1. Hitung r menggunakan abs(z)
# 2. Hitung theta menggunakan cmath.phase(z)
# 3. Verifikasi dengan r * cmath.exp(1j*theta)
# IMPLEMENTASIKAN:
print("\n[Ex 2] Konversikan ke bentuk polar r·e^(iθ):")
numbers = [1+1j, -1+0j, 0-2j, 3+4j]
# TODO: Loop numbers dan konversikan ke polar
pass

# Ex 3: De Moivre
# KONSEP: Teorema De Moivre menyatakan (r·e^(iθ))^n = r^n · e^(i·nθ). Sangat berguna untuk menghitung pangkat.
# LANGKAH:
# 1. Hitung r dan theta dari z = 1 + 1j
# 2. Pangkatkan r dengan 8
# 3. Kalikan theta dengan 8
# IMPLEMENTASIKAN:
print("\n[Ex 3] Gunakan De Moivre untuk hitung (1+i)^8:")
z = 1 + 1j
# TODO: Hitung z^8 dengan De Moivre
pass

# Ex 4: nth roots
# KONSEP: Bilangan kompleks memiliki tepat n akar ke-n. Akar kuadrat dari e^(iθ) adalah e^(i(θ+2πk)/2) untuk k=0,1.
# LANGKAH:
# 1. Ubah z ke bentuk polar
# 2. Gunakan rumus akar ke-n untuk setiap k (k=0, 1)
# 3. Tampilkan hasilnya
# IMPLEMENTASIKAN:
print("\n[Ex 4] Temukan semua akar kuadrat dari i:")
# TODO: Temukan akar kuadrat dari i (k=0,1)
pass

# Ex 5: Fundamental theorem demo
# KONSEP: Teorema Fundamental Aljabar menyatakan bahwa polinomial berderajat n memiliki tepat n akar di himpunan bilangan kompleks.
# LANGKAH:
# 1. Cari 3 akar dari z^3 = 1
# 2. Verifikasi akar-akar tersebut dengan menghitung (z_k)^3 - 1
# IMPLEMENTASIKAN:
print("\n[Ex 5] Teorema Fundamental Aljabar:")
print("  z^3 - 1 = 0 memiliki TEPAT 3 akar di ℂ:")
# TODO: Cari akar-akar dari z^3-1=0 dan verifikasi
pass

print("\n[Selesai]")
