"""
Exercises: Binomial Theorem  |  Phase 1 — Topic 1.19

Petunjuk: Implementasikan fungsi C(n,k) terlebih dahulu, lalu kerjakan setiap soal.
"""
import math
print("LATIHAN 1.19 — TEOREMA BINOMIAL")
print("=" * 50)

# ─────────────────────────────────────────────────────────────
# FUNGSI BANTU — Koefisien Binomial C(n,k)
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   C(n,k) = n! / (k! × (n-k)!) = "n pilih k"
#   Ini adalah banyaknya cara memilih k elemen dari n elemen.
#
# LANGKAH (tanpa factorial untuk efisiensi):
#   1. Jika k < 0 atau k > n: return 0 (tidak valid)
#   2. Gunakan simetri: k = min(k, n-k)  ← kurangi iterasi
#   3. Loop dari i=0 sampai k-1:
#      r = r * (n - i) // (i + 1)
#   4. Return r
#
# IMPLEMENTASIKAN:
def C(n, k):
    """Hitung koefisien binomial C(n,k) = n! / (k!(n-k)!)."""
    # TODO: implementasikan dengan loop (tanpa factorial agar efisien)
    pass

# ─────────────────────────────────────────────────────────────
# [Ex 1] BARIS PASCAL
# ─────────────────────────────────────────────────────────────
# KONSEP: Baris ke-n Segitiga Pascal adalah [C(n,0), C(n,1), ..., C(n,n)].
#         Jumlah semua elemen baris ke-n = 2^n.
# LANGKAH:
#   1. Buat list [C(7,k) for k in range(8)]
#   2. Cetak baris dan jumlahnya
# IMPLEMENTASIKAN:
print("\n[Ex 1] Tulis baris ke-7 Segitiga Pascal:")
# TODO: buat dan cetak baris ke-7 serta jumlahnya
# Jawaban: [1,7,21,35,35,21,7,1], jumlah=128=2^7

# ─────────────────────────────────────────────────────────────
# [Ex 2] EKSPANSI BINOMIAL
# ─────────────────────────────────────────────────────────────
# KONSEP: (x+y)^n = Σ C(n,k) × x^(n-k) × y^k, untuk k=0 sampai n.
# LANGKAH untuk (x+y)^5:
#   1. Loop k dari 0 sampai 5
#   2. Tiap suku: C(5,k) × x^(5-k) × y^k
#   3. Format sebagai string label (misal "21x^2y^3")
# LANGKAH untuk (2x-3)^4:
#   1. a=2x, b=-3, n=4
#   2. Suku ke-k: C(4,k) × (2)^(4-k) × (-3)^k × x^(4-k)
#   3. Hitung dan cetak koefisien tiap suku
# IMPLEMENTASIKAN:
print("\n[Ex 2] Ekspansi:")
print("  (x+y)^5:")
# TODO: cetak semua suku ekspansi (x+y)^5
# Jawaban: x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5

print("  (2x-3)^4:")
# TODO: cetak koefisien setiap suku (k=0..4) dari (2x-3)^4
# Jawaban k=0: 16x^4, k=1: -96x^3, k=2: 216x^2, k=3: -216x, k=4: 81

# ─────────────────────────────────────────────────────────────
# [Ex 3] CARI SUKU SPESIFIK
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Suku ke-(k+1) dari (a+b)^n: T_{k+1} = C(n,k) × a^(n-k) × b^k
#   "Suku bebas x" berarti pangkat x = 0.
#
# LANGKAH untuk (3x - 1/x)^6, cari suku bebas x:
#   1. T_{k+1} = C(6,k) × (3x)^(6-k) × (-1/x)^k
#   2. Pangkat x = (6-k) - k = 6 - 2k
#   3. Suku bebas x: 6 - 2k = 0 → k = 3
#   4. Hitung koefisiennya: C(6,3) × 3^3 × (-1)^3
#
# IMPLEMENTASIKAN:
print("\n[Ex 3] Temukan suku spesifik:")
print("  Dalam (3x - 1/x)^6, temukan suku yang tidak memuat x:")
# TODO: hitung k yang membuat pangkat x = 0, lalu hitung koefisiennya
# Jawaban: k=3, koefisien = C(6,3)×27×(-1) = 20×27×(-1) = -540

# ─────────────────────────────────────────────────────────────
# [Ex 4] APROKSIMASI BINOMIAL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   (1+x)^n ≈ 1 + nx + C(n,2)x² + ...  untuk x kecil.
#   Makin banyak suku yang diambil, makin akurat.
#
# LANGKAH untuk (1.02)^8:
#   1. Tulis x=0.02, n=8
#   2. Aproksimasi orde 1: 1 + 8×0.02
#   3. Aproksimasi orde 2: tambahkan C(8,2)×0.02²
#   4. Nilai exact: 1.02^8 (gunakan Python)
#   5. Hitung error persentase: |aprox - exact| / exact × 100%
#
# IMPLEMENTASIKAN:
print("\n[Ex 4] Gunakan aproksimasi binomial:")
print("  (1.02)^8 ≈ ? (gunakan orde 1 dan orde 2)")
# TODO: hitung exact, approx1, approx2, dan error keduanya
# Jawaban: exact≈1.171659, approx1=1.16, approx2=1.1708, error1≈0.9979%

# ─────────────────────────────────────────────────────────────
# [Ex 5] PROBABILITAS BINOMIAL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Distribusi Binomial: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
#   P(X≥m) = Σ P(X=k) untuk k dari m sampai n
#
# LANGKAH untuk ujian 20 soal, P(benar)=0.7, cari P(X≥15):
#   1. Loop k dari 15 sampai 20
#   2. Tiap k: tambahkan C(20,k) × (0.7)^k × (0.3)^(20-k) ke total
#   3. Cetak hasil dalam persen
#
# IMPLEMENTASIKAN:
print("\n[Ex 5] Probabilitas: ujian 20 soal, P(benar)=0.7, P(≥15 benar)?")
n, p = 20, 0.7
# TODO: hitung P(X≥15) menggunakan distribusi binomial
# Jawaban: P(X≥15) ≈ 0.415839 = 41.58%

print("\n[Selesai]")
