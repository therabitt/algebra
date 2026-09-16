"""
Module  : Linear Inequalities (Pertidaksamaan Linear)
Phase   : 1 - Algebra  |  Topic: 1.5
Jalankan: python3 examples.py
"""
print("=" * 60)
print("PERTIDAKSAMAAN LINEAR — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Sifat-sifat Pertidaksamaan ────────────────────────────
print("\n[1] Sifat Pertidaksamaan — Termasuk FLIP TANDA!")

a, b = 3, 7
print(f"Mulai: {a} < {b}")
print(f"  Tambah 5: {a+5} < {b+5}  (tanda tetap)")
print(f"  Kurangi 2: {a-2} < {b-2}  (tanda tetap)")
print(f"  Kali 3: {a*3} < {b*3}  (tanda tetap, positif)")
print(f"  Kali -2: {a*-2} > {b*-2}  ← TANDA BALIK! (kali negatif)")
print(f"  Bagi 2: {a/2} < {b/2}  (tanda tetap, positif)")
print(f"  Bagi -1: {a/-1} > {b/-1}  ← TANDA BALIK! (bagi negatif)")

# ─── 2. Menyelesaikan pertidaksamaan linear ───────────────────
print("\n[2] Menyelesaikan ax + b < c")

def solve_inequality(a, b, c, op="<"):
    """Selesaikan ax + b {op} c"""
    # ax < c - b  ->  x < (c-b)/a  (perhatikan flip jika a < 0)
    rhs = c - b
    if a == 0:
        # 0 < rhs: all real; 0 > rhs: no solution
        return "Semua real" if eval(f"0 {op} {rhs}") else "Tidak ada solusi"
    val = rhs / a
    # Jika a negatif, balik operator
    if a < 0:
        flip = {"<": ">", ">": "<", "<=": ">=", ">=": "<="}
        op = flip[op]
    return f"x {op} {val:.4g}"

examples = [
    (2, 3, 11, "<",  "2x + 3 < 11"),
    (-3, 6, 0, ">",  "-3x + 6 > 0"),
    (4, -8, 0, ">=", "4x - 8 >= 0"),
    (1, 0, 5,  "<=", "x <= 5"),
]
for a,b,c,op,label in examples:
    sol = solve_inequality(a, b, c, op)
    print(f"  {label}  ->  {sol}")

# ─── 3. Compound Inequalities ─────────────────────────────────
print("\n[3] Pertidaksamaan Majemuk (Compound)")
print("  AND: a < x < b  (x di antara a dan b)")
print("  OR : x < a ATAU x > b")

def in_compound_and(x, a, b):
    return a < x < b

def in_compound_or(x, a, b):
    return x < a or x > b

test_vals = [-5, -1, 0, 2, 4, 7]
print("  AND: -2 < x < 5")
print("  OR : x < -2 ATAU x > 5")
print(f"  {'x':>5} | {'AND':>6} | {'OR':>6}")
for v in test_vals:
    print(f"  {v:>5} | {str(in_compound_and(v,-2,5)):>6} | {str(in_compound_or(v,-2,5)):>6}")

# ─── 4. Pertidaksamaan Nilai Mutlak ───────────────────────────
print("\n[4] Pertidaksamaan Nilai Mutlak")
print("  |x| < a  ↔  -a < x < a")
print("  |x| > a  ↔  x < -a ATAU x > a")
print("  |x - k| < d  ↔  k-d < x < k+d  (jarak dari k < d)")

def abs_ineq_less(x, a):
    """Apakah |x| < a?"""
    return abs(x) < a

def abs_ineq_greater(x, a):
    """Apakah |x| > a?"""
    return abs(x) > a

print("\n  |x| < 3: solusi -3 < x < 3")
vals = [-4, -3, -1, 0, 2, 3, 4]
print(f"  {'x':>5} | {'|x|<3':>8} | {'|x|>3':>8}")
for v in vals:
    print(f"  {v:>5} | {str(abs_ineq_less(v,3)):>8} | {str(abs_ineq_greater(v,3)):>8}")

# ─── 5. Interval Notation ─────────────────────────────────────
print("\n[5] Notasi Interval dari Solusi")

def to_interval(a_coef, b_const, c_rhs, op):
    sol = solve_inequality(a_coef, b_const, c_rhs, op)
    # Ekstrak nilai dari string solusi
    parts = sol.split()
    if len(parts) >= 3:
        val = float(parts[2])
        op_sym = parts[1]
        if op_sym == "<":  return f"(-∞, {val})"
        if op_sym == ">":  return f"({val}, +∞)"
        if op_sym == "<=": return f"(-∞, {val}]"
        if op_sym == ">=": return f"[{val}, +∞)"
    return sol

for a,b,c,op,label in examples:
    interval = to_interval(a, b, c, op)
    print(f"  {label}  ->  {interval}")

# ─── 6. Two-variable linear inequality ───────────────────────
print("\n[6] Pertidaksamaan Dua Variabel ax + by < c")
print("  Solusi: setengah bidang (half-plane)")
print("  Contoh: 2x + 3y <= 12")

def in_half_plane(x, y, a, b, c):
    """Apakah (x,y) memenuhi ax + by <= c?"""
    return a*x + b*y <= c

test_points = [(0,0),(3,2),(5,1),(1,3),(6,0)]
print("  Cek titik-titik untuk 2x + 3y <= 12:")
for px, py in test_points:
    inside = in_half_plane(px, py, 2, 3, 12)
    val = 2*px + 3*py
    print(f"  ({px},{py}): 2({px})+3({py})={val}  <= 12? {inside}")

print("\n[Selesai] Lanjut ke exercises.py")
