"""
Exercises: Basic Matrices  |  Phase 1 — Topic 1.13
"""
print("LATIHAN 1.13 — MATRIKS DASAR")
print("=" * 50)

# ─── Helpers ──────────────────────────────────────────────────
def mat_add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_mul(A, B):
    m,n,p = len(A), len(A[0]), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
def det2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]
def inv2(A):
    d = det2(A)
    if abs(d) < 1e-12: return None
    return [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]
def show(A, label=""):
    if label: print(f"  {label}:")
    for row in A:
        print("   ", row)

# ─── Ex 1: Basic Operations ───────────────────────────────────
print("\n[Ex 1] Hitung A+B, A-B, 2A, Aᵀ")
A = [[1,2,3],[4,5,6]]
B = [[7,8,9],[1,2,3]]
show(mat_add(A,B), "A+B")
show([[A[i][j]-B[i][j] for j in range(3)] for i in range(2)], "A-B")
show([[2*A[i][j] for j in range(3)] for i in range(2)], "2A")
show(transpose(A), "Aᵀ")

# ─── Ex 2: Matrix Multiplication ──────────────────────────────
print("\n[Ex 2] Kalikan matriks")
P = [[1,2],[3,4]]
Q = [[5,0],[1,3]]
PQ = mat_mul(P,Q)
QP = mat_mul(Q,P)
show(PQ, "P×Q")
show(QP, "Q×P")
print(f"  PQ == QP? {PQ == QP}  (tidak komutatif!)")

# ─── Ex 3: Determinant ────────────────────────────────────────
print("\n[Ex 3] Hitung determinan:")
matrices = [
    ([[3,2],[1,4]], "3  2 / 1  4"),
    ([[-1,5],[2,-3]], "-1  5 / 2  -3"),
    ([[0,1],[0,2]], "0  1 / 0  2"),
]
for M, label in matrices:
    d = det2(M)
    print(f"  det({label}) = {d}  {'(singular!)' if d==0 else ''}")

# ─── Ex 4: Inverse ────────────────────────────────────────────
print("\n[Ex 4] Hitung invers (jika ada):")
for M, label in [([[2,1],[5,3]],"A"), ([[4,2],[2,1]],"B")]:
    inv = inv2(M)
    if inv:
        check = mat_mul(M, inv)
        print(f"  inv({label}) = {inv}")
        print(f"  A×A⁻¹ = {check}  (≈ I? {all(abs(check[i][j]-(1 if i==j else 0))<1e-9 for i in range(2) for j in range(2))})")
    else:
        print(f"  {label}: singular, tidak punya invers!")

# ─── Ex 5: Solve system ───────────────────────────────────────
print("\n[Ex 5] Selesaikan sistem menggunakan matriks invers:")
print("  3x + y = 10")
print("  2x + 5y = 17")
A_sys = [[3,1],[2,5]]
b_sys = [10,17]
inv_A = inv2(A_sys)
if inv_A:
    x = [sum(inv_A[i][j]*b_sys[j] for j in range(2)) for i in range(2)]
    print(f"  x = A⁻¹b = {x}")
    print(f"  Verifikasi: 3({x[0]:.2f})+{x[1]:.2f}={3*x[0]+x[1]:.2f}, "
          f"2({x[0]:.2f})+5({x[1]:.2f})={2*x[0]+5*x[1]:.2f}")

# ─── Ex 6: Image transformation ──────────────────────────────
print("\n[Ex 6] Transformasi 2D menggunakan matriks")
import math
angle = math.pi/4  # 45 derajat
R = [[math.cos(angle), -math.sin(angle)],
     [math.sin(angle),  math.cos(angle)]]
point = [[1],[0]]  # titik (1, 0)
rotated = mat_mul(R, point)
print(f"  Rotasi titik (1,0) sebesar 45°:")
print(f"  = ({rotated[0][0]:.4f}, {rotated[1][0]:.4f})")
print(f"  (expected: (√2/2, √2/2) = ({math.sqrt(2)/2:.4f}, {math.sqrt(2)/2:.4f}))")

print("\n[Selesai]")
