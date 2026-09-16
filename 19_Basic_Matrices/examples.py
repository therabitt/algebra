"""
Module  : Basic Matrices (Matriks Dasar)
Phase   : 1 - Algebra  |  Topic: 1.13
Jalankan: python3 examples.py
"""

print("=" * 60)
print("MATRIKS DASAR — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── Kelas Matrix dari nol ─────────────────────────────────────
class Matrix:
    """Matriks lengkap dari nol tanpa numpy."""

    def __init__(self, data):
        """data: list of lists (baris × kolom)."""
        self.data = [list(row) for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self):
        width = max(len(str(self.data[i][j]))
                    for i in range(self.rows) for j in range(self.cols))
        lines = []
        for row in self.data:
            line = "  [" + "  ".join(f"{v:{width}}" for v in row) + "]"
            lines.append(line)
        return "\n".join(lines)

    def shape(self):
        return (self.rows, self.cols)

    def __getitem__(self, idx):
        return self.data[idx]

    def __add__(self, other):
        assert self.shape() == other.shape(), "Dimensi harus sama!"
        return Matrix([[self[i][j] + other[i][j]
                        for j in range(self.cols)]
                       for i in range(self.rows)])

    def __sub__(self, other):
        assert self.shape() == other.shape(), "Dimensi harus sama!"
        return Matrix([[self[i][j] - other[i][j]
                        for j in range(self.cols)]
                       for i in range(self.rows)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self[i][j] * other
                            for j in range(self.cols)]
                           for i in range(self.rows)])
        assert self.cols == other.rows, (
            f"Kolom A ({self.cols}) harus = Baris B ({other.rows})")
        result = [[sum(self[i][k] * other[k][j]
                       for k in range(self.cols))
                   for j in range(other.cols)]
                  for i in range(self.rows)]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self[i][j] for i in range(self.rows)]
                       for j in range(self.cols)])

    def trace(self):
        assert self.rows == self.cols, "Trace hanya untuk matriks persegi!"
        return sum(self[i][i] for i in range(self.rows))

    def det2(self):
        """Determinan matriks 2×2."""
        assert self.rows == self.cols == 2
        return self[0][0]*self[1][1] - self[0][1]*self[1][0]

    def det3(self):
        """Determinan matriks 3×3 (cofactor expansion pada baris 0)."""
        assert self.rows == self.cols == 3
        a = self.data
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
              - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
              + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

    def det(self):
        """Determinan untuk matriks n×n menggunakan Gaussian elimination."""
        assert self.rows == self.cols, "Harus matriks persegi!"
        n = self.rows
        M = [list(row) for row in self.data]  # copy
        sign = 1
        for col in range(n):
            # Cari pivot
            pivot_row = None
            for row in range(col, n):
                if abs(M[row][col]) > 1e-12:
                    pivot_row = row
                    break
            if pivot_row is None:
                return 0  # Singular
            if pivot_row != col:
                M[col], M[pivot_row] = M[pivot_row], M[col]
                sign *= -1
            pivot = M[col][col]
            for row in range(col+1, n):
                factor = M[row][col] / pivot
                for k in range(col, n):
                    M[row][k] -= factor * M[col][k]
        result = sign
        for i in range(n):
            result *= M[i][i]
        return result

    def inverse2(self):
        """Invers matriks 2×2."""
        d = self.det2()
        if abs(d) < 1e-12:
            raise ValueError("Matriks singular (det=0), tidak punya invers!")
        a,b = self[0][0], self[0][1]
        c,d_ = self[1][0], self[1][1]
        return Matrix([[d_/d, -b/d], [-c/d, a/d]])

    @staticmethod
    def identity(n):
        return Matrix([[1 if i==j else 0 for j in range(n)]
                       for i in range(n)])

    @staticmethod
    def zeros(m, n):
        return Matrix([[0]*n for _ in range(m)])


# ─── 1. Membuat Matriks ───────────────────────────────────────
print("\n[1] Membuat dan Menampilkan Matriks")

A = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
B = Matrix([[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])
print(f"A =\n{A}")
print(f"\nB =\n{B}")
print(f"\nShape A: {A.shape()},  Shape B: {B.shape()}")

# ─── 2. Operasi Dasar ─────────────────────────────────────────
print("\n[2] Operasi Penjumlahan, Pengurangan, Skalar")
print(f"\nA + B =\n{A + B}")
print(f"\nA - B =\n{A - B}")
print(f"\n3 × A =\n{A * 3}")

# ─── 3. Perkalian Matriks ─────────────────────────────────────
print("\n[3] Perkalian Matriks")
P = Matrix([[1, 2], [3, 4]])
Q = Matrix([[5, 6], [7, 8]])
print(f"P =\n{P}")
print(f"\nQ =\n{Q}")
print(f"\nP × Q =\n{P * Q}")
print(f"\nQ × P =\n{Q * P}")
print("\n  Perhatikan: P×Q ≠ Q×P  (TIDAK komutatif!)")

# ─── 4. Transpose ─────────────────────────────────────────────
print("\n[4] Transpose")
C = Matrix([[1, 2, 3], [4, 5, 6]])
print(f"C (2×3) =\n{C}")
print(f"\nCᵀ (3×2) =\n{C.transpose()}")
print(f"\n(AB)ᵀ = BᵀAᵀ:")
AB = P * Q
print(f"(P×Q)ᵀ =\n{AB.transpose()}")
print(f"Qᵀ×Pᵀ  =\n{Q.transpose() * P.transpose()}")

# ─── 5. Trace dan Determinan ──────────────────────────────────
print("\n[5] Trace dan Determinan")
M2 = Matrix([[3, 2], [1, 4]])
M3 = Matrix([[1, 2, 3], [0, 4, 5], [1, 0, 6]])

print(f"M2 =\n{M2}")
print(f"tr(M2) = {M2.trace()}")
print(f"det(M2) = {M2.det2()}  (= 3×4 - 2×1 = {3*4-2*1})")

print(f"\nM3 =\n{M3}")
print(f"det(M3) = {M3.det3()}")
print(f"det(M3) via Gauss = {M3.det():.6f}")

# ─── 6. Matriks Invers ────────────────────────────────────────
print("\n[6] Matriks Invers")
M2 = Matrix([[2, 1], [5, 3]])
M2_inv = M2.inverse2()
print(f"M  =\n{M2}")
print(f"\nM⁻¹ =\n{M2_inv}")
I_result = M2 * M2_inv
print(f"\nM × M⁻¹ (harus = I) =\n{I_result}")

# ─── 7. Menyelesaikan Sistem Ax = b ───────────────────────────
print("\n[7] Menyelesaikan Sistem Linear Ax = b")

def gaussian_solve(A_data, b_data):
    """Eliminasi Gauss untuk Ax=b."""
    n = len(b_data)
    # Augmented matrix [A | b]
    M = [list(A_data[i]) + [b_data[i]] for i in range(n)]

    for col in range(n):
        # Partial pivot
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]
        pivot = M[col][col]
        if abs(pivot) < 1e-12:
            return None
        for row in range(col+1, n):
            f = M[row][col] / pivot
            for k in range(col, n+1):
                M[row][k] -= f * M[col][k]

    # Back substitution
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]
    return x

# 2x + y = 5
# 5x + 3y = 13
A_sys = [[2, 1], [5, 3]]
b_sys = [5, 13]
sol = gaussian_solve(A_sys, b_sys)
print(f"  2x + y  = 5")
print(f"  5x + 3y = 13")
print(f"  Solusi: x={sol[0]:.4f}, y={sol[1]:.4f}")
print(f"  Verifikasi: {2*sol[0]+sol[1]:.4f}=5, {5*sol[0]+3*sol[1]:.4f}=13")

# 3×3 system
A3 = [[2,-1,3],[1,3,-1],[3,2,4]]
b3 = [9,6,17]
sol3 = gaussian_solve(A3, b3)
print(f"\n  3×3 system: x={sol3[0]:.4f}, y={sol3[1]:.4f}, z={sol3[2]:.4f}")

# ─── 8. Numpy comparison ──────────────────────────────────────
print("\n[8] Perbandingan dengan NumPy")
try:
    import numpy as np
    A_np = np.array([[2,1],[5,3]], dtype=float)
    b_np = np.array([5,13], dtype=float)
    sol_np = np.linalg.solve(A_np, b_np)
    det_np = np.linalg.det(A_np)
    inv_np = np.linalg.inv(A_np)
    print(f"  np.linalg.solve: x={sol_np[0]:.4f}, y={sol_np[1]:.4f}")
    print(f"  np.linalg.det:   {det_np:.4f}")
    print(f"  np.linalg.inv:\n{inv_np}")
except ImportError:
    print("  (numpy tidak tersedia)")

print("\n[Selesai] Lanjut ke exercises.py")
