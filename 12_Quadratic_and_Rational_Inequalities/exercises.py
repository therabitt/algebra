"""
Exercises: Quadratic & Rational Inequalities  |  Phase 1 — Topic 1.17
"""
import math
print("LATIHAN 1.17 — PERTIDAKSAMAAN KUADRAT & RASIONAL")
print("=" * 55)

def check_interval(f, a, b, n=20):
    """Cek apakah SEMUA nilai di (a,b) memenuhi f(x) > 0."""
    xs = [a + (b-a)*(i+1)/(n+1) for i in range(n)]
    return all(f(x) > 0 for x in xs)

# Ex 1: Quadratic
print("\n[Ex 1] Selesaikan pertidaksamaan kuadrat:")
cases_q = [
    ("x²-7x+12 > 0", lambda x: x**2-7*x+12, "> 0",
     "x<3 atau x>4", [(-10,3),(4,10)], [(3,4)]),
    ("x²+x-6 ≤ 0",  lambda x: x**2+x-6,   "≤ 0",
     "-3 ≤ x ≤ 2",  [(-3,2)],        [(-10,-3),(2,10)]),
    ("2x²-3x-2 > 0",lambda x: 2*x**2-3*x-2,"> 0",
     "x<-1/2 atau x>2", [(-10,-0.5),(2,10)], [(-0.5,2)]),
]
for label, f, op, answer, valid_ivs, invalid_ivs in cases_q:
    ok_valid   = all(check_interval(f if "> 0" in op else lambda x,g=f: -g(x), a,b) for a,b in valid_ivs)
    print(f"  {label}")
    print(f"    Solusi: {answer}")
    print(f"    Verifikasi interval solusi: {'✓' if ok_valid else '✗'}")

# Ex 2: Rational
print("\n[Ex 2] Selesaikan pertidaksamaan rasional:")
cases_r = [
    ("(x+3)/(x-2) ≥ 0", lambda x: (x+3)/(x-2), "x≤-3 atau x>2"),
    ("(x²-9)/(x+1) < 0", lambda x: (x**2-9)/(x+1), "-3<x<-1 atau -1<x<3 (cek!)"),
    ("1/(x-1) > 1/(x+1)", lambda x: 1/(x-1) - 1/(x+1), "x<-1 atau 0<x<1"),
]
for label, f, answer in cases_r:
    print(f"  {label}")
    print(f"    Solusi: {answer}")

# Ex 3: Domain finding using inequalities
print("\n[Ex 3] Tentukan domain fungsi (dengan pertidaksamaan):")
print("  f(x) = √((x²-5x+6)/(x-4))")
print("  Syarat: (x²-5x+6)/(x-4) ≥ 0  dan  x ≠ 4")
print("  = (x-2)(x-3)/(x-4) ≥ 0")
print("  Titik kritis: 2, 3, 4")

def g(x): return (x-2)*(x-3)/(x-4)
for xv in [1, 2, 2.5, 3, 3.5, 4, 5]:
    if abs(xv-4) < 1e-9:
        print(f"    x={xv}: UNDEFINED")
    else:
        val = g(xv)
        domain = val >= 0
        print(f"    x={xv:>5.1f}: val={val:>8.4f} ≥ 0? {domain}")

print("  Domain: [2,3] ∪ (4, ∞)")

# Ex 4: Application
print("\n[Ex 4] Soal Nyata:")
print("  Sebuah peluru ditembakkan vertikal: h(t) = -5t²+50t")
print("  Kapan peluru di ketinggian ≥ 100m?")
print("  -5t²+50t ≥ 100  =>  -5t²+50t-100 ≥ 0  =>  t²-10t+20 ≤ 0")
D = 100 - 80
t1 = (10 - math.sqrt(D))/2
t2 = (10 + math.sqrt(D))/2
print(f"  D = {D},  t = (10 ± √{D})/2")
print(f"  t1 = {t1:.4f}s,  t2 = {t2:.4f}s")
print(f"  Solusi: {t1:.4f} ≤ t ≤ {t2:.4f} detik")

print("\n[Selesai]")
