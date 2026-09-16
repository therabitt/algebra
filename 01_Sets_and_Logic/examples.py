"""
Module  : Sets and Logic (Himpunan dan Logika)
Phase   : 1 - Algebra  |  Topic: 1.14
Jalankan: python3 examples.py
"""
print("=" * 60)
print("HIMPUNAN DAN LOGIKA — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# BAGIAN A: HIMPUNAN
# ─────────────────────────────────────────────────────────────
print("\n=== BAGIAN A: HIMPUNAN ===")

# ─── 1. Operasi Himpunan Dasar ─────────────────────────────
print("\n[1] Operasi Himpunan Dasar")

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
U = set(range(1, 11))  # Universal set

print(f"A = {sorted(A)}")
print(f"B = {sorted(B)}")
print(f"U = {sorted(U)}")
print(f"\nA ∪ B = {sorted(A | B)}")
print(f"A ∩ B = {sorted(A & B)}")
print(f"A − B = {sorted(A - B)}")
print(f"B − A = {sorted(B - A)}")
print(f"A △ B = {sorted(A ^ B)}  (symmetric difference)")
print(f"Aᶜ    = {sorted(U - A)}  (komplemen A di U)")

# ─── 2. Subset dan Keanggotaan ────────────────────────────
print("\n[2] Subset dan Keanggotaan")
C = {3, 4}
print(f"C = {C}")
print(f"C ⊆ A? {C.issubset(A)}")
print(f"C ⊂ A (proper)? {C < A}")
print(f"A ⊆ A? {A.issubset(A)}")
print(f"A ⊂ A (proper)? {A < A}  (tidak proper!)")
print(f"3 ∈ A? {3 in A}")
print(f"9 ∈ A? {9 in A}")

# ─── 3. Kardinalitas dan Himpunan Kuasa ───────────────────
print("\n[3] Kardinalitas dan Himpunan Kuasa")

def power_set(s):
    """Hasilkan semua himpunan bagian dari s."""
    s = list(s)
    n = len(s)
    result = []
    for i in range(2**n):   # 2^n subset
        subset = frozenset(s[j] for j in range(n) if i & (1<<j))
        result.append(subset)
    return result

small = {1, 2, 3}
ps = power_set(small)
print(f"A = {small}")
print(f"|A| = {len(small)}")
print(f"|P(A)| = 2^{len(small)} = {2**len(small)}")
print(f"P(A) = {[set(s) for s in sorted(ps, key=len)]}")

# ─── 4. Prinsip Inklusi-Eksklusi ──────────────────────────
print("\n[4] Prinsip Inklusi-Eksklusi")
A_ie = {1,2,3,4,5,6}
B_ie = {4,5,6,7,8}
C_ie = {6,7,8,9,10}

# |A∪B∪C| = |A|+|B|+|C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
lhs = len(A_ie | B_ie | C_ie)
rhs = (len(A_ie) + len(B_ie) + len(C_ie)
       - len(A_ie & B_ie) - len(A_ie & C_ie) - len(B_ie & C_ie)
       + len(A_ie & B_ie & C_ie))
print(f"A={sorted(A_ie)}, B={sorted(B_ie)}, C={sorted(C_ie)}")
print(f"|A∪B∪C| = {len(A_ie | B_ie | C_ie)}  (langsung)")
print(f"|A|+|B|+|C|-|A∩B|-|A∩C|-|B∩C|+|A∩B∩C| = {rhs}")
print(f"Sama? {lhs == rhs}")

# ─── 5. Produk Kartesian ───────────────────────────────────
print("\n[5] Produk Kartesian A × B")
X = {1, 2, 3}
Y = {"a", "b"}
cart = [(x, y) for x in sorted(X) for y in sorted(Y)]
print(f"X = {sorted(X)},  Y = {sorted(Y)}")
print(f"X × Y = {cart}")
print(f"|X × Y| = {len(cart)} = |X|×|Y| = {len(X)}×{len(Y)}")

# ─────────────────────────────────────────────────────────────
# BAGIAN B: LOGIKA PROPOSISIONAL
# ─────────────────────────────────────────────────────────────
print("\n\n=== BAGIAN B: LOGIKA PROPOSISIONAL ===")

# ─── 6. Konektor Logika Dasar ─────────────────────────────
print("\n[6] Tabel Kebenaran Konektor Dasar")

def truth_table(*vars_names):
    """Generator semua kombinasi nilai kebenaran."""
    n = len(vars_names)
    for i in range(2**n):
        yield {vars_names[j]: bool(i & (1 << (n-1-j))) for j in range(n)}

def print_truth_table(vars_names, connectives):
    """Cetak tabel kebenaran."""
    header = "  " + " | ".join(f"{v:>6}" for v in vars_names + list(connectives.keys()))
    print("  " + "-" * (len(header)-2))
    print(header)
    print("  " + "-" * (len(header)-2))
    for vals in truth_table(*vars_names):
        row_vals = list(vals.values())
        computed = [fn(vals) for fn in connectives.values()]
        all_vals = [str(v)[0] for v in row_vals + computed]
        print("  " + " | ".join(f"{'T' if v=='T' else 'F':>6}" for v in all_vals))

# Tabel untuk dua variabel
print("\n  p AND q, p OR q, NOT p, p XOR q, p → q, p ↔ q:")
connectives = {
    "p∧q": lambda v: v["p"] and v["q"],
    "p∨q": lambda v: v["p"] or  v["q"],
    "¬p":  lambda v: not v["p"],
    "p⊕q": lambda v: v["p"] != v["q"],
    "p→q": lambda v: (not v["p"]) or v["q"],
    "p↔q": lambda v: v["p"] == v["q"],
}
print_truth_table(["p","q"], connectives)

# ─── 7. Hukum De Morgan ────────────────────────────────────
print("\n[7] Hukum De Morgan")
print("  ¬(p ∧ q)  =  ¬p ∨ ¬q")
print("  ¬(p ∨ q)  =  ¬p ∧ ¬q")
for vals in truth_table("p","q"):
    p, q = vals["p"], vals["q"]
    lhs1 = not (p and q)
    rhs1 = (not p) or (not q)
    lhs2 = not (p or q)
    rhs2 = (not p) and (not q)
    ok1 = lhs1 == rhs1; ok2 = lhs2 == rhs2
    print(f"  p={str(p)[0]}, q={str(q)[0]}: "
          f"¬(p∧q)={str(lhs1)[0]}=¬p∨¬q={str(rhs1)[0]} ✓{ok1} | "
          f"¬(p∨q)={str(lhs2)[0]}=¬p∧¬q={str(rhs2)[0]} ✓{ok2}")

# ─── 8. Tautologi dan Kontradiksi ─────────────────────────
print("\n[8] Tautologi dan Kontradiksi")
print("  Tautologi: p ∨ ¬p  (selalu True)")
print("  Kontradiksi: p ∧ ¬p  (selalu False)")
for vals in truth_table("p"):
    p = vals["p"]
    taut = p or (not p)
    contra = p and (not p)
    print(f"  p={str(p)[0]}: p∨¬p={str(taut)[0]}, p∧¬p={str(contra)[0]}")

# ─── 9. Kontrapositif dan Konvers ─────────────────────────
print("\n[9] Implikasi: p→q,  Konvers: q→p,  Kontrapositif: ¬q→¬p")
print("  Kontrapositif selalu setara dengan implikasi asal!")
print(f"  {'p':>3} {'q':>3} | {'p→q':>5} | {'q→p':>5} | {'¬q→¬p':>7}")
print("  " + "-"*40)
for vals in truth_table("p","q"):
    p, q = vals["p"], vals["q"]
    impl = (not p) or q
    conv = (not q) or p
    contra = (not q) or (not (not p))  # ¬q → ¬p = q ∨ ¬p... same as conv actually:
    # Actually: ¬q→¬p = (not(not q)) or (not p) = q or (not p) — same as conv
    # No wait: contrapositive of p->q is ¬q->¬p which equals (not(not q)) or (not p) = q or (not p)
    # which is the SAME as p->q.
    contra_correct = (not (not q)) or (not p)  # = q or not(p) = same as p->q
    contra_correct = q or (not p)
    print(f"  {str(p)[0]:>3} {str(q)[0]:>3} | {str(impl)[0]:>5} | {str(conv)[0]:>5} | {str(contra_correct)[0]:>7}")

# ─── 10. Kuantifikasi ─────────────────────────────────────
print("\n[10] Kuantifikasi — ∀ dan ∃")
numbers = list(range(1, 11))
print(f"  Domain: {numbers}")

predicate_even = lambda x: x % 2 == 0
predicate_pos  = lambda x: x > 0
predicate_gt10 = lambda x: x > 10

print(f"  ∀x: x>0?  {all(predicate_pos(x) for x in numbers)}  (semua positif)")
print(f"  ∃x: x>5?  {any(x>5 for x in numbers)}  (ada yang > 5)")
print(f"  ∀x: x>10? {all(predicate_gt10(x) for x in numbers)}  (semua > 10?)")
print(f"  ∃x: x>10? {any(predicate_gt10(x) for x in numbers)}  (ada yang > 10?)")

# Negasi kuantifier
print("\n  Negasi: ¬(∀x P(x)) = ∃x ¬P(x)")
P = predicate_gt10
neg_forall = any(not P(x) for x in numbers)
exists_neg  = any(not P(x) for x in numbers)
print(f"  ¬(∀x: x>10) = ∃x: x≤10 = {neg_forall} = {exists_neg}")

print("\n[Selesai] Lanjut ke exercises.py")
