"""
Exercises: Sets and Logic  |  Phase 1 — Topic 1.14
"""
print("LATIHAN 1.14 — HIMPUNAN DAN LOGIKA")
print("=" * 50)

A = {1,2,3,4,5}; B = {3,4,5,6,7}; C = {5,6,7,8}; U = set(range(1,11))

# Ex 1: Set operations
print("\n[Ex 1] Hitung operasi himpunan A={1..5}, B={3..7}:")
ops = [("A∪B", A|B), ("A∩B", A&B), ("A-B", A-B), ("B-A", B-A),
       ("A△B", A^B), ("Aᶜ", U-A)]
for name, val in ops:
    print(f"  {name} = {sorted(val)}")

# Ex 2: Venn problems
print("\n[Ex 2] Dari 40 siswa: 25 suka Matematika (M), 18 suka Fisika (F)")
print("  10 suka keduanya. Berapa yang suka keduanya? Hanya M? Hanya F? Tidak keduanya?")
M_total, F_total, both = 25, 18, 10
only_M = M_total - both
only_F = F_total - both
neither = 40 - (only_M + only_F + both)
print(f"  |M∪F| = {M_total}+{F_total}-{both} = {M_total+F_total-both}")
print(f"  Hanya M: {only_M}, Hanya F: {only_F}, Keduanya: {both}, Tidak keduanya: {neither}")

# Ex 3: Power set
print("\n[Ex 3] Himpunan kuasa dari S = {a, b, c}")
def power_set(s):
    s=list(s); n=len(s)
    return [set(s[j] for j in range(n) if i&(1<<j)) for i in range(2**n)]
S = {"a","b","c"}
ps = power_set(S)
print(f"  |P(S)| = 2^3 = {len(ps)}")
print(f"  P(S) = {[sorted(x) for x in sorted(ps, key=lambda x: (len(x), sorted(x)))]}")

# Ex 4: Truth tables
print("\n[Ex 4] Tentukan nilai kebenaran:")
cases = [
    ("p=T, q=F: p→q",  lambda p,q: (not p) or q,  True, False),
    ("p=F, q=T: p↔q",  lambda p,q: p==q,           False, True),
    ("p=T: ¬(p∧¬p)",   lambda p,q: not(p and not p), True, True),
    ("p=T,q=T: ¬p∨¬q", lambda p,q: (not p) or (not q), True, True),
]
for label, fn, p, q in cases:
    result = fn(p,q)
    print(f"  {label} = {result}")

# Ex 5: De Morgan
print("\n[Ex 5] Verifikasi Hukum De Morgan dengan contoh konkret")
A5 = {1,2,3,4}; B5 = {3,4,5,6}; U5 = set(range(1,8))
lhs1 = U5 - (A5 | B5)
rhs1 = (U5-A5) & (U5-B5)
lhs2 = U5 - (A5 & B5)
rhs2 = (U5-A5) | (U5-B5)
print(f"  (A∪B)ᶜ = {sorted(lhs1)},  Aᶜ∩Bᶜ = {sorted(rhs1)},  sama? {lhs1==rhs1}")
print(f"  (A∩B)ᶜ = {sorted(lhs2)},  Aᶜ∪Bᶜ = {sorted(rhs2)},  sama? {lhs2==rhs2}")

# Ex 6: Proof by induction
print("\n[Ex 6] Induksi Matematika: buktikan Σk = n(n+1)/2")
def verify_sum_formula(n):
    direct = sum(range(1, n+1))
    formula = n*(n+1)//2
    return direct, formula, direct==formula

print("  n  | Σk (langsung) | n(n+1)/2 | Sama?")
for n in range(1, 11):
    d, f, ok = verify_sum_formula(n)
    print(f"  {n:>2} | {d:>13} | {f:>8} | {ok}")

print("\n[Selesai]")
