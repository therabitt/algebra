"""
Challenge: Exponents and Logarithms  |  Phase 1 — Topic 1.11
"""
import math
print("CHALLENGE 1.11 — EKSPONEN DAN LOGARITMA")

# Challenge 1: Compute e from scratch
# KONSEP: Nilai konstanta Euler (e) dapat dihitung melalui deret Taylor: e = Σ (1/n!) untuk n=0 ke ∞.
# LANGKAH:
# 1. Inisialisasi sum = 0 dan factorial = 1
# 2. Loop dari n = 0 ke terms
# 3. Update factorial dan tambahkan 1/factorial ke sum
# 4. Bandingkan hasil dengan math.e
# IMPLEMENTASIKAN:
print("\n[Ch1] Menghitung e dari deret Taylor")
def compute_e(terms=20):
    # TODO: Hitung estimasi e dari deret taylor
    pass

# Challenge 2: Compute ln from scratch (Newton's method)
# KONSEP: Menghitung logaritma alami (ln x) dengan mencari akar dari f(y) = e^y - x = 0 menggunakan metode Newton-Raphson: y_new = y - f(y)/f'(y).
# LANGKAH:
# 1. Fungsi objektif: f(y) = e^y - x. Turunannya: f'(y) = e^y
# 2. Rumus Newton: y_new = y - (e^y - x) / e^y
# 3. Mulai dengan y = 1.0, lalu iterasi sampai perbedaan < toleransi
# IMPLEMENTASIKAN:
print("\n[Ch2] Menghitung ln(x) menggunakan Newton-Raphson")
def my_ln(x, tol=1e-12, max_iter=100):
    # TODO: Implementasi metode Newton untuk mencari ln(x)
    pass

# Challenge 3: Logistic growth model
# KONSEP: Model pertumbuhan populasi yang dibatasi kapasitas maksimum (carrying capacity K).
# LANGKAH:
# 1. Tuliskan rumus: P(t) = K / (1 + ((K - P0) / P0) * e^(-rt))
# 2. Evaluasi untuk nilai P0, K, r, t yang diberikan
# IMPLEMENTASIKAN:
print("\n[Ch3] Model Pertumbuhan Logistik (Logistic Growth)")
def logistic(P0, K, r, t):
    """Carrying capacity model."""
    # TODO: Kembalikan nilai fungsi logistik
    pass

print("\n[Selesai Challenge 1.11]")
