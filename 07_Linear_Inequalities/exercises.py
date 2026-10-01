"""
Exercises: Linear Inequalities  |  Phase 1 — Topic 1.5
"""
print("LATIHAN 1.5 — PERTIDAKSAMAAN LINEAR")
print("=" * 50)

# KONSEP:
# Saat mengalikan atau membagi kedua sisi pertidaksamaan dengan bilangan NEGATIF,
# arah tanda ketidaksamaan HARUS DIBALIK.
# LANGKAH:
# 1. Gunakan dictionary atau pemetaan untuk membalik arah operator (contoh '<' -> '>').
# IMPLEMENTASIKAN:
def flip_op(op):
    # TODO: Kembalikan kebalikan dari operator string yang masuk.
    pass

# Ex 1
print("\n[Ex 1] Selesaikan pertidaksamaan:")
# KONSEP:
# Operasi pemecahan aljabar konvensional untuk mengisolasi variabel x.
# LANGKAH:
# 1. Untuk -2x + 4 <= 10 -> -2x <= 6 -> x >= -3 (tanda dibalik).
# IMPLEMENTASIKAN:
# TODO: Selesaikan: "3x - 7 > 8", "-2x + 4 <= 10", "5x + 3 < 3", "x/4 >= -2" dan cetak jawabannya.
pass

# Ex 2 — compound
print("\n[Ex 2] Compound inequalities:")
print("  -3 < 2x+1 < 9")
# KONSEP:
# Pertidaksamaan ganda bisa diselesaikan serentak ke tiga bagiannya.
# LANGKAH:
# 1. Kurangi 1 dari ketiga sisi (-4 < 2x < 8).
# 2. Bagi dua pada ketiga sisi (-2 < x < 4).
# IMPLEMENTASIKAN:
# TODO: Cetak penyelesaian dari inequality di atas dan periksa kebenaran dengan x=0 dan x=-3.
pass

# Ex 3 — absolute value
print("\n[Ex 3] Pertidaksamaan nilai mutlak:")
print("  |2x - 3| <= 5")
# KONSEP:
# |A| <= B ekuivalen dengan -B <= A <= B.
# LANGKAH:
# 1. Konversi ke bentuk -5 <= 2x-3 <= 5.
# 2. Selesaikan pertidaksamaan ganda seperti biasa.
# IMPLEMENTASIKAN:
# TODO: Selesaikan nilai x. Lakukan loop melalui range nilai dan verifikasi ke dalam pertidaksamaan absolut.
pass

# Ex 4 — real world
print("\n[Ex 4] Soal nyata:")
print("  Toko memberikan diskon jika total belanja > 200.000.")
print("  Harga barang Rp 45.000 per item. Berapa minimum item?")
# KONSEP:
# Persoalan real dengan pertidaksamaan: 45000 * n > 200000. Variabel jumlah item/n pastilah bilangan bulat.
# LANGKAH:
# 1. Isolasi n: n > 200000 / 45000.
# 2. Lakukan pembulatan ke atas (ceiling) atau ambil bilangan bulat pertama lebih besar dari hasil pembagian.
# IMPLEMENTASIKAN:
# import math
# TODO: Selesaikan n dan cetak total minimum item.
pass

print("\n[Selesai]")
