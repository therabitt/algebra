"""
Exercises: Exponents and Logarithms  |  Phase 1 — Topic 1.11
"""
import math
print("LATIHAN 1.11 — EKSPONEN DAN LOGARITMA")
print("=" * 50)

# Ex 1: Exponent laws
print("\n[Ex 1] Sederhanakan menggunakan hukum eksponen:")
cases = [
    ("2^3 * 2^4", 2**3 * 2**4, 2**(3+4)),
    ("3^6 / 3^2", 3**6 / 3**2, 3**(6-2)),
    ("(5^2)^3",  (5**2)**3,    5**(2*3)),
    ("4^0",       4**0,         1),
    ("2^(-3)",    2**(-3),      1/8),
    ("9^(1/2)",   9**0.5,       3),
]
for label, lhs, rhs in cases:
    print(f"  {label} = {lhs:.6g}  (expected {rhs:.6g})  ✓ {abs(lhs-rhs)<1e-9}")

# Ex 2: Logarithm laws
print("\n[Ex 2] Hitung nilai logaritma:")
log_cases = [
    ("log_2(64)",  math.log(64,2),    6),
    ("log(0.001)", math.log10(0.001), -3),
    ("ln(e^5)",    math.log(math.e**5), 5),
    ("log_5(125)", math.log(125,5),   3),
]
for label, val, expected in log_cases:
    print(f"  {label} = {val:.6g}  (expected {expected})  ✓ {abs(val-expected)<1e-9}")

# Ex 3: Solve exponential equations
print("\n[Ex 3] Selesaikan persamaan eksponen:")
print("  a) 4^x = 64  ->  x = log_4(64) =", math.log(64,4))
print("  b) 10^(2x-1) = 1000  ->  2x-1=3  ->  x=2  ->", (3+1)/2)
print("  c) 5^(x+2) = 25^x  ->  5^(x+2) = 5^(2x)  ->  x+2=2x  ->  x=2")

# Ex 4: Compound interest
print("\n[Ex 4] Bunga Majemuk: A = P(1 + r/n)^(nt)")
P = 5_000_000  # Rp 5 juta
r = 0.08       # 8% per tahun
n = 12         # bunga bulanan
print(f"  P={P:,}, r={r*100}%, n={n}")
for t in [1, 5, 10, 20]:
    A = P * (1 + r/n)**(n*t)
    print(f"  t={t:>3} tahun: A = Rp {A:>15,.2f}")

# Ex 5: Half-life
print("\n[Ex 5] Waktu Paruh (Half-life): N(t) = N0 * (1/2)^(t/t_half)")
N0 = 1000
t_half = 5  # tahun
print(f"  N0={N0}, t_half={t_half} tahun")
for t in [0, 5, 10, 15, 20]:
    N = N0 * (0.5)**(t/t_half)
    print(f"  t={t:>3}: N = {N:>8.2f}")
t_zero_half = t_half * math.log(2) / math.log(N0)
print(f"  Kapan N=1? t = {t_half * math.log(N0) / math.log(2):.2f} tahun")

print("\n[Selesai]")
