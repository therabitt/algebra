"""
Exercises: Linear Inequalities  |  Phase 1 — Topic 1.5
"""
print("LATIHAN 1.5 — PERTIDAKSAMAAN LINEAR")
print("=" * 50)

def flip_op(op):
    return {"<":">", ">":"<", "<=":">=", ">=":"<="}[op]

# Ex 1
print("\n[Ex 1] Selesaikan pertidaksamaan:")
cases = [
    ("3x - 7 > 8",   lambda: (8+7)/3,   ">"),
    ("-2x + 4 <= 10", lambda: (10-4)/-2, ">="),
    ("5x + 3 < 3",   lambda: (3-3)/5,   "<"),
    ("x/4 >= -2",    lambda: -2*4,      ">="),
]
for label, solver, op_orig in cases:
    val = solver()
    # Flip if needed (for -2x case)
    print(f"  {label}  ->  check manual answer")

# Solutions
print("  SOLUTIONS:")
print("  3x-7>8   ->  x > 5")
print("  -2x+4<=10 -> x >= -3  (tanda BALIK karena bagi -2)")
print("  5x+3<3   ->  x < 0")
print("  x/4>=-2  ->  x >= -8")

# Ex 2 — compound
print("\n[Ex 2] Compound inequalities:")
print("  -3 < 2x+1 < 9")
print("  -3-1 < 2x < 9-1  ->  -4 < 2x < 8  ->  -2 < x < 4")
print("  Interval: (-2, 4)")
print("  Cek x=0:", -2 < 0 < 4)
print("  Cek x=-3:", -2 < -3 < 4)

# Ex 3 — absolute value
print("\n[Ex 3] Pertidaksamaan nilai mutlak:")
print("  |2x - 3| <= 5")
print("  -5 <= 2x-3 <= 5  ->  -2 <= 2x <= 8  ->  -1 <= x <= 4")
print("  Interval: [-1, 4]")
for x in [-2, -1, 0, 2, 4, 5]:
    inside = abs(2*x - 3) <= 5
    print(f"  x={x:3}: |2({x})-3|={abs(2*x-3)} <= 5? {inside}")

# Ex 4 — real world
print("\n[Ex 4] Soal nyata:")
print("  Toko memberikan diskon jika total belanja > 200.000.")
print("  Harga barang Rp 45.000 per item. Berapa minimum item?")
min_items = 200000 / 45000
import math
print(f"  45000n > 200000  ->  n > {min_items:.4f}  ->  n >= {math.ceil(min_items)+1}")
print(f"  Minimum beli {math.ceil(min_items)+1} item")

print("\n[Selesai]")
