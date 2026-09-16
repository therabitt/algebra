"""
Exercises: Algebraic Expressions  |  Phase 1 — Topic 1.3
"""
print("LATIHAN 1.3 — EKSPRESI ALJABAR")
print("=" * 50)

print("""
[Ex 1] Evaluasi f(x) = 2x^2 + 3x - 5 untuk x = -1, 0, 2, 4
""")
def f(x): return 2*x**2 + 3*x - 5
for v in [-1, 0, 2, 4]:
    print(f"  f({v}) = {f(v)}")

print("""
[Ex 2] Sederhanakan: 4x^2 - 3x + 7 + 2x^2 + 5x - 9
  Suku x^2: 4+2=6  ->  6x^2
  Suku x  : -3+5=2 ->  2x
  Konst   : 7-9=-2 -> -2
  Hasil: 6x^2 + 2x - 2
""")
from collections import defaultdict
terms = [(2,4),(1,-3),(0,7),(2,2),(1,5),(0,-9)]
combined = defaultdict(int)
for d,c in terms: combined[d]+=c
print(f"  Koefisien: {dict(combined)}")
print(f"  => 6x^2 + 2x - 2  ✓")

print("""
[Ex 3] Kalikan (2x + 5)(x - 3) menggunakan FOIL
  F: 2x*x  = 2x^2
  O: 2x*-3 = -6x
  I: 5*x   = 5x
  L: 5*-3  = -15
  Hasil: 2x^2 - x - 15
""")
a,b,c,d = 2,5,1,-3
print(f"  2x^2 + {a*d+b*c}x + {b*d}")
import sympy as sp
x = sp.Symbol("x")
print(f"  SymPy verify: {sp.expand((2*x+5)*(x-3))}")

print("""
[Ex 4] Buktikan (a+b)^2 = a^2 + 2ab + b^2 untuk a=7, b=3
""")
a,b = 7,3
lhs = (a+b)**2
rhs = a**2 + 2*a*b + b**2
print(f"  (7+3)^2 = {lhs}")
print(f"  7^2+2(7)(3)+3^2 = {rhs}")
print(f"  Sama? {lhs == rhs}  ✓")

print("""
[Ex 5] Tentukan domain dari f(x) = (x+1)/(x^2-4)
  Penyebut = 0 jika x^2-4=0 -> x=2 atau x=-2
  Domain: semua real kecuali x=2 dan x=-2
  Notasi: (-inf,-2) U (-2,2) U (2,+inf)
""")
def safe_f(x):
    d = x**2 - 4
    if abs(d) < 1e-10: return float("nan")
    return (x+1)/d
for v in [-3, -2, 0, 2, 5]:
    val = safe_f(v)
    print(f"  f({v:3}) = {val}")

print("\n[Selesai]")
