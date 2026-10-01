"""
Exercises: Exponents and Logarithms  |  Phase 1 — Topic 1.11
"""
import math
print("LATIHAN 1.11 — EKSPONEN DAN LOGARITMA")
print("=" * 50)

# Ex 1: Exponent laws
# KONSEP: Hukum eksponen: a^m * a^n = a^(m+n), a^m / a^n = a^(m-n), (a^m)^n = a^(m*n). Pangkat 0 menghasilkan 1, pangkat negatif berarti 1/a^n, dan pangkat pecahan berarti akar.
# LANGKAH:
# 1. Gunakan operator ** di Python untuk menghitung secara langsung
# 2. Bandingkan hasil komputasi dengan perhitungan manual menggunakan aturan eksponen
# IMPLEMENTASIKAN:
print("\n[Ex 1] Sederhanakan menggunakan hukum eksponen:")
# TODO: Hitung dan bandingkan perhitungan eksponen (mis. 2^3 * 2^4, (5^2)^3, dll)
pass

# Ex 2: Logarithm laws
# KONSEP: Logaritma adalah invers dari eksponen. log_b(x) = y berarti b^y = x.
# LANGKAH:
# 1. Gunakan math.log(x, b) untuk basis bebas, math.log10 untuk basis 10, math.log untuk basis e (ln).
# 2. Hitung nilai logaritma dan cocokkan dengan ekspektasi matematisnya
# IMPLEMENTASIKAN:
print("\n[Ex 2] Hitung nilai logaritma:")
# TODO: Hitung log_2(64), log10(0.001), ln(e^5), log_5(125)
pass

# Ex 3: Solve exponential equations
# KONSEP: Persamaan eksponensial diselesaikan dengan mengambil logaritma dari kedua sisi atau dengan menyamakan basis.
# LANGKAH:
# 1. Jika basis bisa disamakan (contoh: 4^x = 64 menjadi 4^x = 4^3), samakan pangkatnya
# 2. Jika tidak bisa disamakan, ambil logaritma (contoh: x = log_4(64))
# IMPLEMENTASIKAN:
print("\n[Ex 3] Selesaikan persamaan eksponen:")
# TODO: Cukup print penyelesaian persamaan 4^x=64, 10^(2x-1)=1000, 5^(x+2)=25^x
pass

# Ex 4: Compound interest
# KONSEP: Formula Bunga Majemuk: A = P(1 + r/n)^(nt).
# LANGKAH:
# 1. Definisikan principal P, rate r, freq n, time t.
# 2. Masukkan ke dalam rumus
# IMPLEMENTASIKAN:
print("\n[Ex 4] Bunga Majemuk: A = P(1 + r/n)^(nt)")
# TODO: Hitung hasil investasi selama 1, 5, 10, 20 tahun
pass

# Ex 5: Half-life
# KONSEP: Peluruhan radioaktif/waktu paruh memiliki rumus N(t) = N0 * (1/2)^(t/t_half).
# LANGKAH:
# 1. Tentukan jumlah awal N0 dan t_half
# 2. Hitung N(t) untuk nilai t tertentu
# 3. Untuk mencari t ketika N=1, gunakan logaritma: t = t_half * log(N0) / log(2)
# IMPLEMENTASIKAN:
print("\n[Ex 5] Waktu Paruh (Half-life): N(t) = N0 * (1/2)^(t/t_half)")
# TODO: Hitung peluruhan zat untuk t=0, 5, 10, 15, 20 dan temukan kapan sisa = 1
pass

print("\n[Selesai]")
