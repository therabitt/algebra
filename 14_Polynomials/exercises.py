"""
Exercises: Polynomials  |  Phase 1 — Topic 1.9
"""
import math
print("LATIHAN 1.9 — POLINOMIAL")
print("=" * 50)

class P:
    def __init__(self, *c): self.c = list(c)
    def __call__(self, x):
        r = 0
        for v in reversed(self.c): r = r*x + v
        return r
    def degree(self): return len(self.c)-1

# Ex 1
print("\n[Ex 1] Evaluasi P(x) = x^4 - 3x^3 + 2x - 7 untuk x=-1,0,1,2,3")
p = P(-7, 2, 0, -3, 1)
for x in [-1,0,1,2,3]:
    print(f"  P({x}) = {p(x)}")

# Ex 2: degree and leading term
print("\n[Ex 2] Identifikasi derajat dan koefisien leading:")
polys = [
    ("4x^5 - x^3 + 2x - 9", P(-9,2,0,-1,0,4), 5, 4),
    ("7",                    P(7),               0, 7),
    ("-3x^2 + x",            P(0,1,-3),          2,-3),
]
for label, p_obj, deg, lead in polys:
    print(f"  {label}: derajat={p_obj.degree()} (exp={deg}), leading={p_obj.c[-1]} (exp={lead})")

# Ex 3: Remainder theorem
print("\n[Ex 3] Gunakan Teorema Sisa untuk P(x)=x^3+2x^2-5x-6:")
p3 = P(-6,-5,2,1)
print("  Sisa P(x)/(x-a):")
for a in [1,-1,2,-2,3,-3]:
    print(f"  a={a:3}: P({a:3}) = {p3(a):5}")

# Ex 4: Factor theorem
print("\n[Ex 4] Tentukan faktor dari P(x)=x^3-6x^2+11x-6")
p4 = P(-6,11,-6,1)
print("  Cek (x-a) adalah faktor:")
for a in range(-4,5):
    if abs(p4(a)) < 1e-9:
        print(f"  (x-{a}) adalah faktor!  P({a})={p4(a):.0f}")

# Ex 5: End behavior
print("\n[Ex 5] Perilaku ujung (end behavior):")
print("  P(x) = -2x^3 + ... (derajat ganjil, leading negatif)")
print("  Saat x->+inf: P(x)->-inf")
print("  Saat x->-inf: P(x)->+inf")
p5 = P(0,0,0,-2)  # -2x^3
for x in [-100, -10, 10, 100]:
    print(f"  P({x}) = {p5(x):.0f}")

print("\n[Selesai]")
