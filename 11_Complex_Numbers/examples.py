"""
Module  : Complex Numbers (Bilangan Kompleks)
Phase   : 1 - Algebra  |  Topic: 1.18
Jalankan: python3 examples.py
"""
import math
import cmath   # Python's complex math module

print("=" * 60)
print("BILANGAN KOMPLEKS — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Representasi dan Operasi Dasar ───────────────────────
print("\n[1] Representasi dan Operasi Dasar")

z1 = 3 + 4j
z2 = 1 - 2j
print(f"  z1 = {z1},  Re(z1) = {z1.real},  Im(z1) = {z1.imag}")
print(f"  z2 = {z2},  Re(z2) = {z2.real},  Im(z2) = {z2.imag}")
print(f"\n  z1 + z2 = {z1 + z2}")
print(f"  z1 - z2 = {z1 - z2}")
print(f"  z1 × z2 = {z1 * z2}")
print(f"  z1 / z2 = {z1 / z2}")

# ─── 2. Konjugat dan Modulus ──────────────────────────────────
print("\n[2] Konjugat, Modulus, dan Argument")

numbers = [3+4j, -2+2j, 5+0j, 0-3j, 1+1j]
print(f"  {'z':>10} | {'z̄ (conj)':>12} | {'|z|':>8} | {'arg(z) rad':>12} | {'arg° deg':>10}")
print("  " + "-"*60)
for z in numbers:
    conj = z.conjugate()
    mod = abs(z)
    arg_rad = cmath.phase(z)
    arg_deg = math.degrees(arg_rad)
    print(f"  {str(z):>10} | {str(conj):>12} | {mod:>8.4f} | {arg_rad:>12.4f} | {arg_deg:>10.4f}")

# ─── 3. Euler Formula & Bentuk Polar ─────────────────────────
print("\n[3] Formula Euler: e^(iθ) = cos(θ) + i·sin(θ)")

angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]
angle_labels = ["0", "π/6", "π/4", "π/3", "π/2", "π", "3π/2", "2π"]
print(f"  {'θ':>6} | {'e^iθ':>22} | {'cos+i·sin':>22} | {'Match?':>7}")
for theta, label in zip(angles, angle_labels):
    euler = cmath.exp(1j * theta)
    manual = complex(math.cos(theta), math.sin(theta))
    match = abs(euler - manual) < 1e-10
    print(f"  {label:>6} | {euler.real:>9.4f}+{euler.imag:>9.4f}i | "
          f"{manual.real:>9.4f}+{manual.imag:>9.4f}i | {match}")

# ─── 4. Rumus Euler yang Paling Indah ─────────────────────────
print("\n[4] Euler's Identity: e^(iπ) + 1 = 0")
result = cmath.exp(1j * math.pi) + 1
print(f"  e^(iπ) = {cmath.exp(1j*math.pi)}")
print(f"  e^(iπ) + 1 = {result}  (≈ 0? {abs(result) < 1e-14})")
print("  Menggabungkan: e (Euler), i (imajiner), π (pi), 1, 0 — 5 konstanta terpenting!")

# ─── 5. Perkalian dalam Bentuk Polar ─────────────────────────
print("\n[5] Perkalian: Moduli × , Arguments +")

z1 = 2 * cmath.exp(1j * math.pi/3)   # r=2, θ=60°
z2 = 3 * cmath.exp(1j * math.pi/6)   # r=3, θ=30°
product = z1 * z2

print(f"  z1 = 2·e^(iπ/3):  |z1|={abs(z1):.4f}, arg={math.degrees(cmath.phase(z1)):.2f}°")
print(f"  z2 = 3·e^(iπ/6):  |z2|={abs(z2):.4f}, arg={math.degrees(cmath.phase(z2)):.2f}°")
print(f"  z1·z2 = {product:.4f}")
print(f"  |z1·z2| = {abs(product):.4f} = |z1|×|z2| = {abs(z1)*abs(z2):.4f}")
print(f"  arg(z1·z2) = {math.degrees(cmath.phase(product)):.2f}° = arg(z1)+arg(z2) = {math.degrees(cmath.phase(z1))+math.degrees(cmath.phase(z2)):.2f}°")

# ─── 6. De Moivre dan Akar-n ─────────────────────────────────
print("\n[6] Teorema De Moivre: (cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)")

# (cos30° + i sin30°)^3
theta = math.pi/6
n = 3
z = complex(math.cos(theta), math.sin(theta))
result_power = z**n
result_demoivre = complex(math.cos(n*theta), math.sin(n*theta))
print(f"  (cos30° + i·sin30°)^3 = {result_power}")
print(f"  cos(90°) + i·sin(90°) = {result_demoivre}")
print(f"  Sama? {abs(result_power - result_demoivre) < 1e-10}")

# ─── 7. Akar-n dari Bilangan Kompleks ────────────────────────
print("\n[7] Akar Kubik dari 1: z^3 = 1")
print("  3 solusi: z_k = e^(2πik/3),  k = 0, 1, 2")
roots = [cmath.exp(2j * math.pi * k / 3) for k in range(3)]
for k, root in enumerate(roots):
    print(f"  k={k}: z = {root.real:.4f} + {root.imag:.4f}i,  z^3 = {(root**3).real:.6f}+{(root**3).imag:.2e}i")

print("\n  Akar ke-4 dari -16: z^4 = -16")
print("  -16 = 16·e^(iπ)  →  z_k = 2·e^(i(π+2πk)/4)")
roots4 = [2 * cmath.exp(1j * (math.pi + 2*math.pi*k)/4) for k in range(4)]
for k, root in enumerate(roots4):
    check = root**4
    print(f"  k={k}: z = {root.real:.4f}+{root.imag:.4f}i,  z^4 = {check.real:.4f}+{check.imag:.2e}i")

# ─── 8. Mandelbrot Set Preview ────────────────────────────────
print("\n[8] Himpunan Mandelbrot: z_{n+1} = z_n² + c")
print("  Untuk tiap c ∈ ℂ, iterasi z=0 → z²+c → (z²+c)²+c → ...")
print("  c MASUK Mandelbrot jika iterasi tidak menuju ∞")

def mandelbrot_iter(c, max_iter=100):
    """Berapa iterasi sebelum |z| > 2?"""
    z = 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter  # termasuk Mandelbrot

test_points = [0+0j, 0.5+0.5j, 1+0j, -2+0j, -0.75+0.1j, 0.285+0.01j]
print(f"\n  {'c':>18} | {'Iterasi':>10} | {'Mandelbrot?':>12}")
for c in test_points:
    iters = mandelbrot_iter(c)
    in_set = iters == 100
    print(f"  {str(c):>18} | {iters:>10} | {str(in_set):>12}")

print("\n[Selesai] Lanjut ke exercises.py")
