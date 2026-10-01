"""
Challenge: Systems of Equations  |  Phase 1 — Topic 1.7
"""
print("CHALLENGE 1.7 — SISTEM PERSAMAAN")

# Challenge 1: Full Gaussian Elimination
print("\n[Ch1] Eliminasi Gauss dari Nol")

# KONSEP:
# Eliminasi Gauss adalah metode step-by-step mentransformasikan sistem Ax = b (matriks augmented)
# menjadi bentuk baris eselon (segitiga atas) untuk memudahkan Back Substitution (substitusi mundur).
# "Partial pivoting" digunakan dengan menukar baris agar pivot selalu elemen terbesar, 
# hal ini meminimalkan error karena pembulatan numerik.

# ALGORITMA:
# 1. Buat augmented matrix: gabungan M = [A | b].
# 2. Forward Elimination (Eliminasi Maju): 
#    - Untuk setiap kolom `col` cari baris ke bawah yang absolutnya max, lalu swap baris tersebut dengan baris saat ini.
#    - Eliminasi elemen-elemen di bawah pivot agar menjadi nol dengan mengurangi baris menggunakan faktor `M[row][col] / pivot`.
# 3. Back Substitution (Substitusi Mundur):
#    - Pecahkan x[i] mulai dari baris terakhir ke atas dengan cara mengurangi M[i][n] dengan sum(M[i][j]*x[j]).

def gaussian_elimination(A, b):
    """
    Selesaikan sistem Ax = b menggunakan eliminasi Gauss dengan partial pivoting.
    """
    import copy
    # IMPLEMENTASIKAN:
    # TODO: Isi proses swap (partial pivoting), forward elimination, dan back substitution
    pass

# Test 2x2
# A2 = [[2, 3],[4,-1]]; b2 = [12, 5]
# TODO: Uji dengan Gaussian Elimination di atas, solusi = [3.0, 2.0]
pass

# Test 3x3
# A3 = [[1,1,1],[2,-1,1],[1,1,-2]]; b3 = [6,3,-3]
# TODO: Uji, dan verifikasi dengan matrix 3x3.
pass

# Challenge 2: Iterative Methods (Jacobi)
print("\n[Ch2] Metode Jacobi (Iteratif)")

# KONSEP:
# Metode Jacobi menyelesaikan persamaan kuadrat dengan mencari x^(k+1) menggunakan iterasi berdasarkan x^(k) masa lalu.
# Formula: x_i^(k+1) = (b_i - sum_{j!=i} A_ij*x_j^k) / A_ii
# Hanya akan konvergen jika A merupakan 'Diagonally Dominant Matrix'.

# ALGORITMA:
# 1. Tetapkan tebakan x awal [0.0, 0.0, ...]
# 2. Iterasikan k dari 0 ke limit.
# 3. Untuk setiap baris i, kurangi b[i] dengan hasil jumlah perkalian antara sel di luar diagonal dan tebakan sebelumnya (x_j).
# 4. Bagi hasil selisih tadi dengan A[i][i]
# 5. Cek selisih error iterasi saat ini dengan iterasi lama (apakah sudah kurang dari toleransi). Jika ya, hentikan dan konvergen.

def jacobi(A, b, x0=None, tol=1e-8, max_iter=100):
    """
    Jacobi iterative method.
    """
    # IMPLEMENTASIKAN:
    # TODO: Iterasikan, gunakan formula Jacobi dan kalkulasi galat / error, update array x secara simultan
    pass

# Diagonally dominant system
# A_jac = [[4,1,0],[1,4,1],[0,1,4]]
# b_jac = [5, 6, 5]
# TODO: Terapkan Jacobi dan perhatikan kecepatannya konvergen.
pass

print("\n[Selesai Challenge 1.7]")
