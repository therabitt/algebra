"""
Challenge: Sequences and Series  |  Phase 1 — Topic 1.12

Petunjuk: Soal-soal ini lebih kompleks. Baca ALGORITMA dan LANGKAH dengan teliti sebelum implementasi.
"""
import math
print("CHALLENGE 1.12 — BARISAN DAN DERET")

# ─────────────────────────────────────────────────────────────
# [Ch1] FIBONACCI O(log n) dengan Matrix Exponentiation
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   F(n) dapat dihitung dalam O(log n) menggunakan perkalian matriks.
#   Hubungan kunci: [[F(n+1), F(n)], [F(n), F(n-1)]] = [[1,1],[1,0]]^n
#   Sehingga F(n) = (M^n)[0][1] di mana M = [[1,1],[1,0]]
#
# ALGORITMA: Fast Exponentiation by Squaring
#   - Jika n=1: return M
#   - Jika n genap: M^n = (M^(n/2))²  — separuh kerja, lalu kuadratkan
#   - Jika n ganjil: M^n = M × M^(n-1) — pangkat 1 lebih kecil
#   Kompleksitas: O(log n) vs O(n) iteratif
#
# LANGKAH mat_mul(A, B) — perkalian 2 matriks 2×2:
#   1. Elemen [0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
#   2. Elemen [0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
#   3. Elemen [1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
#   4. Elemen [1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
#   5. Return list 2D 2×2
#
# IMPLEMENTASIKAN:
print("\n[Ch1] Fibonacci O(log n) dengan Matrix Exponentiation")

def mat_mul(A, B):
    """Perkalian dua matriks 2×2. Return matriks [[a,b],[c,d]]."""
    # TODO: hitung keempat elemen dan return sebagai list 2D
    pass

def mat_pow(M, n):
    """
    Pangkatkan matriks 2×2 M sebesar n menggunakan fast exponentiation.
    Kasus dasar n==1, lalu rekursi genap/ganjil.
    """
    # TODO:
    # if n == 1: return M
    # if n % 2 == 0: half = mat_pow(M, n//2); return mat_mul(half, half)
    # return mat_mul(M, mat_pow(M, n-1))
    pass

def fib_matrix(n):
    """Hitung F(n) menggunakan matrix exponentiation."""
    if n == 0:
        return 0
    M = [[1, 1], [1, 0]]
    # TODO: pangkatkan M sebesar n, kembalikan elemen [0][1]
    pass

def fib_iter(n):
    """Verifikasi: F(n) dengan cara iteratif O(n)."""
    # TODO: implementasikan versi iteratif sebagai pembanding
    pass

# TODO: uji untuk n = [10, 50, 100, 1000], bandingkan kedua metode
# Format: "F(n): matrix=X, iteratif=X, sama=True"
# Jawaban: F(10)=55, F(50)=12586269025, F(100)=354224848179261915075

# ─────────────────────────────────────────────────────────────
# [Ch2] PARADOKS ZENO — Deret Geometrika Tak Hingga
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Paradoks Zeno: Achilles (10 m/s) mengejar kura-kura yang 10m di depan (5 m/s).
#   Setiap kali Achilles menutup jarak, kura-kura maju setengahnya → deret tak hingga.
#   Jumlahnya KONVERGEN — ini membuktikan paradoks Zeno salah!
#
# LANGKAH:
#   1. Mulai: gap=10m, v_achilles=10, v_kura=5
#   2. Setiap langkah: t = gap / (v_achilles - v_kura)
#   3. total_time += t, gap /= 2
#   4. Ulangi 10 langkah, cetak tabel Step | Gap | Total Time
#   5. Cetak total teoritis: S∞ = gap0 / (v_achilles - v_kura) = 10/5 = 2 detik
#
# IMPLEMENTASIKAN:
print("\n[Ch2] Paradoks Zeno — Deret Geometrika Tak Hingga")
print("  Achilles lari, kura-kura start 10m di depan, kecepatan kura = setengah Achilles")
# TODO: simulasikan 10 langkah Zeno, cetak tabel
# TODO: cetak total waktu teoritis (S∞)
# Jawaban: konvergen ke 2.0 detik

# ─────────────────────────────────────────────────────────────
# [Ch3] UJI KONVERGENSI DERET
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   - Harmonic series Σ1/n → DIVERGEN (walaupun setiap suku mengecil)
#   - Basel problem Σ1/n² → KONVERGEN ke π²/6 (ditemukan Euler 1734)
#
# LANGKAH untuk Harmonic (Σ1/n, n=1..1000):
#   1. Inisialisasi s = 0
#   2. Loop n dari 1 sampai 1000: s += 1/n
#   3. Cetak hasilnya (nilainya masih kecil padahal sudah 1000 suku → divergen)
#
# LANGKAH untuk Basel (Σ1/n², n=1..10000):
#   1. Jumlahkan 1/n² untuk n dari 1 sampai 10000
#   2. Bandingkan dengan math.pi**2/6
#   3. Hitung selisih (error)
#
# IMPLEMENTASIKAN:
print("\n[Ch3] Uji Konvergensi Deret")
# TODO: hitung harmonic series Σ1/n untuk n=1..1000, cetak hasilnya
# Jawaban: ≈ 7.485471

# TODO: hitung Basel problem Σ1/n² untuk n=1..10000, bandingkan dengan π²/6
# Jawaban: Σ1/n² ≈ 1.64483407, π²/6 ≈ 1.64493407, error ≈ 1.00e-4

print("\n[Selesai Challenge 1.12]")


