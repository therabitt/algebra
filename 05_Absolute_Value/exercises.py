"""
Exercises: Absolute Value  |  Phase 1 — Topic 1.15
"""
import math
print("LATIHAN 1.15 — NILAI MUTLAK")
print("=" * 50)

# Ex 1: Compute
print("\n[Ex 1] Hitung nilai mutlak:")
vals = [-7, 0, 3.14, -math.sqrt(2), math.pi-3]
for v in vals:
    print(f"  |{v:.4f}| = {abs(v):.4f}")

# Ex 2: Solve equations
print("\n[Ex 2] Selesaikan persamaan:")
print("  a) |x-5| = 3  ->  x-5=3 atau x-5=-3  ->  x=8 atau x=2")
for x in [8, 2]: print(f"     x={x}: |{x}-5|={abs(x-5)} == 3? {abs(x-5)==3}")

print("  b) |2x+1| = 7  ->  2x+1=7 atau 2x+1=-7  ->  x=3 atau x=-4")
for x in [3,-4]: print(f"     x={x}: |2({x})+1|={abs(2*x+1)} == 7? {abs(2*x+1)==7}")

print("  c) |x+2| = |2x-1|  ->  x+2=2x-1 atau x+2=-(2x-1)")
print("     Case 1: x=3,  Case 2: x=-1/3")
for x in [3, -1/3]: print(f"     x={x:.4f}: |{x:.4f}+2|={abs(x+2):.4f}, |2({x:.4f})-1|={abs(2*x-1):.4f}")

# Ex 3: Solve inequalities
print("\n[Ex 3] Selesaikan pertidaksamaan:")
print("  a) |x| ≤ 4  ->  -4 ≤ x ≤ 4  (interval [-4, 4])")
test = [-5,-4,-1,0,3,4,5]
print(f"     Cek: {[(x, abs(x)<=4) for x in test]}")

print("  b) |2x-3| > 5  ->  2x-3>5 atau 2x-3<-5  ->  x>4 atau x<-1")
for x in [-2,-1,0,2,4,5]: print(f"     x={x}: |2({x})-3|={abs(2*x-3)}>5? {abs(2*x-3)>5}")

# Ex 4: Distance interpretation
print("\n[Ex 4] Interpretasi jarak:")
print("  Semua x yang berjarak kurang dari 3 dari titik x=5:")
print("  |x-5| < 3  ->  2 < x < 8")
for x in [1,2,3,5,7,8,9]:
    d = abs(x-5)
    print(f"  x={x}: jarak={d} < 3? {d<3}")

# Ex 5: Triangle inequality
print("\n[Ex 5] Verifikasi ketidaksamaan segitiga pada bilangan kompleks:")
z1, z2 = 3+4j, 1-2j
lhs = abs(z1+z2)
rhs = abs(z1)+abs(z2)
print(f"  z1={z1}, z2={z2}")
print(f"  |z1+z2| = {lhs:.4f}")
print(f"  |z1|+|z2| = {rhs:.4f}")
print(f"  |z1+z2| ≤ |z1|+|z2|? {lhs <= rhs + 1e-10}  ✓")

print("\n[Selesai]")
