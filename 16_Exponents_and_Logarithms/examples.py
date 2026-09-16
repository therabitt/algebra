"""
Module  : Exponents and Logarithms (Eksponen dan Logaritma)
Phase   : 1 - Algebra  |  Topic: 1.11
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("EKSPONEN DAN LOGARITMA — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Hukum Eksponen ────────────────────────────────────────
print("\n[1] 7 Hukum Eksponen")
a, b, m, n = 2, 3, 4, 3
print(f"  a={a}, b={b}, m={m}, n={n}")
print(f"  1. a^m * a^n = a^(m+n): {a**m}*{a**n} = {a**m*a**n} = {a**(m+n)}")
print(f"  2. a^m / a^n = a^(m-n): {a**m}/{a**n} = {a**m/a**n} = {a**(m-n)}")
print(f"  3. (a^m)^n  = a^(mn):   ({a}^{m})^{n} = {(a**m)**n} = {a**(m*n)}")
print(f"  4. (ab)^n   = a^n*b^n:  ({a}*{b})^{n} = {(a*b)**n} = {a**n}*{b**n}={a**n*b**n}")
print(f"  5. a^0      = 1:        {a}^0 = {a**0}")
print(f"  6. a^(-n)   = 1/a^n:    {a}^(-2) = {a**(-2)} = 1/{a**2}")
print(f"  7. a^(1/n)  = nth root: {a}^(1/2) = {a**(0.5):.6f} = √{a}")

# ─── 2. Bilangan e ────────────────────────────────────────────
print("\n[2] Bilangan e = lim(1+1/n)^n saat n->∞")
for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    approx = (1 + 1/n)**n
    print(f"  n={n:>10}: (1+1/n)^n = {approx:.10f}  (e = {math.e:.10f})")

# ─── 3. Fungsi Eksponensial ───────────────────────────────────
print("\n[3] Fungsi Eksponensial: f(x) = a^x")
print(f"  {'x':>5} | {'2^x':>12} | {'e^x':>12} | {'(0.5)^x':>12}")
for x in [-3, -2, -1, 0, 1, 2, 3]:
    print(f"  {x:>5} | {2**x:>12.4f} | {math.e**x:>12.4f} | {0.5**x:>12.4f}")

# ─── 4. Definisi Logaritma ────────────────────────────────────
print("\n[4] Logaritma: log_b(x) = y  ↔  b^y = x")
pairs = [(2, 8), (10, 1000), (math.e, math.e**3), (3, 81)]
for base, val in pairs:
    log_val = math.log(val, base)
    verify = base**log_val
    print(f"  log_{base:.3g}({val:.4g}) = {log_val:.4f}  (cek: {base:.3g}^{log_val:.4f} = {verify:.6f})")

# ─── 5. Hukum Logaritma ───────────────────────────────────────
print("\n[5] Hukum Logaritma (basis 10)")
a, b = 100, 1000
print(f"  1. log(a*b) = log(a)+log(b): log({a*b}) = {math.log10(a*b):.4f} = {math.log10(a):.4f}+{math.log10(b):.4f}")
print(f"  2. log(a/b) = log(a)-log(b): log({a/b}) = {math.log10(a/b):.4f} = {math.log10(a):.4f}-{math.log10(b):.4f}")
print(f"  3. log(a^n) = n*log(a):      log({a}^3) = {math.log10(a**3):.4f} = 3*{math.log10(a):.4f}")
print(f"  4. Perubahan basis: log_b(x) = log(x)/log(b)")
print(f"     log_2(8) = log(8)/log(2) = {math.log(8):.4f}/{math.log(2):.4f} = {math.log(8)/math.log(2):.4f}")

# ─── 6. Menyelesaikan Persamaan Eksponen ─────────────────────
print("\n[6] Menyelesaikan Persamaan Eksponen")
print("  2^x = 32  ->  x = log_2(32) = 5")
print(f"  Verifikasi: 2^5 = {2**5}")
print("  3^(2x+1) = 243  ->  2x+1 = log_3(243) = 5  ->  x = 2")
x = (math.log(243)/math.log(3) - 1) / 2
print(f"  Verifikasi: 3^(2*{x}+1) = {3**(2*x+1):.0f}")
print("  e^(x-1) = 10  ->  x-1 = ln(10)  ->  x = ln(10)+1")
x = math.log(10) + 1
print(f"  x = {x:.6f},  e^(x-1) = {math.e**(x-1):.6f}")

# ─── 7. Pertumbuhan Eksponensial ──────────────────────────────
print("\n[7] Model Pertumbuhan & Peluruhan: P(t) = P0 * e^(kt)")
P0 = 1000   # populasi awal
k_growth = 0.05   # laju tumbuh 5% per tahun
k_decay  = -0.03  # laju luruh -3% per tahun
print(f"  Populasi awal P0={P0}, k={k_growth}")
print(f"  {'t (tahun)':>12} | {'Pertumbuhan':>14} | {'Peluruhan':>12}")
for t in [0, 5, 10, 20, 50]:
    grow = P0 * math.e**(k_growth*t)
    decay = P0 * math.e**(k_decay*t)
    print(f"  {t:>12} | {grow:>14.2f} | {decay:>12.2f}")

# ─── 8. Aplikasi Nyata ────────────────────────────────────────
print("\n[8] Aplikasi Nyata Logaritma")
print("  pH = -log10([H+])")
for h_conc, substance in [(1e-7,"air murni"),(1e-3,"cuka"),(1e-12,"pemutih")]:
    print(f"  [{substance}] [H+]={h_conc:.0e}  ->  pH={-math.log10(h_conc):.1f}")

print("\n  Skala Richter: M = log10(I/I0)")
for ratio, event in [(1e3,"gempa kecil"),(1e6,"gempa menengah"),(1e9,"gempa besar")]:
    M = math.log10(ratio)
    print(f"  I/I0={ratio:.0e}  ->  M={M:.1f}  ({event})")

print("\n  Desibel: dB = 10*log10(P/P0)")
for ratio, sound in [(1,"batas pendengaran"),(1e6,"percakapan normal"),(1e12,"pesawat jet")]:
    dB = 10*math.log10(ratio) if ratio > 0 else 0
    print(f"  P/P0={ratio:.0e}  ->  {dB:.0f} dB  ({sound})")

print("\n[Selesai]")
