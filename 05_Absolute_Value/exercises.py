"""
Exercises: Absolute Value  |  Phase 1 — Topic 1.15
"""
import math
print("LATIHAN 1.15 — NILAI MUTLAK")
print("=" * 50)

# Ex 1: Compute
print("\n[Ex 1] Hitung nilai mutlak:")
# KONSEP:
# Nilai mutlak mengembalikan besaran (magnitude) positif dari sebuah angka. 
# Secara matematis, |x| = x jika x >= 0, dan -x jika x < 0.
# LANGKAH:
# 1. Loop melalui daftar nilai (misal: -7, 0, 3.14, -sqrt(2)).
# 2. Cetak nilai dari tiap elemen menggunakan fungsi abs() bawaan Python.
# IMPLEMENTASIKAN:
# TODO: Hitung dan cetak nilai mutlak
pass

# Ex 2: Solve equations
print("\n[Ex 2] Selesaikan persamaan:")
print("  a) |x-5| = 3  ->  x-5=3 atau x-5=-3  ->  x=8 atau x=2")
# KONSEP:
# Persamaan nilai mutlak |A| = B memiliki 2 kemungkinan solusi: A = B atau A = -B (jika B >= 0).
# LANGKAH:
# 1. Pecah menjadi dua kemungkinan untuk masing-masing persamaan (a, b, c).
# 2. Hitung nilai x dan verifikasi kembali ke persamaan menggunakan substitusi dan fungsi abs().
# IMPLEMENTASIKAN:
# TODO: Selesaikan persamaan b) |2x+1| = 7 dan c) |x+2| = |2x-1|, lalu cetak dan uji hasil x-nya.
pass

# Ex 3: Solve inequalities
print("\n[Ex 3] Selesaikan pertidaksamaan:")
print("  a) |x| ≤ 4  ->  -4 ≤ x ≤ 4  (interval [-4, 4])")
# KONSEP:
# - |A| < B berarti jaraknya kurang dari B, ekuivalen dengan -B < A < B. (Interval tertutup/And).
# - |A| > B berarti jaraknya lebih dari B, ekuivalen dengan A > B ATAU A < -B. (Interval terbuka/Or).
# LANGKAH:
# 1. Untuk a) |x| ≤ 4, tentukan range solusinya. Lakukan tes iterasi manual untuk memverifikasi.
# 2. Untuk b) |2x-3| > 5, selesaikan pertidaksamaan menjadi x > 4 atau x < -1. Verifikasi dengan titik uji (test points).
# IMPLEMENTASIKAN:
# TODO: Lakukan pengecekan dengan list test point, cetak boolean benar/salah.
pass

# Ex 4: Distance interpretation
print("\n[Ex 4] Interpretasi jarak:")
print("  Semua x yang berjarak kurang dari 3 dari titik x=5:")
# KONSEP:
# Secara geometris, |x - a| adalah jarak antara titik x dan titik a di garis bilangan.
# LANGKAH:
# 1. Jarak ke 5 kurang dari 3 berarti |x - 5| < 3, sehingga intervalnya 2 < x < 8.
# 2. Uji menggunakan beberapa titik x dan print hasilnya.
# IMPLEMENTASIKAN:
# TODO: Iterasikan beberapa nilai untuk membuktikan apakah d = abs(x-5) < 3.
pass

# Ex 5: Triangle inequality
print("\n[Ex 5] Verifikasi ketidaksamaan segitiga pada bilangan kompleks:")
z1, z2 = 3+4j, 1-2j
# KONSEP:
# Ketidaksamaan Segitiga: |a + b| ≤ |a| + |b|. 
# Ini berlaku untuk semua bilangan real maupun kompleks (sebagai jarak vektor di ruang Euclid).
# LANGKAH:
# 1. Definisikan dua bilangan kompleks z1 dan z2.
# 2. Hitung sisi kiri LHS = abs(z1 + z2).
# 3. Hitung sisi kanan RHS = abs(z1) + abs(z2).
# 4. Bandingkan dan cetak verifikasinya (dengan margin error numerik karena perbandingan float).
# IMPLEMENTASIKAN:
# TODO: Hitung LHS dan RHS dan buktikan Ketidaksamaan Segitiga.
pass

print("\n[Selesai]")
