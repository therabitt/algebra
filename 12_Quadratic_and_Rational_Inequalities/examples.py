"""
Module  : Quadratic & Rational Inequalities
Phase   : 1 - Algebra  |  Topic: 1.17
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("PERTIDAKSAMAAN KUADRAT & RASIONAL")
print("=" * 60)

# ─── 1. Tabel Tanda (Sign Chart) ──────────────────────────────
print("\n[1] Metode Tabel Tanda (Sign Chart)")

def sign_chart(factors, test_values, critical_points):
    """
    Buat tabel tanda untuk f(x) = product(factors).
    factors: list of lambda x -> nilai
    critical_points: titik-titik kritis (terurut)
    test_values: satu nilai test per interval
    """
    print(f"  Titik kritis: {critical_points}")
    intervals = (["(-∞, " + str(critical_points[0]) + ")"] +
                 [f"({critical_points[i]}, {critical_points[i+1]})"
                  for i in range(len(critical_points)-1)] +
                 ["(" + str(critical_points[-1]) + ", +∞)"])

    for i, (interval, t) in enumerate(zip(intervals, test_values)):
        signs = [("+" if f(t) > 0 else "-") for f in factors]
        product = 1
        for f in factors: product *= f(t)
        total_sign = "+" if product > 0 else "-"
        print(f"  {interval:>20}: [{', '.join(signs)}] => {total_sign}")

# ─── 2. Pertidaksamaan Kuadrat ────────────────────────────────
print("\n[2] x² - 5x + 6 > 0")
print("  Faktorkan: (x-2)(x-3) > 0")
print("  Titik kritis: x=2, x=3")
factors = [lambda x: x-2, lambda x: x-3]
sign_chart(factors, [-10, 2.5, 10], [2, 3])
print("  Solusi: x < 2 atau x > 3  =>  (-∞,2) ∪ (3,∞)")

# Verifikasi
print("  Verifikasi:")
for xv in [-1, 2, 2.5, 3, 4]:
    val = xv**2 - 5*xv + 6
    print(f"    x={xv}: val={val:.2f} > 0? {val > 0}")

print("\n[3] -x² + 4x - 4 ≥ 0")
print("  = -(x-2)² ≥ 0  => -(x-2)² ≥ 0")
print("  (x-2)² ≥ 0 selalu, tapi -(x-2)² ≤ 0")
print("  Solusi: -(x-2)² = 0 => x = 2  (satu titik!)")
for xv in [0, 1, 2, 3, 4]:
    val = -xv**2 + 4*xv - 4
    print(f"    x={xv}: {val:.2f} ≥ 0? {val >= 0}")

print("\n[4] x² + 2x + 5 < 0")
D = 4 - 20
print(f"  D = {D} < 0, koefisien a=1 > 0 => selalu POSITIF")
print("  Tidak ada solusi real!")

# ─── 3. Pertidaksamaan Rasional ──────────────────────────────
print("\n[5] (x-1)/(x+2) > 0")
print("  Titik kritis: x=1 (num=0), x=-2 (den=0)")
print("  PENTING: x=-2 tidak masuk solusi (penyebut=0)!")

factors_r = [lambda x: x-1, lambda x: x+2]
sign_chart(factors_r, [-10, -1.5, 5], [-2, 1])
print("  Solusi: x < -2 atau x > 1  =>  (-∞,-2) ∪ (1,∞)")

for xv in [-5, -2, 0, 1, 3]:
    if xv == -2:
        print(f"    x={xv}: UNDEFINED (penyebut=0)")
    else:
        val = (xv-1)/(xv+2)
        print(f"    x={xv}: {val:.4f} > 0? {val > 0}")

print("\n[6] (x²-4)/(x-3) ≤ 0")
print("  = (x+2)(x-2)/(x-3) ≤ 0")
print("  Titik kritis: x=-2, x=2, x=3")
factors_r2 = [lambda x: x+2, lambda x: x-2, lambda x: x-3]
sign_chart(factors_r2, [-10, 0, 2.5, 10], [-2, 2, 3])
print("  Solusi: x ≤ -2 atau 2 ≤ x < 3  (x=3 dikecualikan!)")

# ─── 4. |f(x)| > g(x) — Advanced Absolute Value ─────────────
print("\n[7] |2x-1| > x+2  (nilai mutlak lanjut)")
print("  Kasus 1: 2x-1 ≥ 0, i.e. x ≥ 1/2:")
print("    2x-1 > x+2  =>  x > 3")
print("  Kasus 2: 2x-1 < 0, i.e. x < 1/2:")
print("    -(2x-1) > x+2  =>  1-2x > x+2  =>  -1 > 3x  =>  x < -1/3")
print("  Solusi: x < -1/3 atau x > 3  =>  (-∞, -1/3) ∪ (3, +∞)")

for xv in [-1, -1/3, 0, 3, 4]:
    lhs = abs(2*xv - 1)
    rhs = xv + 2
    print(f"    x={xv:>6.3f}: |2x-1|={lhs:.3f} > x+2={rhs:.3f}? {lhs > rhs}")

print("\n[8] |x+1| < |x-3|")
print("  Kuadratkan: (x+1)² < (x-3)²")
print("  x²+2x+1 < x²-6x+9  =>  8x < 8  =>  x < 1")
for xv in [-2, 0, 0.99, 1, 2]:
    lhs = abs(xv+1)
    rhs = abs(xv-3)
    print(f"    x={xv:>5.2f}: |x+1|={lhs:.2f} < |x-3|={rhs:.2f}? {lhs < rhs}")

print("\n[Selesai]")
