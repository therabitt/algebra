"""
Challenge: Polynomials  |  Phase 1 — Topic 1.9
"""
import math
print("CHALLENGE 1.9 — POLINOMIAL")

# Challenge 1: Lagrange Interpolation
# KONSEP: Interpolasi Lagrange menemukan polinomial berderajat n yang tepat melewati n+1 titik yang diberikan.
# ALGORITMA:
# P(x) = Σ (y_i * L_i(x)), di mana L_i(x) adalah polinomial basis Lagrange:
# L_i(x) = Π (x - x_j) / (x_i - x_j) untuk setiap j ≠ i
# LANGKAH:
# 1. Definisikan fungsi yang mengembalikan sebuah fungsi baru poly(x)
# 2. Dalam poly(x), inisialisasi result = 0.0
# 3. Iterasi tiap titik (x_i, y_i)
# 4. Hitung L_i(x) dengan loop perkalian untuk j ≠ i
# 5. Tambahkan y_i * L_i(x) ke result
# KOMPLEKSITAS: Waktu O(n^2) untuk evaluasi fungsi pada n titik
# IMPLEMENTASIKAN:
print("\n[Ch1] Interpolasi Lagrange")
print("  Temukan polinomial unik derajat n yang melewati n+1 titik")

def lagrange_interpolate(points):
    """
    Buat fungsi interpolasi Lagrange dari titik-titik.
    points: list of (x, y) pairs
    """
    # TODO: Kembalikan fungsi polinomial hasil interpolasi
    pass

# Challenge 2: Synthetic Division
# KONSEP: Pembagian Sintetis adalah metode cepat untuk membagi polinomial P(x) dengan faktor linier (x - r).
# LANGKAH:
# 1. Tulis koefisien P(x) secara berurutan [a_n, a_{n-1}, ..., a_0]
# 2. Bawa turun koefisien pertama: q_0 = a_n
# 3. Untuk setiap koefisien berikutnya c, kalikan hasil sebelumnya dengan r, dan tambahkan c: q_i = q_{i-1} * r + c
# 4. Elemen terakhir adalah sisa (remainder). Sisanya adalah koefisien hasil bagi (quotient).
# IMPLEMENTASIKAN:
print("\n[Ch2] Pembagian Sintetis (Synthetic Division)")
def synthetic_division(coeffs, divisor_root):
    """
    Bagi P(x) dengan (x - r) menggunakan pembagian sintetis.
    coeffs: koefisien dari derajat tinggi ke rendah [a_n, ..., a_0]
    """
    # TODO: Kembalikan tuple (quotient_coeffs_list, remainder)
    pass

print("\n[Selesai Challenge 1.9]")
