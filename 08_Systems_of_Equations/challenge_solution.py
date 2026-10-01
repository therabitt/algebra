"""
Challenge: Systems of Equations  |  Phase 1 — Topic 1.7
"""
print("CHALLENGE 1.7 — SISTEM PERSAMAAN")

# Challenge 1: Full Gaussian Elimination
print("\n[Ch1] Eliminasi Gauss dari Nol")

def gaussian_elimination(A, b):
    """
    Selesaikan sistem Ax = b menggunakan eliminasi Gauss dengan partial pivoting.
    """
    import copy
    n = len(b)
    # Augmented matrix
    M = [list(A[i]) + [b[i]] for i in range(n)]
    
    for col in range(n):
        # Partial pivoting: cari baris dengan nilai terbesar di kolom ini
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]
        
        pivot = M[col][col]
        if abs(pivot) < 1e-12:
            return None  # Singular
        
        # Eliminasi ke bawah
        for row in range(col+1, n):
            factor = M[row][col] / pivot
            M[row] = [M[row][j] - factor * M[col][j] for j in range(n+1)]
    
    # Back substitution
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]
    
    return x

# Test 2x2
A2 = [[2, 3],[4,-1]]
b2 = [12, 5]
sol = gaussian_elimination(A2, b2)
print(f"  2x+3y=12, 4x-y=5  ->  {sol}")

# Test 3x3
A3 = [[1,1,1],[2,-1,1],[1,1,-2]]
b3 = [6,3,-3]
sol = gaussian_elimination(A3, b3)
print(f"  3x3 system  ->  x={sol[0]:.2f}, y={sol[1]:.2f}, z={sol[2]:.2f}")

# Challenge 2: Iterative Methods (Jacobi)
print("\n[Ch2] Metode Jacobi (Iteratif)")
def jacobi(A, b, x0=None, tol=1e-8, max_iter=100):
    """
    Jacobi iterative method: x_i^(k+1) = (b_i - sum_{j!=i} A_ij*x_j^k) / A_ii
    Perlu dominan diagonal: |A_ii| > sum|A_ij| untuk j!=i
    """
    n = len(b)
    x = x0 or [0.0]*n
    for k in range(max_iter):
        x_new = list(x)
        for i in range(n):
            s = sum(A[i][j]*x[j] for j in range(n) if j!=i)
            x_new[i] = (b[i] - s) / A[i][i]
        err = max(abs(x_new[i]-x[i]) for i in range(n))
        x = x_new
        if err < tol:
            print(f"  Konvergen setelah {k+1} iterasi")
            return x
    return x

# Diagonally dominant system
A_jac = [[4,1,0],[1,4,1],[0,1,4]]
b_jac = [5, 6, 5]
sol = jacobi(A_jac, b_jac)
print(f"  Jacobi solution: {[round(s,6) for s in sol]}")

print("\n[Selesai Challenge 1.7]")
