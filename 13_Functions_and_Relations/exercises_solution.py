"""
Exercises: Functions and Relations  |  Phase 1 — Topic 1.8
"""
import math
print("LATIHAN 1.8 — FUNGSI DAN RELASI")
print("=" * 50)

# Ex 1: Domain
print("\n[Ex 1] Tentukan domain fungsi:")
funcs = [
    ("f(x) = √(x-3)",       lambda x: x >= 3,    "x >= 3  i.e. [3, ∞)"),
    ("g(x) = 1/(x^2-4)",    lambda x: abs(x)!=2, "x ≠ ±2"),
    ("h(x) = ln(2x-1)",     lambda x: 2*x-1 > 0, "x > 1/2 i.e. (1/2, ∞)"),
]
for label, domain_fn, answer in funcs:
    test_vals = [-5,-2,-1,0,0.5,1,2,3,4,10]
    valid = [v for v in test_vals if domain_fn(v)]
    print(f"  {label}: domain = {answer}")
    print(f"    (tes nilai: {valid})")

# Ex 2: Composition
print("\n[Ex 2] Komposisi Fungsi")
def f(x): return 2*x + 3
def g(x): return x**2 - 1

print(f"  f(x) = 2x+3,  g(x) = x^2-1")
x = 2
fog = f(g(x))
gof = g(f(x))
print(f"  (f∘g)(2) = f(g(2)) = f({g(x)}) = {fog}")
print(f"  (g∘f)(2) = g(f(2)) = g({f(x)}) = {gof}")
print(f"  f∘g ≠ g∘f: {fog != gof}  (komposisi tidak komutatif!)")

# Ex 3: Inverse
print("\n[Ex 3] Fungsi Invers")
print("  f(x) = 3x - 5  ->  invers: f^-1(x) = (x+5)/3")
def f_inv(x): return (x+5)/3
for val in [0, 4, 7, -2]:
    y = 3*val - 5
    x_back = f_inv(y)
    print(f"  f({val})={y},  f^-1({y})={x_back:.4g}  (back to {val}? {abs(x_back-val)<1e-10})")

# Ex 4: Even/Odd
print("\n[Ex 4] Fungsi Genap dan Ganjil")
def is_even(f, test_range=range(-5,6)):
    return all(abs(f(x) - f(-x)) < 1e-10 for x in test_range if x != 0)
def is_odd(f, test_range=range(-5,6)):
    return all(abs(f(x) + f(-x)) < 1e-10 for x in test_range if x != 0)

funcs_eo = [
    ("x^2", lambda x: x**2),
    ("x^3", lambda x: x**3),
    ("x^2+x", lambda x: x**2+x),
    ("cos(x)", math.cos),
    ("sin(x)", math.sin),
]
print(f"  {'Fungsi':>15} | {'Genap':>6} | {'Ganjil':>6}")
for name, fn in funcs_eo:
    e = is_even(fn); o = is_odd(fn)
    print(f"  {name:>15} | {str(e):>6} | {str(o):>6}")

# Ex 5: Piecewise
print("\n[Ex 5] Fungsi Pecahan (Piecewise)")
def piecewise(x):
    if x < 0:   return -x
    elif x < 3: return x**2
    else:       return 9
test = [-3,-1,0,1,2,3,4,5]
print(f"  f(x) = -x jika x<0 | x^2 jika 0<=x<3 | 9 jika x>=3")
print(f"  {'x':>5}: " + "  ".join(f"{v:>3}" for v in test))
print(f"  {'f':>5}: " + "  ".join(f"{piecewise(v):>3}" for v in test))

print("\n[Selesai]")
