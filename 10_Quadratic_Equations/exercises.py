"""
Exercises: Quadratic Equations  |  Phase 1 — Topic 1.6
"""
import math
print("LATIHAN 1.6 — PERSAMAAN KUADRAT")
print("=" * 50)

# KONSEP: Diskriminan D = b^2 - 4ac menentukan jenis akar persamaan kuadrat.
# Jika D < 0: 2 akar kompleks. Jika D == 0: 1 akar kembar. Jika D > 0: 2 akar real berbeda.
#
# LANGKAH:
# 1. Hitung nilai diskriminan D.
# 2. Cek apakah D < 0. Jika ya, hitung bagian real (-b/2a) dan imajiner (√(-D)/2a), return tuple akar kompleks.
# 3. Cek apakah D == 0. Jika ya, hitung akar ganda (-b/2a) dan return.
# 4. Jika D > 0, hitung r1 dan r2 menggunakan rumus ABC (-b ± √D)/2a dan return.
# 5. Return juga nilai D bersama akar-akarnya (misal: return akar_tuple, D).
#
# IMPLEMENTASIKAN:
def quadratic_roots(a, b, c):
    pass

# Ex 1: solve by factoring
print("\n[Ex 1] Faktorisasi: x^2 + 5x + 6 = 0")
print("  (x+2)(x+3) = 0  ->  x=-2 atau x=-3")
# TODO: Panggil quadratic_roots untuk memverifikasi akar persamaan x^2 + 5x + 6 = 0
r, D = None, None
print(f"  Verifikasi: roots={r}, D={D}")
# Jawaban: roots=(-2.0, -3.0), D=1

# Ex 2: completing the square
print("\n[Ex 2] Melengkapi Kuadrat: x^2 - 6x + 5 = 0")
print("  x^2 - 6x = -5")
print("  x^2 - 6x + 9 = -5 + 9 = 4  (tambah (6/2)^2=9)")
print("  (x-3)^2 = 4  ->  x-3 = ±2  ->  x=5 atau x=1")
# TODO: Panggil quadratic_roots untuk x^2 - 6x + 5 = 0
r, D = None, None
print(f"  Verifikasi: roots={r}")
# Jawaban: roots=(5.0, 1.0)

# Ex 3: quadratic formula
print("\n[Ex 3] Rumus ABC: 2x^2 - 4x - 6 = 0")
a,b,c = 2,-4,-6
# TODO: Hitung D secara manual dan panggil quadratic_roots
D_manual = None
print(f"  D = {b}^2 - 4({a})({c}) = {D_manual}")
print(f"  x = ({-b} ± √{D_manual}) / {2*a}")
# r, _ = quadratic_roots(a,b,c)
# print(f"  x1={r[0]}, x2={r[1]}")
# Jawaban: x1=3.0, x2=-1.0, D=64

# Ex 4: complex roots
print("\n[Ex 4] Akar Kompleks: x^2 + 4 = 0")
# TODO: Panggil quadratic_roots untuk x^2 + 4 = 0
# r, D = quadratic_roots(1, 0, 4)
# print(f"  D = {D} < 0 -> akar kompleks")
# print(f"  x = ±2i  ->  {r}")
# Jawaban: D=-16, roots=(2j, -2j)

# Ex 5: Vieta's formulas
print("\n[Ex 5] Formula Vieta: ax^2+bx+c=0")
print("  x1+x2 = -b/a,  x1*x2 = c/a")
# TODO: Gunakan quadratic_roots untuk menguji (1,-5,6), (2,3,-2), (1,0,-9)
#       dan buktikan bahwa x1+x2 = -b/a dan x1*x2 = c/a

# Ex 6: vertex and max/min
print("\n[Ex 6] Vertex dari f(x) = -3x^2 + 12x - 5")
a,b,c = -3,12,-5
# KONSEP: Koordinat titik puncak (vertex) parabol y = ax^2 + bx + c ada di x = -b/2a.
# Nilai optimum (maks/min) adalah y = f(x_vertex).
#
# LANGKAH:
# 1. Hitung h = -b/2a
# 2. Hitung k = a*h^2 + b*h + c
#
# IMPLEMENTASIKAN:
h = None
k = None
print(f"  h = -b/2a = {h}")
print(f"  k = f(h) = {k}")
print(f"  Vertex: ({h}, {k})")
# Jawaban: h=2.0, k=7.0, Maksimum = 7.0 di x = 2.0

# Ex 7: projectile
print("\n[Ex 7] Soal Proyektil: h(t) = -5t^2 + 20t + 15 (meter)")
print("  (a) Kapan mencapai tanah? h(t)=0")
# TODO: Cari akar positif dari -5t^2 + 20t + 15 = 0
t_land = None
print(f"  t = {t_land} detik")
# Jawaban: t=4.562 detik (akar positif)

print("  (b) Ketinggian maksimum?")
# TODO: Cari titik puncak h(t) = -5t^2 + 20t + 15
t_max = None
h_max = None
print(f"  t_max={t_max}s, h_max={h_max}m")
# Jawaban: t_max=2.0s, h_max=35.0m

print("\n[Selesai]")
