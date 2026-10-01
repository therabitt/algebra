"""
Exercises: Number Systems — SOLUTION FILE
Phase 1 — Topic 1.1
[Jangan buka sebelum mencoba sendiri!]
"""
import math
import fractions

print("=" * 60)
print("LATIHAN 1.1 — SISTEM BILANGAN [SOLUSI]")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# Exercise 1: Klasifikasi Bilangan
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 1] Klasifikasi bilangan:")
numbers = {
    "-7"  : (-7, "Z (bulat), Q (rasional), R (real), C (kompleks)"),
    "0"   : (0,  "W (cacah), Z, Q, R, C"),
    "3/4" : (fractions.Fraction(3,4), "Q (rasional), R, C"),
    "√5"  : (math.sqrt(5), "Irasional, R, C"),
    "2+3i": (complex(2,3), "C (kompleks) saja"),
    "-3/1": (-3, "Z, Q, R, C"),
}
for name, (val, systems) in numbers.items():
    print(f"  {name:8} ∈ {systems}")

# ─────────────────────────────────────────────────────────────
# Exercise 2: Desimal Berulang ke Pecahan
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 2] Desimal berulang ke pecahan:")
# a) x = 0.666... → 10x = 6.666... → 9x = 6 → x = 6/9 = 2/3
a = fractions.Fraction(6, 9)
print(f"  a) 0.666...    = {a} = {float(a):.6f}")
# b) x = 0.272727... → 100x = 27.272727... → 99x = 27 → x = 27/99 = 3/11
b = fractions.Fraction(27, 99)
print(f"  b) 0.272727... = {b} = {float(b):.6f}")
# c) 10x=5.833..., 100x=58.333..., 90x=53 → x=53/90
c = fractions.Fraction(53, 90)
print(f"  c) 0.58333...  = {c} = {float(c):.6f}")

# ─────────────────────────────────────────────────────────────
# Exercise 3: Operasi Bilangan Kompleks
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 3] Operasi bilangan kompleks:")
z1 = complex(4, 3)
z2 = complex(2, -1)
print(f"  z1={z1}, z2={z2}")
print(f"  a) z1 + z2 = {z1 + z2}")
print(f"  b) z1 × z2 = {z1 * z2}")
print(f"  c) |z1|   = {abs(z1)}")
div = z1 / z2
print(f"  d) z1/z2  = {div.real:.4f} + {div.imag:.4f}i")

# ─────────────────────────────────────────────────────────────
# Exercise 4: Keanggotaan Interval
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 4] Keanggotaan interval (x=4):")
x = 4
print(f"  a) [2, 4]  : {2 <= x <= 4}   (ya, ujung tertutup)")
print(f"  b) (2, 4)  : {2 < x < 4}  (tidak, ujung terbuka)")
print(f"  c) [4, 7)  : {4 <= x < 7}   (ya, ujung kiri tertutup)")
print(f"  d) (4, 7]  : {4 < x <= 7}  (tidak, ujung kiri terbuka)")

# ─────────────────────────────────────────────────────────────
# Exercise 5: Floor dan Ceiling
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 5] Floor ⌊x⌋ dan Ceiling ⌈x⌉:")
for v in [2.9, -1.2, 5.0, -3.0]:
    print(f"  x = {v:5.1f}: ⌊x⌋ = {math.floor(v):3d}, ⌈x⌉ = {math.ceil(v):3d}")

# ─────────────────────────────────────────────────────────────
# Exercise 6: Sifat Klosure
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 6] Sifat klosure:")
print(f"  a) N tertutup -?  FALSE  (contoh: 2 - 5 = {2-5}, bukan asli)")
print(f"  b) Z tertutup ×?  TRUE   (bulat × bulat = bulat selalu)")
print(f"  c) Q tertutup ÷?  TRUE   (asal pembagi ≠ 0)")
val = math.sqrt(2) * math.sqrt(2)
print(f"  d) Irasional ×?   FALSE  (√2 × √2 = {val:.6f} = 2, rasional!)")

print("\n[Selesai] SOLUTION FILE")
