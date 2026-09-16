"""
Module  : Absolute Value (Nilai Mutlak)
Phase   : 1 - Algebra  |  Topic: 1.15
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("NILAI MUTLAK — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Definisi dan Implementasi dari Nol ────────────────────
print("\n[1] Implementasi |x| dari nol (piecewise)")

def my_abs(x):
    """Nilai mutlak tanpa abs() bawaan Python."""
    return x if x >= 0 else -x

values = [-5, -0.5, 0, 0.5, 3, -100, math.pi, -math.e]
print(f"  {'x':>10} | {'|x| manual':>12} | {'abs(x)':>8} | {'Match?':>6}")
for v in values:
    manual = my_abs(v)
    builtin = abs(v)
    print(f"  {v:>10.4f} | {manual:>12.4f} | {builtin:>8.4f} | {abs(manual-builtin)<1e-12}")

# ─── 2. Sifat-Sifat ───────────────────────────────────────────
print("\n[2] Verifikasi Sifat Nilai Mutlak")

import random; random.seed(7)
test_pairs = [(random.uniform(-10,10), random.uniform(-10,10)) for _ in range(5)]

print("  Menguji |xy| = |x|·|y|  dan  |x/y| = |x|/|y|  dan  √(x²) = |x|:")
print(f"  {'x':>7} {'y':>7} | {'|xy|':>8} | {'|x|·|y|':>8} | {'√x²=|x|':>10}")
for x, y in test_pairs:
    lhs_mul = abs(x*y)
    rhs_mul = abs(x)*abs(y)
    sqrt_sq = math.sqrt(x**2)
    print(f"  {x:>7.3f} {y:>7.3f} | {lhs_mul:>8.4f} | {rhs_mul:>8.4f} | "
          f"{sqrt_sq:>8.4f}={abs(x):.4f} ✓{abs(sqrt_sq-abs(x))<1e-10}")

# ─── 3. Ketidaksamaan Segitiga ────────────────────────────────
print("\n[3] Ketidaksamaan Segitiga: |x+y| ≤ |x| + |y|")
print(f"  {'x':>8} {'y':>8} | {'|x+y|':>8} | {'|x|+|y|':>10} | {'|x+y|≤|x|+|y|':>15}")
for x, y in test_pairs:
    lhs = abs(x+y)
    rhs = abs(x)+abs(y)
    print(f"  {x:>8.3f} {y:>8.3f} | {lhs:>8.4f} | {rhs:>10.4f} | {lhs<=rhs+1e-10}")

# ─── 4. Persamaan Nilai Mutlak ────────────────────────────────
print("\n[4] Menyelesaikan |ax + b| = c")

def solve_abs_eq(a, b, c):
    """
    Selesaikan |ax + b| = c
    Kasus: c > 0 -> dua solusi, c = 0 -> satu solusi, c < 0 -> tidak ada
    """
    if c < 0:
        print(f"  |{a}x + {b}| = {c}: tidak ada solusi (|...| selalu ≥ 0)")
        return []
    if c == 0:
        x = -b/a if a != 0 else None
        print(f"  |{a}x + {b}| = 0: x = {x}")
        return [x] if x is not None else []
    # ax+b = c  atau  ax+b = -c
    if a == 0:
        if abs(b) == c: print(f"  |{b}| = {c}: True (tak hingga solusi)")
        else: print(f"  |{b}| = {c}: False (tidak ada solusi)")
        return []
    x1 = (c - b) / a
    x2 = (-c - b) / a
    print(f"  |{a}x + {b}| = {c}")
    print(f"    -> {a}x + {b} = {c}  =>  x = {x1}")
    print(f"    -> {a}x + {b} = {-c} =>  x = {x2}")
    return sorted([x1, x2])

solve_abs_eq(2, -3, 5)   # |2x-3| = 5
solve_abs_eq(1, 0, 4)    # |x| = 4
solve_abs_eq(3, 6, 0)    # |3x+6| = 0
solve_abs_eq(1, 0, -2)   # |x| = -2

# ─── 5. Pertidaksamaan Nilai Mutlak ──────────────────────────
print("\n[5] Menyelesaikan Pertidaksamaan |ax + b| {op} c")

def solve_abs_ineq(a, b, c, op):
    """
    Selesaikan |ax+b| op c
    op: "<", "<=", ">", ">="
    """
    if a == 0:
        print(f"  |{b}| {op} {c}: {eval(f'{abs(b)} {op} {c}')}")
        return

    if op in ("<", "<="):
        # -c op ax+b op c  ->  (-c-b)/a op x op (c-b)/a
        lo = (-c-b)/a; hi = (c-b)/a
        if a < 0: lo, hi = hi, lo  # flip jika a negatif
        bracket = "[" if op == "<=" else "("
        bracket_r = "]" if op == "<=" else ")"
        print(f"  |{a}x + {b}| {op} {c}  ->  x ∈ {bracket}{lo:.4g}, {hi:.4g}{bracket_r}")
    else:
        # x < (-c-b)/a atau x > (c-b)/a
        val1 = (-c-b)/a; val2 = (c-b)/a
        if a < 0: val1, val2 = val2, val1
        left_open = "(" if op == ">" else "("
        right_close = ")" if op == ">=" else ")"
        bracket_l = "(" if op == ">" else "("
        bracket_r = ")" if op == ">=" else ")"
        edge = "]" if op == ">=" else ")"
        print(f"  |{a}x + {b}| {op} {c}  ->  "
              f"x < {min(val1,val2):.4g} atau x > {max(val1,val2):.4g}")

solve_abs_ineq(1, 0, 3, "<")    # |x| < 3
solve_abs_ineq(1, -2, 4, "<=")  # |x-2| <= 4
solve_abs_ineq(2, 1, 3, ">")    # |2x+1| > 3
solve_abs_ineq(1, 0, 5, ">=")   # |x| >= 5

# ─── 6. Jarak sebagai Nilai Mutlak ───────────────────────────
print("\n[6] Jarak Menggunakan Nilai Mutlak")
print("  |x - a| = jarak x ke a")
a_pt = 3
test_xs = [-2, 0, 1, 3, 5, 7]
print(f"  Jarak ke titik a={a_pt}:")
for x in test_xs:
    dist = abs(x - a_pt)
    print(f"  |{x} - {a_pt}| = {dist}")

# Error tolerance
print("\n  Aplikasi toleransi: |x - 10| < 0.01  (x dalam 0.01 dari 10)")
test_vals = [9.99, 10.005, 10.012, 10.009, 9.98]
for v in test_vals:
    within = abs(v - 10) < 0.01
    print(f"  x={v}: |{v}-10|={abs(v-10):.4f} < 0.01? {within}")

# ─── 7. Modulus Bilangan Kompleks ────────────────────────────
print("\n[7] Modulus Bilangan Kompleks |a + bi|")
complex_nums = [3+4j, 1-1j, 5+0j, 0+3j, -2-2j]
for z in complex_nums:
    mod = abs(z)
    manual = math.sqrt(z.real**2 + z.imag**2)
    print(f"  |{z}| = {mod:.4f} = √({z.real:.0f}²+{z.imag:.0f}²) = {manual:.4f}")

# ─── 8. Transformasi Fungsi |x| ──────────────────────────────
print("\n[8] Transformasi f(x) = a|x-h| + k")
def abs_transformed(a, h, k):
    return lambda x: a*abs(x-h) + k

transforms = [
    (1, 0, 0, "|x|",         "standard"),
    (1, 2, 0, "|x-2|",       "geser kanan 2"),
    (1, 0, 3, "|x|+3",       "geser atas 3"),
    (2, 0, 0, "2|x|",        "stretch vertikal x2"),
    (-1,0, 0, "-|x|",        "refleksi x-axis"),
]
x_test = 2
print(f"  Evaluasi semua transformasi di x={x_test}:")
for a, h, k, label, desc in transforms:
    f = abs_transformed(a, h, k)
    print(f"  {label:>12} ({desc:>25}): f({x_test}) = {f(x_test)}")

print("\n[Selesai] Lanjut ke exercises.py")
