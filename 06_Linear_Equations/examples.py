"""
Module  : Linear Equations (Persamaan Linear)
Phase   : 1 - Algebra  |  Topic: 1.4
Jalankan: python3 examples.py
"""
print("=" * 60)
print("PERSAMAAN LINEAR — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Solving ax + b = c step by step ─────────────────────
print("\n[1] Menyelesaikan ax + b = c")

def solve_linear(a, b, c, verbose=True):
    """
    Selesaikan ax + b = c
    Langkah: ax = c - b  ->  x = (c-b)/a
    """
    if a == 0:
        if b == c:
            return "Infinite solutions (identitas)"
        else:
            return "No solution (kontradiksi)"
    x = (c - b) / a
    if verbose:
        print(f"  {a}x + {b} = {c}")
        print(f"  {a}x = {c} - {b} = {c - b}")
        print(f"  x = {c - b}/{a} = {x}")
    return x

cases = [
    (2, 3, 11, "2x + 3 = 11"),
    (5, -7, 18, "5x - 7 = 18"),
    (0, 4, 4,  "0x + 4 = 4  (identitas)"),
    (0, 3, 7,  "0x + 3 = 7  (kontradiksi)"),
    (1, 0, -5, "x = -5"),
]
for a, b, c, label in cases:
    print(f"\nSolving: {label}")
    result = solve_linear(a, b, c)
    print(f"  x = {result}")

# ─── 2. Verifikasi solusi ─────────────────────────────────────
print("\n[2] Verifikasi Solusi")

def verify(a, b, c, x):
    """Verifikasi apakah x memenuhi ax + b = c"""
    lhs = a * x + b
    satisfied = abs(lhs - c) < 1e-10
    print(f"  Cek: {a}({x}) + {b} = {lhs}  == {c}? {satisfied}")
    return satisfied

verify(2, 3, 11, 4)
verify(5, -7, 18, 5)

# ─── 3. Persamaan Literal ─────────────────────────────────────
print("\n[3] Persamaan Literal (Literal Equations)")
print("  Selesaikan untuk variabel tertentu dari persamaan umum")
print("  Contoh: PV = nRT -> T = PV/(nR)")
print("  Contoh: A = (1/2)bh -> h = 2A/b")

try:
    import sympy as sp
    P,V,n,R,T = sp.symbols("P V n R T")
    eq = sp.Eq(P*V, n*R*T)
    print(f"\n  PV = nRT")
    print(f"  Solve for T: T = {sp.solve(eq, T)[0]}")
    print(f"  Solve for R: R = {sp.solve(eq, R)[0]}")
    
    A,b,h = sp.symbols("A b h", positive=True)
    eq2 = sp.Eq(A, sp.Rational(1,2)*b*h)
    print(f"\n  A = (1/2)bh")
    print(f"  Solve for h: h = {sp.solve(eq2, h)[0]}")
except ImportError:
    print("  (sympy tidak tersedia, skip)")

# ─── 4. Word Problems (Soal Cerita) ──────────────────────────
print("\n[4] Soal Cerita -> Persamaan Linear")

print("\n  Soal: Ani punya uang Rp x. Setelah membeli buku Rp 25.000")
print("  dan mendapat kembalian Rp 15.000, ia membayar Rp 40.000.")
print("  Berapa nilai x?")
print("  Model: x - 25000 = 40000 - 15000  ->  x = 50000")
x = solve_linear(1, -25000, 40000 - 15000, verbose=False)
print(f"  Jawaban: x = Rp {x:,.0f}")

print("\n  Soal: Jumlah dua bilangan adalah 48.")
print("  Bilangan pertama 4 lebih besar dari 2x bilangan kedua.")
print("  Model: x + y = 48, x = 2y + 4")
try:
    import sympy as sp
    x,y = sp.symbols("x y")
    sol = sp.solve([x+y-48, x-2*y-4], [x,y])
    print(f"  Jawaban: x = {sol[x]}, y = {sol[y]}")
except ImportError:
    # Manual
    # x + y = 48, x = 2y+4 -> 2y+4+y=48 -> 3y=44 -> y=44/3
    y_val = 44/3
    x_val = 2*y_val + 4
    print(f"  Jawaban: x = {x_val:.2f}, y = {y_val:.2f}")

# ─── 5. Proporsi ─────────────────────────────────────────────
print("\n[5] Proporsi dan Cross Multiplication")
print("  a/b = c/d  ->  ad = bc  (cross multiply)")

def solve_proportion(a, b, c):
    """Selesaikan a/b = c/x -> x = bc/a"""
    x = b * c / a
    print(f"  {a}/{b} = {c}/x  ->  x = {x:.4f}")
    return x

print("  Jika 3/4 = 9/x, cari x:")
solve_proportion(3, 4, 9)
print("  Jika resep untuk 4 orang butuh 2.5 cup tepung, untuk 10 orang?")
solve_proportion(4, 2.5, 10)

print("\n[Selesai] Lanjut ke exercises.py")
