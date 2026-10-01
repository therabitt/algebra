"""
Exercises: Functions and Relations  |  Phase 1 — Topic 1.8
"""
import math
print("LATIHAN 1.8 — FUNGSI DAN RELASI")
print("=" * 50)

# Ex 1: Domain
# KONSEP: Domain fungsi adalah himpunan semua nilai input yang membuat fungsi terdefinisi secara real.
# LANGKAH:
# 1. Untuk akar √f(x), syaratnya f(x) ≥ 0
# 2. Untuk pecahan 1/f(x), syaratnya f(x) ≠ 0
# 3. Untuk logaritma ln(f(x)), syaratnya f(x) > 0
# IMPLEMENTASIKAN:
print("\n[Ex 1] Tentukan domain fungsi:")
# TODO: Implementasikan pengecekan domain untuk f(x)=√(x-3), g(x)=1/(x²-4), h(x)=ln(2x-1)

# Ex 2: Composition
# KONSEP: Komposisi fungsi (f∘g)(x) berarti memasukkan hasil g(x) sebagai input ke f(x).
# LANGKAH:
# 1. Hitung nilai g(x)
# 2. Masukkan hasil tersebut ke fungsi f
# 3. Tunjukkan bahwa pada umumnya f(g(x)) ≠ g(f(x))
# IMPLEMENTASIKAN:
print("\n[Ex 2] Komposisi Fungsi")
def f(x): return 2*x + 3
def g(x): return x**2 - 1
# TODO: Hitung (f∘g)(2) dan (g∘f)(2)

# Ex 3: Inverse
# KONSEP: Fungsi invers f⁻¹(x) membalikkan operasi fungsi f(x). f(f⁻¹(x)) = x.
# LANGKAH:
# 1. Tulis y = f(x)
# 2. Selesaikan persamaan untuk mendapatkan x dalam bentuk y
# 3. Tukar variabel untuk mendapatkan f⁻¹(x)
# IMPLEMENTASIKAN:
print("\n[Ex 3] Fungsi Invers")
print("  f(x) = 3x - 5  ->  invers: f^-1(x) = (x+5)/3")
# TODO: Buat fungsi f_inv(x) dan verifikasi f_inv(f(x)) == x

# Ex 4: Even/Odd
# KONSEP: Fungsi genap memenuhi f(-x) = f(x) (simetris sumbu y). Fungsi ganjil memenuhi f(-x) = -f(x) (simetris titik asal).
# LANGKAH:
# 1. Evaluasi f(x) dan f(-x) untuk rentang nilai tes (x ≠ 0)
# 2. Jika selisih absolut f(x) - f(-x) mendekati nol, fungsi itu genap
# 3. Jika selisih absolut f(x) + f(-x) mendekati nol, fungsi itu ganjil
# IMPLEMENTASIKAN:
print("\n[Ex 4] Fungsi Genap dan Ganjil")
def is_even(f, test_range=range(-5,6)):
    pass # TODO
def is_odd(f, test_range=range(-5,6)):
    pass # TODO

# Ex 5: Piecewise
# KONSEP: Fungsi piecewise didefinisikan dengan aturan berbeda pada interval domain yang berbeda.
# LANGKAH:
# 1. Gunakan blok if-elif-else
# 2. Evaluasi kondisi x untuk memilih rumus yang sesuai
# IMPLEMENTASIKAN:
print("\n[Ex 5] Fungsi Pecahan (Piecewise)")
def piecewise(x):
    # TODO: Implementasikan -x jika x<0, x^2 jika 0<=x<3, 9 jika x>=3
    pass

print("\n[Selesai]")
