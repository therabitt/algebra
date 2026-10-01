"""
Exercises: Systems of Equations  |  Phase 1 — Topic 1.7
"""
print("LATIHAN 1.7 — SISTEM PERSAMAAN")
print("=" * 50)

# KONSEP:
# Aturan Cramer memecahkan sistem 2x2 linear a1*x + b1*y = c1, a2*x + b2*y = c2.
# x = Dx/D, y = Dy/D
# di mana D = determinan = a1*b2 - a2*b1. 
# Jika D == 0, maka tidak ada satu solusi unik (bisa inkonsisten/parallel atau dependen/infinite).
# LANGKAH:
# 1. Buat fungsi cramer_2x2() untuk menghitung D, Dx, dan Dy.
# 2. Jika D=0, return None, None. 
# 3. Jika bukan, return Dx/D dan Dy/D.
# IMPLEMENTASIKAN:
def cramer_2x2(a1,b1,c1, a2,b2,c2):
    # TODO: Hitung Aturan Cramer
    pass

# Ex 1: Substitution
print("\n[Ex 1] Metode Substitusi:")
print("  y = 2x + 1")
print("  3x + y = 16")
print("  Substitusi: 3x + (2x+1) = 16 -> 5x=15 -> x=3, y=7")
# IMPLEMENTASIKAN:
# TODO: Panggil cramer_2x2(-2,1,1, 3,1,16) (karena -2x + y = 1) dan cetak verifikasinya.
pass

# Ex 2: Elimination
print("\n[Ex 2] Metode Eliminasi:")
print("  2x + 3y = 12")
print("  4x - 3y = 6")
print("  Tambahkan: 6x = 18 -> x=3; 2(3)+3y=12 -> y=2")
# IMPLEMENTASIKAN:
# TODO: Verifikasikan kembali hasil x dan y menggunakan cramer_2x2().
pass

# Ex 3: Classification
print("\n[Ex 3] Klasifikasi Sistem:")
# KONSEP:
# Berdasarkan determinan, jika D!=0, maka "Konsisten" dengan satu solusi persis (bertemu di 1 titik).
# Jika D==0 dan a1/a2 = c1/c2, maka "Dependen" dengan tak terbatas solusi (garis identik berhimpitan).
# Jika D==0 dan a1/a2 != c1/c2, maka "Inkonsisten" dan tidak ada solusi (garis sejajar).
# IMPLEMENTASIKAN:
systems = [
    (1,-1,3, 2,-2,6, "Dependen (garis sama)"),
    (1,1,3,  1,1,5,  "Inkonsisten (paralel)"),
    (2,3,7,  1,-1,1, "Konsisten (satu solusi)"),
]
# TODO: Ulangi sistem persamaan, hitung determinan, identifikasi dan print klasifikasinya.
pass

# Ex 4: 3-variable system
print("\n[Ex 4] Sistem 3 Variabel (Gaussian Elimination):")
print("   x +  y +  z = 6")
print("  2x - y +  z = 3")
print("   x +  y - 2z = -3")
# KONSEP:
# Pemecahan numerikal dapat diselesaikan dengan cepat melalui matriks dan linalg Numpy jika terpasang.
# LANGKAH:
# 1. Deklarasikan NumPy array untuk matriks persamaan [3x3] dan solusinya [3].
# 2. Selesaikan dengan `np.linalg.solve()`.
# IMPLEMENTASIKAN:
# TODO: Hitung (bila numpy ada), jika ada exception ImportError abaikan saja.
pass

# Ex 5: Word problem
print("\n[Ex 5] Soal Campuran:")
print("  50 kg campuran kacang A (Rp30.000/kg) dan B (Rp20.000/kg)")
print("  harga total Rp1.200.000")
print("  x + y = 50,  30000x + 20000y = 1200000")
# IMPLEMENTASIKAN:
# TODO: Selesaikan dengan fungsi Cramer dan cetak perbandingan kilogramnya.
pass

print("\n[Selesai]")
