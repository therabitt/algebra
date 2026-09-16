"""
Challenge: Quadratic Equations  |  Phase 1 — Topic 1.6
"""
import math
print("CHALLENGE 1.6 — PERSAMAAN KUADRAT")

# Challenge 1: Depressed Cubic intro (hubungan dengan kuadrat)
print("\n[Ch1] Dari Kuadrat ke Kubik: Formula Cardano (preview)")
print("  Persamaan kubik: t^3 + pt + q = 0")
print("  Diskriminan: D = -(4p^3 + 27q^2)")

def cardano_depressed(p, q):
    """Selesaikan t^3 + pt + q = 0 (depressed cubic)"""
    D = -(4*p**3 + 27*q**2)
    print(f"  t^3 + {p}t + {q} = 0,  D = {D:.4f}")
    # Cardano: t = cbrt(-q/2 + sqrt(q^2/4 + p^3/27)) + cbrt(-q/2 - sqrt(q^2/4 + p^3/27))
    inner = (q/2)**2 + (p/3)**3
    if inner >= 0:
        r1 = (-q/2 + math.sqrt(inner))**(1/3) if (-q/2+math.sqrt(inner))>=0 else -((-(-q/2+math.sqrt(inner)))**(1/3))
        r2 = (-q/2 - math.sqrt(inner))**(1/3) if (-q/2-math.sqrt(inner))>=0 else -((-(-q/2-math.sqrt(inner)))**(1/3))
        t = r1 + r2
        print(f"  Akar real: t ≈ {t:.6f}")
        print(f"  Verifikasi: t^3+{p}t+{q} = {t**3+p*t+q:.6f}")
    else:
        print(f"  Tiga akar real (casus irreducibilis) — butuh bilangan kompleks")

cardano_depressed(-3, 2)
cardano_depressed(1, -1)

# Challenge 2: Newton-Raphson untuk akar kuadrat
print("\n[Ch2] Newton-Raphson untuk menyelesaikan ax^2+bx+c=0")
def newton_raphson_quadratic(a, b, c, x0=1.0, tol=1e-10, max_iter=100):
    """
    Temukan akar ax^2+bx+c=0 menggunakan Newton-Raphson.
    f(x) = ax^2+bx+c,  f'(x) = 2ax+b
    x_{n+1} = x_n - f(x_n)/f'(x_n)
    """
    def f(x):  return a*x**2 + b*x + c
    def df(x): return 2*a*x + b
    x = x0
    print(f"  a={a}, b={b}, c={c}, start x0={x0}")
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-15:
            print("  Derivatif = 0, berhenti"); break
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            print(f"  Konvergen setelah {i+1} iterasi: x = {x_new:.10f}")
            print(f"  Verifikasi: f(x) = {f(x_new):.2e}")
            return x_new
        x = x_new
    return x

newton_raphson_quadratic(1, -5, 6, x0=4)    # x=3
newton_raphson_quadratic(1, -5, 6, x0=1)    # x=2
newton_raphson_quadratic(2, -4, -6, x0=5)   # x=3

print("\n[Selesai Challenge 1.6]")
