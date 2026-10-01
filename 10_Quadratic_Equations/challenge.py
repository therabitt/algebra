"""
Challenge: Quadratic Equations  |  Phase 1 — Topic 1.6
"""
import math
print("CHALLENGE 1.6 — PERSAMAAN KUADRAT")

# KONSEP: Persamaan kubik dapat diselesaikan dengan Formula Cardano dan metode Newton-Raphson.
# Challenge 1: Depressed Cubic intro (hubungan dengan kuadrat)
print("\n[Ch1] Dari Kuadrat ke Kubik: Formula Cardano (preview)")
print("  Persamaan kubik: t^3 + pt + q = 0")
print("  Diskriminan: D = -(4p^3 + 27q^2)")

# ALGORITMA: Formula Cardano
# Untuk persamaan kubik t^3 + pt + q = 0
# Solusi bisa didapatkan dengan mencari nilai cbrt(-q/2 + sqrt(q^2/4 + p^3/27))
# ditambah cbrt(-q/2 - sqrt(q^2/4 + p^3/27))
#
# LANGKAH:
# 1. Hitung nilai diskriminan D = -(4*p^3 + 27*q^2).
# 2. Hitung nilai inner = (q/2)^2 + (p/3)^3.
# 3. Jika inner >= 0, hitung akar kubik dari (-q/2 + sqrt(inner)) dan (-q/2 - sqrt(inner)).
# 4. Tambahkan kedua akar kubik tersebut untuk mendapatkan nilai t, lalu print.
# 5. Jika inner < 0, print informasi bahwa diperlukan bilangan kompleks (casus irreducibilis).
#
# TIPS: Untuk akar kubik dari bilangan negatif di Python, lakukan -((-x)**(1/3))
# 
# IMPLEMENTASIKAN:
def cardano_depressed(p, q):
    """Selesaikan t^3 + pt + q = 0 (depressed cubic)"""
    pass

# TODO: panggil dan uji cardano_depressed(-3, 2) dan cardano_depressed(1, -1)
# Jawaban:
# cardano_depressed(-3, 2) -> akar real t ≈ -2.0
# cardano_depressed(1, -1) -> akar real t ≈ 0.682328

# Challenge 2: Newton-Raphson untuk akar kuadrat
print("\n[Ch2] Newton-Raphson untuk menyelesaikan ax^2+bx+c=0")

# ALGORITMA: Metode Newton-Raphson
# Metode iteratif untuk mencari akar fungsi: x_{n+1} = x_n - f(x_n)/f'(x_n)
#
# LANGKAH:
# 1. Definisikan fungsi lokal f(x) = ax^2 + bx + c
# 2. Definisikan fungsi turunan df(x) = 2ax + b
# 3. Lakukan iterasi sebanyak max_iter:
# 4.    Hitung fx = f(x) dan dfx = df(x)
# 5.    Jika abs(dfx) sangat kecil (< 1e-15), hentikan iterasi (karena akan membagi dengan nol)
# 6.    Hitung x_new = x - (fx / dfx)
# 7.    Jika selisih abs(x_new - x) lebih kecil dari tol, return x_new (sudah konvergen)
# 8.    Update x = x_new
# 9. Return x hasil iterasi terakhir jika belum konvergen
#
# IMPLEMENTASIKAN:
def newton_raphson_quadratic(a, b, c, x0=1.0, tol=1e-10, max_iter=100):
    """
    Temukan akar ax^2+bx+c=0 menggunakan Newton-Raphson.
    f(x) = ax^2+bx+c,  f'(x) = 2ax+b
    x_{n+1} = x_n - f(x_n)/f'(x_n)
    """
    pass

# TODO: panggil newton_raphson_quadratic untuk (1, -5, 6, x0=4), (1, -5, 6, x0=1), dan (2, -4, -6, x0=5)
# Jawaban:
# (1,-5,6) x0=4 -> x=3.0
# (1,-5,6) x0=1 -> x=2.0
# (2,-4,-6) x0=5 -> x=3.0

print("\n[Selesai Challenge 1.6]")
