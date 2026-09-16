"""
Exercises: Complex Numbers  |  Phase 1 — Topic 1.18
"""
import math, cmath
print("LATIHAN 1.18 — BILANGAN KOMPLEKS")
print("=" * 50)

# Ex 1: Operations
print("\n[Ex 1] Hitung:")
z1, z2 = 2+3j, 1-4j
print(f"  z1={z1}, z2={z2}")
print(f"  z1+z2 = {z1+z2}")
print(f"  z1×z2 = {z1*z2}")
print(f"  z1/z2 = {z1/z2:.4f}")
print(f"  |z1|  = {abs(z1):.4f}")
print(f"  z1·z̄1 = {z1*z1.conjugate():.1f}  (= |z1|² = {abs(z1)**2:.1f})")

# Ex 2: Polar form
print("\n[Ex 2] Konversikan ke bentuk polar r·e^(iθ):")
numbers = [1+1j, -1+0j, 0-2j, 3+4j]
for z in numbers:
    r = abs(z)
    theta = cmath.phase(z)
    print(f"  {str(z):>10}: r={r:.4f}, θ={math.degrees(theta):.2f}°  → {r:.4f}·e^(i·{theta:.4f})")
    # Verify
    reconstructed = r * cmath.exp(1j*theta)
    print(f"             Rekonstruksi: {reconstructed.real:.4f}+{reconstructed.imag:.4f}i ✓{abs(reconstructed-z)<1e-10}")

# Ex 3: De Moivre
print("\n[Ex 3] Gunakan De Moivre untuk hitung (1+i)^8:")
z = 1 + 1j
r = abs(z); theta = cmath.phase(z)
print(f"  1+i: r={r:.4f}, θ={math.degrees(theta):.2f}°")
result = r**8 * cmath.exp(8j*theta)
print(f"  (1+i)^8 = {r:.4f}^8 · e^(i·8·{math.degrees(theta):.2f}°)")
print(f"          = {r**8:.4f} · e^(i·{8*math.degrees(theta):.2f}°)")
print(f"          = {result:.4f}")
print(f"  Direct:  {z**8:.4f}  ✓{abs(result-z**8)<1e-8}")

# Ex 4: nth roots
print("\n[Ex 4] Temukan semua akar kuadrat dari i:")
print("  z² = i = e^(iπ/2)")
print("  z_k = e^(i(π/2 + 2πk)/2) = e^(i(π/4 + πk))")
for k in range(2):
    z = cmath.exp(1j * (math.pi/4 + math.pi*k))
    print(f"  k={k}: z = {z.real:.6f}+{z.imag:.6f}i,  z² = {(z**2).real:.6f}+{(z**2).imag:.2e}i")

# Ex 5: Fundamental theorem demo
print("\n[Ex 5] Teorema Fundamental Aljabar:")
print("  z^3 - 1 = 0 memiliki TEPAT 3 akar di ℂ:")
roots = [cmath.exp(2j*math.pi*k/3) for k in range(3)]
for k, r in enumerate(roots):
    check = r**3 - 1
    print(f"  z{k} = {r.real:.6f}+{r.imag:.6f}i,  z³-1 = {check.real:.2e}+{check.imag:.2e}i")

print("\n[Selesai]")
