"""
Exercises: Quadratic Equations  |  Phase 1 — Topic 1.6
"""
import math
print("LATIHAN 1.6 — PERSAMAAN KUADRAT")
print("=" * 50)

def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        re = -b/(2*a)
        im = math.sqrt(-D)/(2*a)
        return (complex(re, im), complex(re, -im)), D
    elif D == 0:
        r = -b/(2*a)
        return (r, r), D
    else:
        r1 = (-b + math.sqrt(D))/(2*a)
        r2 = (-b - math.sqrt(D))/(2*a)
        return (r1, r2), D

# Ex 1: solve by factoring
print("\n[Ex 1] Faktorisasi: x^2 + 5x + 6 = 0")
print("  (x+2)(x+3) = 0  ->  x=-2 atau x=-3")
r, D = quadratic_roots(1, 5, 6)
print(f"  Verifikasi: roots={r}, D={D}")

# Ex 2: completing the square
print("\n[Ex 2] Melengkapi Kuadrat: x^2 - 6x + 5 = 0")
print("  x^2 - 6x = -5")
print("  x^2 - 6x + 9 = -5 + 9 = 4  (tambah (6/2)^2=9)")
print("  (x-3)^2 = 4  ->  x-3 = ±2  ->  x=5 atau x=1")
r, D = quadratic_roots(1, -6, 5)
print(f"  Verifikasi: roots={r}")

# Ex 3: quadratic formula
print("\n[Ex 3] Rumus ABC: 2x^2 - 4x - 6 = 0")
a,b,c = 2,-4,-6
D = b**2-4*a*c
print(f"  D = {b}^2 - 4({a})({c}) = {D}")
print(f"  x = ({-b} ± √{D}) / {2*a}")
r, _ = quadratic_roots(a,b,c)
print(f"  x1={r[0]}, x2={r[1]}")

# Ex 4: complex roots
print("\n[Ex 4] Akar Kompleks: x^2 + 4 = 0")
r, D = quadratic_roots(1, 0, 4)
print(f"  D = {D} < 0 -> akar kompleks")
print(f"  x = ±2i  ->  {r}")

# Ex 5: Vieta's formulas
print("\n[Ex 5] Formula Vieta: ax^2+bx+c=0")
print("  x1+x2 = -b/a,  x1*x2 = c/a")
for (a,b,c) in [(1,-5,6),(2,3,-2),(1,0,-9)]:
    r, D = quadratic_roots(a,b,c)
    if D >= 0:
        x1,x2 = r
        print(f"  {a}x^2+{b}x+{c}: sum={x1+x2:.4g} (=-b/a={-b/a:.4g}), "
              f"prod={x1*x2:.4g} (=c/a={c/a:.4g})")

# Ex 6: vertex and max/min
print("\n[Ex 6] Vertex dari f(x) = -3x^2 + 12x - 5")
a,b,c = -3,12,-5
h = -b/(2*a)   # x-vertex
k = a*h**2 + b*h + c  # y-vertex
print(f"  h = -b/2a = {h:.4g}")
print(f"  k = f(h) = {k:.4g}")
print(f"  Vertex: ({h}, {k})")
print(f"  {'Maksimum' if a < 0 else 'Minimum'} = {k} di x = {h}")

# Ex 7: projectile
print("\n[Ex 7] Soal Proyektil: h(t) = -5t^2 + 20t + 15 (meter)")
print("  (a) Kapan mencapai tanah? h(t)=0")
roots, D = quadratic_roots(-5, 20, 15)
t_land = max(r for r in roots if isinstance(r,(int,float)) and r >= 0)
print(f"  t = {t_land:.4g} detik")
print("  (b) Ketinggian maksimum?")
h_func = lambda t: -5*t**2 + 20*t + 15
t_max = -20/(2*-5)
h_max = h_func(t_max)
print(f"  t_max={t_max}s, h_max={h_max}m")

print("\n[Selesai]")
