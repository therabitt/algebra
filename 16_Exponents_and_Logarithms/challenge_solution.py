"""
Challenge: Exponents and Logarithms  |  Phase 1 — Topic 1.11
"""
import math
print("CHALLENGE 1.11 — EKSPONEN DAN LOGARITMA")

# Challenge 1: Compute e from scratch
print("\n[Ch1] Menghitung e dari deret Taylor")
print("  e = sum(1/n!) untuk n=0,1,2,...")

def compute_e(terms=20):
    e_approx = 0
    factorial = 1
    for n in range(terms):
        if n > 0: factorial *= n
        e_approx += 1 / factorial
        if n % 5 == 4:
            print(f"  n={n:>3}: e ≈ {e_approx:.15f}")
    return e_approx

e_calc = compute_e(20)
print(f"  e kalkulasi = {e_calc:.15f}")
print(f"  e aktual    = {math.e:.15f}")
print(f"  Error       = {abs(e_calc-math.e):.2e}")

# Challenge 2: Compute ln from scratch (Newton's method)
print("\n[Ch2] Menghitung ln(x) menggunakan Newton-Raphson")
print("  Cari y sehingga e^y = x, yaitu: f(y)=e^y-x, f'(y)=e^y")
def my_ln(x, tol=1e-12, max_iter=100):
    if x <= 0: raise ValueError("ln(x) hanya untuk x > 0")
    y = 1.0  # initial guess
    for i in range(max_iter):
        ey = math.e ** y
        y_new = y - (ey - x) / ey
        if abs(y_new - y) < tol:
            return y_new, i+1
        y = y_new
    return y, max_iter

for val in [1, math.e, 2, 10, 100]:
    result, iters = my_ln(val)
    print(f"  ln({val:>8.4f}) = {result:.10f}  (actual: {math.log(val):.10f}, iters={iters})")

# Challenge 3: Logistic growth model
print("\n[Ch3] Model Pertumbuhan Logistik (Logistic Growth)")
print("  dP/dt = rP(1 - P/K)  ->  P(t) = K/(1 + ((K-P0)/P0)*e^(-rt))")
def logistic(P0, K, r, t):
    """Carrying capacity model."""
    return K / (1 + ((K-P0)/P0) * math.e**(-r*t))

P0, K, r = 100, 10000, 0.3
print(f"  P0={P0}, K={K} (carrying capacity), r={r}")
print(f"  {'t':>5} | {'P(t)':>12} | {'% kapasitas':>12}")
for t in [0, 5, 10, 15, 20, 30, 50]:
    P = logistic(P0, K, r, t)
    print(f"  {t:>5} | {P:>12.2f} | {P/K*100:>11.1f}%")

print("\n[Selesai Challenge 1.11]")
