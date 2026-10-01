"""
Exercises: Sequences and Series  |  Phase 1 — Topic 1.12

Petunjuk: Baca KONSEP dan LANGKAH di setiap soal, lalu implementasikan di bagian TODO.
"""
import math
print("LATIHAN 1.12 — BARISAN DAN DERET")
print("=" * 50)

# ─────────────────────────────────────────────────────────────
# FUNGSI BANTU — Implementasikan fungsi-fungsi ini terlebih dahulu!
# ─────────────────────────────────────────────────────────────

# KONSEP: Suku ke-n barisan aritmetika: a_n = a1 + (n-1)*d
# LANGKAH:
#   1. Terima parameter a1 (suku pertama), d (beda), n (indeks)
#   2. Kembalikan a1 + (n-1)*d
def arith_nth(a1, d, n):
    # TODO: kembalikan suku ke-n barisan aritmetika
    pass

# KONSEP: Jumlah n suku barisan aritmetika: Sn = n/2 * (a1 + an)
# LANGKAH:
#   1. Hitung an menggunakan arith_nth
#   2. Kembalikan n * (a1 + an) / 2
def arith_sum(a1, d, n):
    # TODO: hitung dan kembalikan jumlah n suku
    pass

# KONSEP: Suku ke-n barisan geometrika: a_n = a1 * r^(n-1)
def geo_nth(a1, r, n):
    # TODO: kembalikan suku ke-n barisan geometrika
    pass

# KONSEP: Jumlah n suku barisan geometrika: Sn = a1*(1-r^n)/(1-r)
# LANGKAH:
#   1. Jika r ≈ 1 (beda sangat kecil), gunakan: Sn = a1 * n
#   2. Jika r ≠ 1, gunakan: Sn = a1*(1-r^n)/(1-r)
def geo_sum(a1, r, n):
    # TODO: kembalikan jumlah n suku
    pass

# KONSEP: Jumlah tak hingga: S∞ = a1/(1-r), hanya konvergen jika |r| < 1
# LANGKAH:
#   1. Cek apakah |r| < 1
#   2. Jika ya: return a1/(1-r)
#   3. Jika tidak: return float("inf")
def geo_inf(a1, r):
    # TODO: kembalikan jumlah tak hingga atau inf
    pass


# [Ex 1] BARISAN ARITMETIKA
# LANGKAH: Gunakan arith_nth dan arith_sum yang sudah kamu buat.
print("\n[Ex 1] Barisan aritmetika: a1=7, d=4")
a1, d = 7, 4
# TODO: cetak suku ke-15, jumlah 20 suku, dan 10 suku pertama
# Jawaban: suku ke-15=63, jumlah 20 suku=900, 10 suku: [7,11,15,19,23,27,31,35,39,43]

# [Ex 2] BARISAN GEOMETRIKA
# LANGKAH: Gunakan geo_nth dan geo_sum.
print("\n[Ex 2] Barisan geometrika: a1=3, r=2")
a1, r = 3, 2
# TODO: cetak suku ke-8 dan jumlah 8 suku
# Jawaban: suku ke-8=384, jumlah 8 suku=765.00

# [Ex 3] DERET TAK HINGGA
# KONSEP: Deret geometrika konvergen jika |r| < 1. S∞ = a1/(1-r).
print("\n[Ex 3] Deret tak hingga: a1=12, r=1/3")
# TODO: hitung S∞ menggunakan geo_inf
# Jawaban: S∞ = 18.000000

# [Ex 4] CARI JUMLAH SUKU DAN TOTAL DERET
# KONSEP: Jika suku terakhir diketahui, cari n dulu baru hitung jumlah.
# LANGKAH:
#   1. Dari rumus an = a1 + (n-1)*d → n = (an - a1) / d + 1
#   2. Hitung jumlah menggunakan arith_sum
print("\n[Ex 4] Cari suku tengah dan jumlah:")
print("  Barisan: 5, 8, 11, 14, ..., 50")
a1, d = 5, 3
# TODO: hitung n dan total jumlah
# Jawaban: n=16, jumlah=440

# [Ex 5] BARISAN FIBONACCI
# KONSEP: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). Setiap suku = jumlah dua sebelumnya.
# LANGKAH:
#   1. Mulai dengan a=0, b=1
#   2. Iterasi n kali: lakukan (a, b) = (b, a+b)
#   3. Kembalikan a
print("\n[Ex 5] Barisan Fibonacci")

def fib(n):
    """Kembalikan bilangan Fibonacci ke-n secara iteratif."""
    # TODO: implementasikan dengan loop (bukan rekursi)
    pass

# TODO: buat list F(0)..F(19), cetak, dan hitung jumlah 10 pertama
# Jawaban: jumlah 10 pertama = 88

# [Ex 6] BUNGA MAJEMUK (Aplikasi Barisan Geometrika)
# KONSEP: A = P * r_bulan^n_bulan, di mana r_bulan = 1 + (bunga_tahunan/12)
# LANGKAH:
#   1. Hitung r_month = 1 + r_year/12
#   2. Untuk setiap periode: A = P * r_month^n_months
print("\n[Ex 6] Bunga Majemuk sebagai Barisan Geometrika")
P, r_year = 10_000_000, 0.06
# TODO: hitung dan cetak nilai akhir untuk 1, 2, 5, 10 tahun (12,24,60,120 bulan)
# Jawaban (1 tahun): Rp 10,616,778.12

print("\n[Selesai]")


