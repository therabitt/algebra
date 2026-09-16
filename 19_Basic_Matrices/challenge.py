"""
Challenge: Basic Matrices  |  Phase 1 — Topic 1.13
"""
import math
print("CHALLENGE 1.13 — MATRIKS DASAR")

# ─── Ch1: LU Decomposition ────────────────────────────────────
print("\n[Ch1] LU Decomposition (PA = LU)")
def lu_decompose(A):
    """
    Dekomposisi LU dengan partial pivoting.
    A = P·L·U di mana:
    P: permutation, L: lower triangular, U: upper triangular
    """
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    U = [list(map(float, row)) for row in A]
    P = list(range(n))

    for col in range(n):
        # Partial pivot
        max_row = max(range(col, n), key=lambda r: abs(U[r][col]))
        if max_row != col:
            U[col], U[max_row] = U[max_row], U[col]
            P[col], P[max_row] = P[max_row], P[col]
            for k in range(col):
                L[col][k], L[max_row][k] = L[max_row][k], L[col][k]

        L[col][col] = 1.0
        for row in range(col+1, n):
            if abs(U[col][col]) < 1e-12: continue
            factor = U[row][col] / U[col][col]
            L[row][col] = factor
            for k in range(col, n):
                U[row][k] -= factor * U[col][k]

    return L, U, P

A_lu = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b_lu = [8, -11, -3]
L, U, P = lu_decompose(A_lu)
print("  A = [[2,1,-1],[-3,-1,2],[-2,1,2]]")
print("  L =")
for row in L: print("   ", [round(x,4) for x in row])
print("  U =")
for row in U: print("   ", [round(x,4) for x in row])

# Solve using L and U
def forward_sub(L, b):
    n = len(b)
    y = [0.0]*n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))
        y[i] /= L[i][i]
    return y

def back_sub(U, y):
    n = len(y)
    x = [0.0]*n
    for i in range(n-1,-1,-1):
        x[i] = y[i] - sum(U[i][j]*x[j] for j in range(i+1,n))
        if abs(U[i][i]) > 1e-12:
            x[i] /= U[i][i]
    return x

b_perm = [b_lu[P[i]] for i in range(len(b_lu))]
y = forward_sub(L, b_perm)
x = back_sub(U, y)
print(f"  Solusi Ax=b: x={[round(v,4) for v in x]}")
# Verify
verify = [sum(A_lu[i][j]*x[j] for j in range(3)) for i in range(3)]
print(f"  Verifikasi Ax={[round(v,4) for v in verify]} == b={b_lu}")

# ─── Ch2: Strassen (preview) ──────────────────────────────────
print("\n[Ch2] Strassen 2×2 Matrix Multiplication")
print("  Algoritma Strassen: 7 perkalian scalar (vs 8 standar)")

def strassen_2x2(A, B):
    """
    Strassen untuk 2×2. Hemat 1 perkalian dibanding biasa.
    """
    a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]
    e,f,g,h = B[0][0],B[0][1],B[1][0],B[1][1]

    # 7 perkalian (vs 8 standar)
    m1 = (a+d)*(e+h)   # (a+d)(e+h)
    m2 = (c+d)*e       # (c+d)e
    m3 = a*(f-h)       # a(f-h)
    m4 = d*(g-e)       # d(g-e)
    m5 = (a+b)*h       # (a+b)h
    m6 = (c-a)*(e+f)   # (c-a)(e+f)
    m7 = (b-d)*(g+h)   # (b-d)(g+h)

    C = [
        [m1+m4-m5+m7, m3+m5],
        [m2+m4,       m1-m2+m3+m6]
    ]
    return C

A_s = [[1,2],[3,4]]
B_s = [[5,6],[7,8]]
C_strassen = strassen_2x2(A_s, B_s)
C_normal = [[sum(A_s[i][k]*B_s[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print(f"  Strassen: {C_strassen}")
print(f"  Normal  : {C_normal}")
print(f"  Sama? {C_strassen == C_normal}")

# ─── Ch3: Power Iteration (eigenvalue preview) ────────────────
print("\n[Ch3] Power Iteration — Eigenvalue Terbesar (preview)")

def mat_vec(A, v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def vec_norm(v):
    return math.sqrt(sum(x**2 for x in v))

def power_iteration(A, tol=1e-8, max_iter=1000):
    n = len(A)
    v = [1.0/math.sqrt(n)]*n  # initial guess
    eigenval = 0.0
    for i in range(max_iter):
        Av = mat_vec(A, v)
        norm = vec_norm(Av)
        v_new = [x/norm for x in Av]
        eigenval_new = sum(v_new[k]*Av[k] for k in range(n))
        if abs(eigenval_new - eigenval) < tol:
            return eigenval_new, v_new, i+1
        v, eigenval = v_new, eigenval_new
    return eigenval, v, max_iter

A_eig = [[4,1],[2,3]]
lam, vec, iters = power_iteration(A_eig)
print(f"  A = [[4,1],[2,3]]")
print(f"  Eigenvalue terbesar ≈ {lam:.6f} (setelah {iters} iterasi)")
print(f"  Eigenvector ≈ {[round(v,6) for v in vec]}")
print(f"  (Nilai eksak: λ=5, v=[1/√2, 1/√2]≈[{1/math.sqrt(2):.6f},{1/math.sqrt(2):.6f}])")

print("\n[Selesai Challenge 1.13]")
