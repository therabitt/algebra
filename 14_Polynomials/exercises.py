"""
Exercises: Polynomials  |  Phase 1 — Topic 1.9
"""
import math
print("LATIHAN 1.9 — POLINOMIAL")
print("=" * 50)

# KONSEP: Polinomial dievaluasi dengan mengganti x dengan nilai yang diberikan.
# LANGKAH:
# 1. Definisikan list koefisien.
# 2. Iterasi untuk menghitung jumlah tiap suku.
# IMPLEMENTASIKAN:
class P:
    def __init__(self, *c): 
        # TODO: inisialisasi koefisien
        pass
    def __call__(self, x):
        # TODO: evaluasi polinomial untuk nilai x
        pass
    def degree(self): 
        # TODO: return derajat polinomial
        pass

# Ex 1
print("\n[Ex 1] Evaluasi P(x) = x^4 - 3x^3 + 2x - 7 untuk x=-1,0,1,2,3")
# TODO: Buat objek P dan evaluasi untuk setiap x
pass

# Ex 2: degree and leading term
# KONSEP: Derajat polinomial adalah pangkat tertinggi dari x. Leading term adalah koefisien dari suku berpangkat tertinggi.
# LANGKAH:
# 1. Cari elemen terakhir dari array koefisien (yang merepresentasikan pangkat tertinggi)
# 2. Panjang array minus 1 adalah derajat polinomial
# IMPLEMENTASIKAN:
print("\n[Ex 2] Identifikasi derajat dan koefisien leading:")
# TODO: Identifikasi derajat dan koefisien leading untuk 4x^5-x^3+2x-9, 7, -3x^2+x
pass

# Ex 3: Remainder theorem
# KONSEP: Teorema Sisa menyatakan bahwa sisa pembagian P(x) dengan (x - a) adalah P(a).
# LANGKAH:
# 1. Substitusi x = a ke dalam P(x)
# 2. Hasil evaluasi adalah sisa pembagian
# IMPLEMENTASIKAN:
print("\n[Ex 3] Gunakan Teorema Sisa untuk P(x)=x^3+2x^2-5x-6:")
# TODO: Hitung sisa untuk P(x)/(x-a) dengan a=1,-1,2,-2,3,-3
pass

# Ex 4: Factor theorem
# KONSEP: Teorema Faktor menyatakan (x - a) adalah faktor dari P(x) jika dan hanya jika P(a) = 0.
# LANGKAH:
# 1. Hitung P(a)
# 2. Jika nilai P(a) mendekati nol (dengan toleransi error floating point), maka (x-a) adalah faktor
# IMPLEMENTASIKAN:
print("\n[Ex 4] Tentukan faktor dari P(x)=x^3-6x^2+11x-6")
# TODO: Cek (x-a) adalah faktor untuk a dalam range -4 sampai 4
pass

# Ex 5: End behavior
# KONSEP: Perilaku ujung grafik polinomial saat x menuju +∞ atau -∞ ditentukan oleh derajat (genap/ganjil) dan tanda leading coefficient (positif/negatif).
# LANGKAH:
# 1. Amati leading term: -2x^3 (derajat ganjil, tanda negatif)
# 2. Jika x -> +inf, maka -2x^3 -> -inf
# 3. Jika x -> -inf, maka -2x^3 -> +inf
# IMPLEMENTASIKAN:
print("\n[Ex 5] Perilaku ujung (end behavior):")
print("  P(x) = -2x^3 + ... (derajat ganjil, leading negatif)")
# TODO: Tunjukkan perilaku dengan print nilai P(x) untuk x = -100, -10, 10, 100
pass

print("\n[Selesai]")
