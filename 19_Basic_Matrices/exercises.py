"""
Exercises: Basic Matrices  |  Phase 1 — Topic 1.13

Petunjuk: Implementasikan semua fungsi helper dulu, lalu kerjakan setiap soal.
"""
print("LATIHAN 1.13 — MATRIKS DASAR")
print("=" * 50)

# ─────────────────────────────────────────────────────────────
# FUNGSI BANTU — Implementasikan semua fungsi ini terlebih dahulu!
# ─────────────────────────────────────────────────────────────

# KONSEP: Penjumlahan matriks: (A+B)[i][j] = A[i][j] + B[i][j]
# LANGKAH:
#   1. Loop baris i dari 0 sampai len(A)-1
#   2. Loop kolom j dari 0 sampai len(A[0])-1
#   3. Hasilkan list 2D baru dengan elemen A[i][j] + B[i][j]
def mat_add(A, B):
    # TODO: kembalikan matriks hasil penjumlahan A + B
    pass

# KONSEP: Perkalian matriks: (A×B)[i][j] = Σ A[i][k] × B[k][j]
# LANGKAH:
#   1. Dapatkan dimensi: m=baris A, n=kolom A=baris B, p=kolom B
#   2. Triple loop: i (baris A), j (kolom B), k (elemen dot product)
#   3. Hasil[i][j] = sum(A[i][k]*B[k][j] for k in range(n))
def mat_mul(A, B):
    # TODO: kembalikan matriks hasil perkalian A × B
    pass

# KONSEP: Transpos: mengubah baris menjadi kolom, A^T[i][j] = A[j][i]
# LANGKAH:
#   1. Buat matriks baru dengan dimensi terbalik
#   2. Hasil[i][j] = A[j][i]
def transpose(A):
    # TODO: kembalikan transpos dari A
    pass

# KONSEP: Determinan matriks 2×2: det([[a,b],[c,d]]) = ad - bc
def det2(A):
    # TODO: kembalikan ad - bc
    pass

# KONSEP: Invers matriks 2×2: A^(-1) = (1/det) × [[d,-b],[-c,a]]
# LANGKAH:
#   1. Hitung det = det2(A)
#   2. Jika |det| < 1e-12: matriks singular, return None
#   3. Kembalikan [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]
def inv2(A):
    # TODO: kembalikan invers atau None jika singular
    pass

# Helper display (sudah jadi — jangan ubah)
def show(A, label=""):
    if label: print(f"  {label}:")
    for row in A:
        print("   ", row)


# ─────────────────────────────────────────────────────────────
# [Ex 1] OPERASI DASAR MATRIKS
# ─────────────────────────────────────────────────────────────
# KONSEP: Penjumlahan, pengurangan (A-B = A + (-B)), perkalian skalar, transpos.
# LANGKAH:
#   1. Gunakan mat_add(A, B) untuk A+B
#   2. Buat A-B dengan list comprehension: A[i][j] - B[i][j]
#   3. Buat 2A dengan list comprehension: 2*A[i][j]
#   4. Gunakan transpose(A) untuk transpos
# IMPLEMENTASIKAN:
print("\n[Ex 1] Hitung A+B, A-B, 2A, A^T")
A = [[1,2,3],[4,5,6]]
B = [[7,8,9],[1,2,3]]
# TODO: hitung dan tampilkan A+B, A-B, 2A, dan transpos(A)
# Jawaban A+B: [[8,10,12],[5,7,9]]

# ─────────────────────────────────────────────────────────────
# [Ex 2] PERKALIAN MATRIKS
# ─────────────────────────────────────────────────────────────
# KONSEP: Perkalian matriks TIDAK komutatif: P×Q ≠ Q×P (umumnya).
# LANGKAH:
#   1. Hitung P×Q dan Q×P menggunakan mat_mul
#   2. Bandingkan apakah hasilnya sama
# IMPLEMENTASIKAN:
print("\n[Ex 2] Kalikan matriks")
P = [[1,2],[3,4]]
Q = [[5,0],[1,3]]
# TODO: hitung PQ, QP, dan tunjukkan apakah PQ == QP
# Jawaban PQ: [[7,6],[19,12]], QP: [[5,10],[10,14]]

# ─────────────────────────────────────────────────────────────
# [Ex 3] DETERMINAN
# ─────────────────────────────────────────────────────────────
# KONSEP: det([[a,b],[c,d]]) = ad - bc. Jika det=0, matriks singular.
# IMPLEMENTASIKAN:
print("\n[Ex 3] Hitung determinan:")
matrices = [
    ([[3,2],[1,4]], "3  2 / 1  4"),
    ([[-1,5],[2,-3]], "-1  5 / 2  -3"),
    ([[0,1],[0,2]], "0  1 / 0  2"),
]
for M, label in matrices:
    # TODO: hitung det2(M) dan cetak hasilnya
    # Jawaban: 10, -7, 0 (singular!)
    pass

# ─────────────────────────────────────────────────────────────
# [Ex 4] INVERS MATRIKS
# ─────────────────────────────────────────────────────────────
# KONSEP: A × A^(-1) = I (matriks identitas). Hanya ada jika det ≠ 0.
# LANGKAH:
#   1. Gunakan inv2(M) untuk menghitung invers
#   2. Verifikasi: M × M^(-1) harus menghasilkan matriks identitas
# IMPLEMENTASIKAN:
print("\n[Ex 4] Hitung invers (jika ada):")
for M, label in [([[2,1],[5,3]],"A"), ([[4,2],[2,1]],"B")]:
    # TODO: hitung invers, cetak, dan verifikasi M × inv = I
    # Jawaban A: inv=[[3,-1],[-5,2]], B: singular!
    pass

# ─────────────────────────────────────────────────────────────
# [Ex 5] SELESAIKAN SISTEM DENGAN INVERS MATRIKS
# ─────────────────────────────────────────────────────────────
# KONSEP: Ax = b → x = A^(-1) × b
# LANGKAH:
#   1. Bentuk matriks A dari koefisien sistem
#   2. Hitung inv2(A)
#   3. Kalikan inv_A dengan vektor b: x[i] = sum(inv_A[i][j]*b[j] for j)
# IMPLEMENTASIKAN:
print("\n[Ex 5] Selesaikan sistem menggunakan matriks invers:")
print("  3x + y = 10")
print("  2x + 5y = 17")
A_sys = [[3,1],[2,5]]
b_sys = [10,17]
# TODO: cari invers A, kalikan dengan b, cetak solusi dan verifikasi
# Jawaban: x=3.0, y=1.0

# ─────────────────────────────────────────────────────────────
# [Ex 6] TRANSFORMASI 2D DENGAN MATRIKS
# ─────────────────────────────────────────────────────────────
# KONSEP: Rotasi 2D menggunakan matriks:
#   R(θ) = [[cos θ, -sin θ], [sin θ, cos θ]]
#   Titik baru = R × titik_lama
# LANGKAH:
#   1. Buat matriks rotasi R untuk θ = 45° = π/4
#   2. Terapkan ke titik (1, 0) menggunakan mat_mul
# IMPLEMENTASIKAN:
print("\n[Ex 6] Transformasi 2D menggunakan matriks")
import math
angle = math.pi/4  # 45 derajat
# TODO: buat R(45°) dan rotasikan titik [[1],[0]]
# Jawaban: (√2/2, √2/2) ≈ (0.7071, 0.7071)

print("\n[Selesai]")
