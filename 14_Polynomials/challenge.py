"""
Challenge: Polynomials  |  Phase 1 — Topic 1.9
"""
import math
print("CHALLENGE 1.9 — POLINOMIAL")

# Challenge 1: Lagrange Interpolation
print("\n[Ch1] Interpolasi Lagrange")
print("  Temukan polinomial unik derajat n yang melewati n+1 titik")

def lagrange_interpolate(points):
    """
    Buat fungsi interpolasi Lagrange dari titik-titik.
    points: list of (x, y) pairs
    """
    def poly(x):
        result = 0.0
        n = len(points)
        for i, (xi, yi) in enumerate(points):
            # Hitung L_i(x) = product((x-xj)/(xi-xj)) for j!=i
            L = 1.0
            for j, (xj, yj) in enumerate(points):
                if i != j:
                    L *= (x - xj) / (xi - xj)
            result += yi * L
        return result
    return poly

# Contoh: interpolasi sin(x) di beberapa titik
import math
sample_points = [(0, 0), (math.pi/6, 0.5), (math.pi/4, math.sqrt(2)/2),
                 (math.pi/3, math.sqrt(3)/2), (math.pi/2, 1.0)]
sin_poly = lagrange_interpolate(sample_points)

print(f"  Interpolasi sin(x) dari {len(sample_points)} titik:")
test_xs = [0, math.pi/8, math.pi/4, 3*math.pi/8, math.pi/2]
print(f"  {'x':>12} | {'Lagrange':>12} | {'sin(x)':>12} | {'Error':>12}")
for x in test_xs:
    approx = sin_poly(x)
    actual = math.sin(x)
    print(f"  {x:>12.6f} | {approx:>12.8f} | {actual:>12.8f} | {abs(approx-actual):>12.2e}")

# Challenge 2: Synthetic Division
print("\n[Ch2] Pembagian Sintetis (Synthetic Division)")
def synthetic_division(coeffs, divisor_root):
    """
    Bagi P(x) dengan (x - r) menggunakan pembagian sintetis.
    coeffs: koefisien dari derajat tinggi ke rendah [a_n, ..., a_0]
    """
    result = [coeffs[0]]
    for c in coeffs[1:]:
        result.append(result[-1] * divisor_root + c)
    return result[:-1], result[-1]  # quotient, remainder

# P(x) = x^3 - 6x^2 + 11x - 6, divide by (x-3)
coeffs = [1, -6, 11, -6]
q, r = synthetic_division(coeffs, 3)
print(f"  P(x) = x^3-6x^2+11x-6, bagi (x-3):")
print(f"  Quotient : {q}  (= {q[0]}x^2 + {q[1]}x + {q[2]})")
print(f"  Remainder: {r}")

# Verify: remainder = P(3)
p = lambda x: x**3 - 6*x**2 + 11*x - 6
print(f"  P(3) = {p(3)} == remainder {r}: {abs(p(3)-r)<1e-10}")

print("\n[Selesai Challenge 1.9]")
