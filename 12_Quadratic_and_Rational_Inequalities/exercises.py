"""
Exercises: Quadratic & Rational Inequalities  |  Phase 1 — Topic 1.17
"""
import math
print("LATIHAN 1.17 — PERTIDAKSAMAAN KUADRAT & RASIONAL")
print("=" * 55)

# Ex 1: Quadratic
# KONSEP: Pertidaksamaan kuadrat diselesaikan dengan mencari akar-akar persamaan kuadrat,
# lalu menggunakan sign chart (garis bilangan) atau parabola untuk menentukan interval solusi.
# LANGKAH:
# 1. Cari akar-akar persamaan kuadrat
# 2. Buat garis bilangan dan uji tanda pada setiap interval
# 3. Pilih interval yang memenuhi pertidaksamaan
# IMPLEMENTASIKAN:
print("\n[Ex 1] Selesaikan pertidaksamaan kuadrat:")
def check_interval(f, a, b, n=20):
    pass # TODO: Implementasikan verifikasi interval

# TODO: Selesaikan x²-7x+12 > 0, x²+x-6 ≤ 0, 2x²-3x-2 > 0

# Ex 2: Rational
# KONSEP: Pertidaksamaan rasional melibatkan pembilang dan penyebut. Titik kritis adalah pembuat nol pembilang dan penyebut.
# LANGKAH:
# 1. Jadikan ruas kanan nol
# 2. Samakan penyebut
# 3. Cari pembuat nol pembilang dan penyebut
# 4. Uji tanda pada garis bilangan (ingat penyebut tidak boleh nol)
# IMPLEMENTASIKAN:
print("\n[Ex 2] Selesaikan pertidaksamaan rasional:")
# TODO: Selesaikan (x+3)/(x-2) ≥ 0, (x²-9)/(x+1) < 0, 1/(x-1) > 1/(x+1)

# Ex 3: Domain finding using inequalities
# KONSEP: Domain fungsi akar adalah nilai di mana fungsi di dalam akar ≥ 0, dan penyebut pecahan tidak boleh nol.
# LANGKAH:
# 1. Tuliskan syarat di dalam akar ≥ 0
# 2. Faktorkan dan cari titik kritis
# 3. Tentukan interval yang memenuhi (dengan syarat penyebut ≠ 0)
# IMPLEMENTASIKAN:
print("\n[Ex 3] Tentukan domain fungsi (dengan pertidaksamaan):")
print("  f(x) = √((x²-5x+6)/(x-4))")
# TODO: Implementasikan pencarian domain

# Ex 4: Application
# KONSEP: Model matematika peluru menggunakan persamaan gerak parabola. 
# LANGKAH:
# 1. Tuliskan pertidaksamaan h(t) ≥ 100
# 2. Susun menjadi pertidaksamaan kuadrat at² + bt + c ≤ 0
# 3. Gunakan rumus ABC untuk mencari batas waktu
# IMPLEMENTASIKAN:
print("\n[Ex 4] Soal Nyata:")
print("  Sebuah peluru ditembakkan vertikal: h(t) = -5t²+50t")
# TODO: Kapan peluru di ketinggian ≥ 100m? Cari batas t1 dan t2

print("\n[Selesai]")
