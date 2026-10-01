"""
Challenge: Basic Matrices  |  Phase 1 — Topic 1.13

Petunjuk: Soal-soal ini membutuhkan pemahaman algoritma linear algebra tingkat lanjut.
"""
import math
print("CHALLENGE 1.13 — MATRIKS DASAR")

# ─────────────────────────────────────────────────────────────
# [Ch1] LU DECOMPOSITION
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Dekomposisi LU memfaktorkan A = P·L·U di mana:
#   P = matriks permutasi (pivoting), L = lower triangular, U = upper triangular
#   Berguna untuk menyelesaikan Ax=b secara efisien.
#
# ALGORITMA: Gaussian Elimination dengan Partial Pivoting
#   Untuk setiap kolom col:
#   1. Temukan baris dengan nilai absolut terbesar (partial pivot)
#   2. Tukar baris tersebut ke posisi col (update P)
#   3. Hitung faktor eliminasi: L[row][col] = U[row][col] / U[col][col]
#   4. Eliminasi: U[row][k] -= faktor × U[col][k]
#
# LANGKAH forward_sub(L, b) — selesaikan Ly=b:
#   1. Loop i dari 0 sampai n-1
#   2. y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))
#   3. y[i] /= L[i][i]
#
# LANGKAH back_sub(U, y) — selesaikan Ux=y:
#   1. Loop i dari n-1 sampai 0 (terbalik)
#   2. x[i] = y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))
#   3. x[i] /= U[i][i]
#
# IMPLEMENTASIKAN:
print("\n[Ch1] LU Decomposition (PA = LU)")

def lu_decompose(A):
    """
    Dekomposisi LU dengan partial pivoting.
    Return (L, U, P) di mana P adalah permutation list.
    """
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    U = [list(map(float, row)) for row in A]
    P = list(range(n))
    # TODO: implementasikan Gaussian elimination dengan partial pivoting
    # Untuk setiap kolom col:
    #   1. Temukan baris max_row (abs terbesar di kolom col)
    #   2. Swap U[col] dan U[max_row], swap P[col] dan P[max_row]
    #   3. Swap elemen L yang sudah diisi
    #   4. L[col][col] = 1.0
    #   5. Untuk setiap baris di bawah col: hitung faktor, update L dan U
    return L, U, P

def forward_sub(L, b):
    """Selesaikan Ly=b (forward substitution)."""
    n = len(b)
    y = [0.0]*n
    # TODO: loop maju, hitung y[i] = (b[i] - sum(L[i][j]*y[j])) / L[i][i]
    return y

def back_sub(U, y):
    """Selesaikan Ux=y (backward substitution)."""
    n = len(y)
    x = [0.0]*n
    # TODO: loop mundur, hitung x[i] = (y[i] - sum(U[i][j]*x[j])) / U[i][i]
    return x

A_lu = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b_lu = [8, -11, -3]
# TODO: dekomposisi A_lu, cetak L dan U, lalu selesaikan Ax=b
# Jawaban: x=[2.0, 3.0, -1.0]

# ─────────────────────────────────────────────────────────────
# [Ch2] STRASSEN 2×2 MATRIX MULTIPLICATION
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Algoritma Strassen mengalikan dua matriks 2×2 dengan hanya 7 perkalian scalar
#   (standar butuh 8). Ini penting untuk matriks besar secara rekursif.
#
# ALGORITMA: Strassen
#   Untuk A=[[a,b],[c,d]], B=[[e,f],[g,h]], hitung 7 "M" terlebih dahulu:
#   m1 = (a+d)(e+h)
#   m2 = (c+d)e
#   m3 = a(f-h)
#   m4 = d(g-e)
#   m5 = (a+b)h
#   m6 = (c-a)(e+f)
#   m7 = (b-d)(g+h)
#   Lalu: C = [[m1+m4-m5+m7, m3+m5], [m2+m4, m1-m2+m3+m6]]
#
# IMPLEMENTASIKAN:
print("\n[Ch2] Strassen 2×2 Matrix Multiplication")
print("  Algoritma Strassen: 7 perkalian scalar (vs 8 standar)")

def strassen_2x2(A, B):
    """Perkalian matriks 2×2 menggunakan algoritma Strassen (7 perkalian)."""
    a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]
    e,f,g,h = B[0][0],B[0][1],B[1][0],B[1][1]
    # TODO: hitung m1..m7, lalu susun matriks C menggunakan kombinasinya
    pass

A_s = [[1,2],[3,4]]
B_s = [[5,6],[7,8]]
# TODO: bandingkan hasil strassen_2x2 dengan perkalian normal
# Jawaban: [[19,22],[43,50]]

# ─────────────────────────────────────────────────────────────
# [Ch3] POWER ITERATION — Eigenvalue Terbesar
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Power iteration adalah metode iteratif untuk mencari eigenvalue terbesar.
#   Idenya: vektor acak yang berulang kali dikalikan A akan "mengarah" ke eigenvector dominan.
#
# ALGORITMA: Power Iteration
#   1. Mulai dengan vektor v = [1/√n, 1/√n, ...] (tebakan awal ternormalisasi)
#   2. Setiap iterasi:
#      a. Av = mat_vec(A, v)
#      b. norm = panjang Av (vec_norm)
#      c. v_new = Av / norm (normalisasi)
#      d. eigenval_new = dot(v_new, Av)  (Rayleigh quotient)
#      e. Jika |eigenval_new - eigenval| < tol: konvergen → stop
#      f. Update v = v_new, eigenval = eigenval_new
#
# IMPLEMENTASIKAN:
print("\n[Ch3] Power Iteration — Eigenvalue Terbesar (preview)")

def mat_vec(A, v):
    """Kalikan matriks A dengan vektor v."""
    # TODO: return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
    pass

def vec_norm(v):
    """Panjang vektor v = sqrt(sum(x^2))."""
    # TODO: kembalikan sqrt dari jumlah kuadrat elemen
    pass

def power_iteration(A, tol=1e-8, max_iter=1000):
    """Cari eigenvalue terbesar A menggunakan power iteration."""
    n = len(A)
    v = [1.0/math.sqrt(n)]*n  # tebakan awal
    eigenval = 0.0
    # TODO: implementasikan loop power iteration sesuai algoritma di atas
    # Return (eigenval, v, jumlah_iterasi)
    pass

A_eig = [[4,1],[2,3]]
# TODO: jalankan power_iteration, cetak eigenvalue dan eigenvector
# Jawaban: eigenvalue ≈ 5.0, eigenvector ≈ [0.7071, 0.7071]
# Nilai eksak: λ=5, v=[1/√2, 1/√2]

print("\n[Selesai Challenge 1.13]")
