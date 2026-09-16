"""
Challenge: Quadratic & Rational Inequalities  |  Phase 1 — Topic 1.17
"""
import math
print("CHALLENGE 1.17 — PERTIDAKSAMAAN KUADRAT & RASIONAL")

# Challenge 1: General Sign Chart Engine
print("\n[Ch1] Sign Chart Engine Universal")

def solve_inequality_by_sign_chart(numerator_roots, denominator_roots, strict_denom=True):
    """
    Selesaikan f(x) > 0 menggunakan sign chart.
    Asumsi: setiap faktor (x - r) muncul sekali.
    """
    all_roots = sorted(set(numerator_roots + denominator_roots))
    print(f"  Titik kritis: {all_roots}")

    # Tentukan interval
    intervals = []
    if all_roots:
        intervals.append((-math.inf, all_roots[0]))
        for i in range(len(all_roots)-1):
            intervals.append((all_roots[i], all_roots[i+1]))
        intervals.append((all_roots[-1], math.inf))

    print(f"  {'Interval':>25} | {'Tanda f(x)':>10} | {'Dalam solusi?':>14}")
    print("  " + "-"*55)
    solutions = []
    for lo, hi in intervals:
        # Pilih titik test
        if lo == -math.inf and hi == math.inf:
            t = 0.0
        elif lo == -math.inf:
            t = hi - 1
        elif hi == math.inf:
            t = lo + 1
        else:
            t = (lo + hi) / 2

        # Hitung tanda
        num_sign = 1
        for r in numerator_roots:
            num_sign *= (t - r)
        den_sign = 1
        for r in denominator_roots:
            den_sign *= (t - r)

        if abs(den_sign) < 1e-12:
            continue

        total = num_sign / den_sign
        sign_str = "+" if total > 0 else "-"
        in_solution = total > 0

        lo_str = "-∞" if lo == -math.inf else str(round(lo,3))
        hi_str = "+∞" if hi == math.inf   else str(round(hi,3))
        print(f"  ({lo_str}, {hi_str}){' ':>5} | {sign_str:>10} | {str(in_solution):>14}")

        if in_solution:
            solutions.append((lo, hi))

    return solutions

print("\n  (x-1)(x-3)/(x+2) > 0")
print("  Num roots: [1,3], Den roots: [-2]")
solve_inequality_by_sign_chart([1, 3], [-2])

print("\n  (x+1)(x-2)(x-4) < 0  =>  (x+1)(x-2)(x-4) * (-1) > 0")
print("  Equivalently, solve -(x+1)(x-2)(x-4) > 0")
solve_inequality_by_sign_chart([-1, 2, 4], [])

# Challenge 2: AM-GM Inequality
print("\n[Ch2] Ketidaksamaan AM-GM")
print("  AM ≥ GM: (a+b)/2 ≥ √(ab) untuk a,b ≥ 0")
print("  Kesamaan terjadi jika dan hanya jika a = b")

def verify_am_gm(pairs):
    for a, b in pairs:
        am = (a+b)/2
        gm = math.sqrt(a*b) if a*b >= 0 else float('nan')
        print(f"  a={a:>6}, b={b:>6}: AM={am:>8.4f}, GM={gm:>8.4f}, AM≥GM? {am>=gm-1e-10}")

verify_am_gm([(4,9),(1,1),(3,12),(0,16),(5,5)])

print("\n  Generalized: (x₁+x₂+...+xₙ)/n ≥ (x₁x₂...xₙ)^(1/n)")
data = [2, 3, 5, 8]
n = len(data)
AM = sum(data)/n
GM = math.prod(data)**(1/n)
print(f"  Data: {data}")
print(f"  AM = {AM:.4f},  GM = {GM:.4f},  AM ≥ GM? {AM >= GM - 1e-10}")

# Challenge 3: Cauchy-Schwarz
print("\n[Ch3] Ketidaksamaan Cauchy-Schwarz")
print("  (Σ aᵢbᵢ)² ≤ (Σ aᵢ²)(Σ bᵢ²)")
a_vec = [1, 2, 3, 4]
b_vec = [4, 3, 2, 1]
lhs = sum(a*b for a,b in zip(a_vec, b_vec))**2
rhs = sum(a**2 for a in a_vec) * sum(b**2 for b in b_vec)
print(f"  a = {a_vec}, b = {b_vec}")
print(f"  (Σab)² = {lhs}")
print(f"  (Σa²)(Σb²) = {rhs}")
print(f"  (Σab)² ≤ (Σa²)(Σb²)? {lhs <= rhs}")

print("\n[Selesai Challenge 1.17]")
