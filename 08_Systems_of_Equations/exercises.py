"""
Exercises: Systems of Equations  |  Phase 1 — Topic 1.7
"""
print("LATIHAN 1.7 — SISTEM PERSAMAAN")
print("=" * 50)

# Helper: Cramer 2x2
def cramer_2x2(a1,b1,c1, a2,b2,c2):
    D  = a1*b2 - a2*b1
    Dx = c1*b2 - c2*b1
    Dy = a1*c2 - a2*c1
    if D == 0: return None, None
    return Dx/D, Dy/D

# Ex 1: Substitution
print("\n[Ex 1] Metode Substitusi:")
print("  y = 2x + 1")
print("  3x + y = 16")
print("  Substitusi: 3x + (2x+1) = 16 -> 5x=15 -> x=3, y=7")
x,y = cramer_2x2(-2,1,1, 3,1,16)
print(f"  Verifikasi: x={x}, y={y}")
print(f"  y=2({x})+1={2*x+1}, 3({x})+{y}={3*x+y}")

# Ex 2: Elimination
print("\n[Ex 2] Metode Eliminasi:")
print("  2x + 3y = 12")
print("  4x - 3y = 6")
print("  Tambahkan: 6x = 18 -> x=3; 2(3)+3y=12 -> y=2")
x,y = cramer_2x2(2,3,12, 4,-3,6)
print(f"  Verifikasi: x={x}, y={y}")

# Ex 3: Classification
print("\n[Ex 3] Klasifikasi Sistem:")
systems = [
    (1,-1,3, 2,-2,6, "Dependen (garis sama)"),
    (1,1,3,  1,1,5,  "Inkonsisten (paralel)"),
    (2,3,7,  1,-1,1, "Konsisten (satu solusi)"),
]
for a1,b1,c1,a2,b2,c2,expected in systems:
    D = a1*b2-a2*b1
    if D != 0:
        x,y = cramer_2x2(a1,b1,c1,a2,b2,c2)
        print(f"  {a1}x+{b1}y={c1}, {a2}x+{b2}y={c2}: x={x}, y={y} | {expected}")
    else:
        # Check consistency
        if a1*c2 == a2*c1:
            print(f"  {a1}x+{b1}y={c1}, {a2}x+{b2}y={c2}: TAK HINGGA solusi | {expected}")
        else:
            print(f"  {a1}x+{b1}y={c1}, {a2}x+{b2}y={c2}: TIDAK ADA solusi | {expected}")

# Ex 4: 3-variable system
print("\n[Ex 4] Sistem 3 Variabel (Gaussian Elimination):")
print("   x +  y +  z = 6")
print("  2x - y +  z = 3")
print("   x +  y - 2z = -3")
try:
    import numpy as np
    A = np.array([[1,1,1],[2,-1,1],[1,1,-2]], dtype=float)
    b = np.array([6,3,-3], dtype=float)
    sol = np.linalg.solve(A, b)
    print(f"  Solusi: x={sol[0]:.2f}, y={sol[1]:.2f}, z={sol[2]:.2f}")
    print(f"  Verifikasi A@x = {A@sol} == {b}")
except ImportError:
    print("  (numpy tidak tersedia)")

# Ex 5: Word problem
print("\n[Ex 5] Soal Campuran:")
print("  50 kg campuran kacang A (Rp30.000/kg) dan B (Rp20.000/kg)")
print("  harga total Rp1.200.000")
print("  x + y = 50,  30000x + 20000y = 1200000")
x,y = cramer_2x2(1,1,50, 30000,20000,1200000)
print(f"  Kacang A = {x} kg, Kacang B = {y} kg")

print("\n[Selesai]")
