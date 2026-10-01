"""
Exercises: Number Systems (Sistem Bilangan)
Phase 1 — Topic 1.1

Petunjuk:
  1. Baca setiap soal dengan seksama
  2. Implementasikan fungsimu sendiri di bawah setiap soal
  3. Jalankan file untuk melihat hasilnya
  4. Jika sudah selesai → bandingkan dengan exercises_solution.py
"""
import math
import fractions

print("=" * 60)
print("LATIHAN 1.1 — SISTEM BILANGAN")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# [Ex 1] KLASIFIKASI BILANGAN
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Hierarki sistem bilangan:
#   N (asli) ⊂ W (cacah) ⊂ Z (bulat) ⊂ Q (rasional) ⊂ R (real) ⊂ C (kompleks)
#   Irasional (√2, π, e) ⊂ R tapi BUKAN ∈ Q
#
# LANGKAH:
#   1. -7 → negatif, jadi bukan N/W. Masuk Z, Q (bisa ditulis -7/1), R, C
#   2. 0 → masuk W, Z, Q, R, C
#   3. 3/4 → bukan bilangan bulat, jadi Q, R, C
#   4. √5 → irasional (tidak bisa ditulis p/q), masuk R dan C saja
#   5. 2+3i → bilangan kompleks, C saja
#   6. -3/1 = -3 → sama dengan -7, masuk Z, Q, R, C
#
# IMPLEMENTASIKAN:
print("\n[Ex 1] Klasifikasikan bilangan berikut (N, W, Z, Q, Irasional, C):")
print("  a) -7    b) 0    c) 3/4    d) √5    e) 2+3i    f) -3/1")

# TODO: print klasifikasi masing-masing bilangan, contoh:
# print("  -7  ∈ Z, Q, R, C")
# print("  0   ∈ W, Z, Q, R, C")
# ... dst untuk semua 6 bilangan

# Jawaban: -7∈Z,Q,R,C | 0∈W,Z,Q,R,C | 3/4∈Q,R,C | √5∈Irasional,R,C | 2+3i∈C | -3/1∈Z,Q,R,C


# ─────────────────────────────────────────────────────────────
# [Ex 2] DESIMAL BERULANG KE PECAHAN
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Setiap desimal berulang adalah bilangan RASIONAL (dapat ditulis p/q).
#   Trik: kalikan dengan 10^n agar bagian berulang sejajar, lalu kurangi.
#
# LANGKAH untuk 0.666...:
#   Misalkan x = 0.666...
#   10x = 6.666...
#   10x - x = 6.666... - 0.666... = 6
#   9x = 6  →  x = 6/9 = 2/3
#
# LANGKAH untuk 0.272727...:
#   x = 0.272727...
#   100x = 27.272727...
#   99x = 27  →  x = 27/99 = 3/11
#
# LANGKAH untuk 0.58333...:
#   Bagian tidak berulang: 5 (1 digit), bagian berulang: 3 (1 digit)
#   10x = 5.8333...  → 100x = 58.333...
#   90x = 53  →  x = 53/90
#
# IMPLEMENTASIKAN:
print("\n[Ex 2] Ubah desimal berulang ke pecahan:")
print("  a) 0.666...    b) 0.272727...    c) 0.583333...")

# TODO: hitung setiap pecahan menggunakan class fractions.Fraction
# dan cetak hasilnya dalam bentuk: "a) 0.666... = 2/3 = 0.666667"
# Gunakan fractions.Fraction(pembilang, penyebut) untuk menyederhanakan otomatis

# Jawaban: a) 2/3  b) 3/11  c) 53/90


# ─────────────────────────────────────────────────────────────
# [Ex 3] OPERASI BILANGAN KOMPLEKS
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   z = a + bi, dimana i² = -1
#   Penjumlahan: (a+bi)+(c+di) = (a+c) + (b+d)i
#   Perkalian:   (a+bi)(c+di) = (ac-bd) + (ad+bc)i
#   Modulus:     |z| = √(a² + b²)
#   Pembagian:   kalikan pembilang dan penyebut dengan KONJUGAT (a-bi)
#
# LANGKAH untuk z1/z2 dimana z1=4+3i, z2=2-i:
#   z1/z2 = (4+3i)/(2-i) × (2+i)/(2+i)
#         = (4+3i)(2+i) / (4+1)
#         = (8+4i+6i+3i²) / 5
#         = (8-3 + 10i) / 5
#         = 5/5 + 10i/5 = 1 + 2i
#
# IMPLEMENTASIKAN:
print("\n[Ex 3] Hitung operasi kompleks: z1=4+3i, z2=2-i")
z1 = complex(4, 3)
z2 = complex(2, -1)
# TODO: hitung dan cetak:
# a) z1 + z2
# b) z1 × z2
# c) |z1|
# d) z1 / z2 dalam bentuk a+bi

# Jawaban: a) 6+2i  b) 11+2i  c) 5.0  d) 1+2i


# ─────────────────────────────────────────────────────────────
# [Ex 4] KEANGGOTAAN INTERVAL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Notasi interval:
#   [a,b]  = tertutup: a ≤ x ≤ b  (titik ujung TERMASUK)
#   (a,b)  = terbuka:  a < x < b  (titik ujung TIDAK termasuk)
#   [a,b)  = setengah terbuka: a ≤ x < b
#
# LANGKAH untuk x=4:
#   [2,4] : cek 2 <= 4 <= 4  → True
#   (2,4) : cek 2 < 4 < 4   → False (4 tidak < 4)
#   [4,7) : cek 4 <= 4 < 7  → True
#   (4,7] : cek 4 < 4 <= 7  → False (4 tidak > 4)
#
# IMPLEMENTASIKAN:
print("\n[Ex 4] Apakah x=4 ada di interval: [2,4]  (2,4)  [4,7)  (4,7]?")
x = 4
# TODO: cek setiap interval dengan ekspresi boolean Python dan cetak hasilnya
# Contoh: print(f"  [2,4] : {2 <= x <= 4}")

# Jawaban: [2,4]=True  (2,4)=False  [4,7)=True  (4,7]=False


# ─────────────────────────────────────────────────────────────
# [Ex 5] FLOOR DAN CEILING
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   ⌊x⌋ (floor)   = bilangan bulat terbesar ≤ x
#   ⌈x⌉ (ceiling) = bilangan bulat terkecil ≥ x
#   Hati-hati untuk bilangan NEGATIF:
#   ⌊-1.2⌋ = -2 (bukan -1!)   ⌈-1.2⌉ = -1
#
# LANGKAH:
#   Gunakan math.floor(x) dan math.ceil(x)
#
# IMPLEMENTASIKAN:
print("\n[Ex 5] Hitung ⌊x⌋ dan ⌈x⌉:")
values = [2.9, -1.2, 5.0, -3.0]
# TODO: loop values, cetak floor dan ceiling setiap nilai
# Contoh format: "x =  2.9: ⌊x⌋ =  2, ⌈x⌉ =  3"

# Jawaban: 2.9→(2,3)  -1.2→(-2,-1)  5.0→(5,5)  -3.0→(-3,-3)


# ─────────────────────────────────────────────────────────────
# [Ex 6] SIFAT KLOSURE (CLOSURE)
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Himpunan S "tertutup" terhadap operasi ○ jika:
#   untuk SEMUA a,b ∈ S → a ○ b ∈ S (hasilnya masih di S)
#   Untuk MENYANGKAL: cukup temukan SATU contoh penyangkal!
#
# LANGKAH:
#   a) N tertutup terhadap -? Coba 2-5=-3 → bukan N → FALSE
#   b) Z tertutup terhadap ×? Bulat×Bulat=Bulat selalu → TRUE
#   c) Q tertutup terhadap ÷? p/q ÷ r/s = ps/qr ∈ Q (asal r≠0) → TRUE
#   d) Irasional tertutup ×? √2 × √2 = 2 (rasional!) → FALSE
#
# IMPLEMENTASIKAN:
print("\n[Ex 6] Sifat klosure (True/False + contoh):")
print("  a) N tertutup terhadap pengurangan?")
print("  b) Z tertutup terhadap perkalian?")
print("  c) Q tertutup terhadap pembagian?")
print("  d) Irasional tertutup terhadap perkalian?")
# TODO: untuk setiap kasus, cetak jawaban True/False beserta contoh penyangkal/pembuktian

# Jawaban: a)FALSE(2-5=-3∉N)  b)TRUE  c)TRUE  d)FALSE(√2×√2=2∈Q)

print("\n[Selesai] Bandingkan dengan exercises_solution.py setelah selesai!")
