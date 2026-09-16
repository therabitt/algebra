"""
Challenge: Sets and Logic  |  Phase 1 — Topic 1.14
"""
print("CHALLENGE 1.14 — HIMPUNAN DAN LOGIKA")

# ─── Ch1: Propositional Logic Evaluator ───────────────────────
print("\n[Ch1] Evaluator Logika Proposisional")

class Prop:
    """Kelas proposisi yang bisa dikombinasikan."""
    def __init__(self, name, value=None):
        self.name = name
        self._value = value

    def eval(self, env=None):
        if self._value is not None: return self._value
        return env.get(self.name, False)

    def __and__(self, other):
        result = Prop(f"({self.name}∧{other.name})")
        orig_eval = lambda env: self.eval(env) and other.eval(env)
        result.eval = orig_eval
        return result

    def __or__(self, other):
        result = Prop(f"({self.name}∨{other.name})")
        orig_eval = lambda env: self.eval(env) or other.eval(env)
        result.eval = orig_eval
        return result

    def __invert__(self):
        result = Prop(f"¬{self.name}")
        orig_eval = lambda env: not self.eval(env)
        result.eval = orig_eval
        return result

    def implies(self, other):
        result = Prop(f"({self.name}→{other.name})")
        orig_eval = lambda env: (not self.eval(env)) or other.eval(env)
        result.eval = orig_eval
        return result

    def __repr__(self): return self.name

# Test
p = Prop("p")
q = Prop("q")
impl = p.implies(q)
contra = (~q).implies(~p)

print("  p→q (implikasi) vs ¬q→¬p (kontrapositif):")
print(f"  {'p':>3} {'q':>3} | {'p→q':>5} | {'¬q→¬p':>7} | {'Sama?':>6}")
for pv in [True, False]:
    for qv in [True, False]:
        env = {"p": pv, "q": qv}
        i_val = impl.eval(env)
        c_val = contra.eval(env)
        print(f"  {str(pv)[0]:>3} {str(qv)[0]:>3} | {str(i_val)[0]:>5} | {str(c_val)[0]:>7} | {str(i_val==c_val)[0]:>6}")

# ─── Ch2: SAT Solver (brute force) ────────────────────────────
print("\n[Ch2] SAT Solver — Apakah formula dapat dipenuhi?")

def sat_solve(formula_fn, variables):
    """
    Brute-force SAT solver: coba semua kombinasi nilai kebenaran.
    formula_fn: fungsi yang menerima dict {var: bool} dan return bool
    variables: list nama variabel
    """
    n = len(variables)
    solutions = []
    for i in range(2**n):
        env = {variables[j]: bool(i & (1<<j)) for j in range(n)}
        if formula_fn(env):
            solutions.append(dict(env))
    return solutions

# Formula: (p ∨ q) ∧ (¬p ∨ r) ∧ (¬q ∨ ¬r)
def formula(env):
    p,q,r = env["p"], env["q"], env["r"]
    return (p or q) and ((not p) or r) and ((not q) or (not r))

solutions = sat_solve(formula, ["p","q","r"])
print(f"  Formula: (p∨q) ∧ (¬p∨r) ∧ (¬q∨¬r)")
print(f"  SAT: {len(solutions) > 0}  ({len(solutions)} solusi)")
for sol in solutions:
    print(f"    {sol}")

# Contradiction: p ∧ ¬p
def contra_formula(env):
    p = env["p"]
    return p and (not p)

solutions2 = sat_solve(contra_formula, ["p"])
print(f"\n  Formula: p ∧ ¬p")
print(f"  SAT: {len(solutions2) > 0}  ({'kontradiksi!' if not solutions2 else 'satisfiable'})")

# Tautology: p ∨ ¬p
def taut_formula(env):
    p = env["p"]
    return p or (not p)

solutions3 = sat_solve(taut_formula, ["p"])
print(f"\n  Formula: p ∨ ¬p")
print(f"  Semua 2^1={2} kombinasi penuhi? {len(solutions3)==2}  ({'tautologi!' if len(solutions3)==2 else 'bukan'})")

# ─── Ch3: Cantor's Diagonal Argument (demo) ───────────────────
print("\n[Ch3] Argumen Diagonal Cantor")
print("  Buktikan bahwa bilangan real (0,1) tidak bisa didaftar!")
print("  Jika ada daftar, kita bisa buat bilangan yang tidak ada di daftar.")

import random
random.seed(42)

# Buat "daftar" bilangan di (0,1) sebagai digit desimal
def random_infinite_decimal(n_digits=20):
    return [random.randint(0, 9) for _ in range(n_digits)]

listing = [random_infinite_decimal() for _ in range(10)]
print("\n  Daftar 10 bilangan (20 digit pertama):")
for i, num in enumerate(listing):
    print(f"  [{i}]: 0.{''.join(map(str,num))}")

# Argumen diagonal: ambil digit ke-i dari bilangan ke-i, ganti dengan digit berbeda
diagonal_digits = [listing[i][i] for i in range(10)]
new_number = [(d+1)%10 for d in diagonal_digits]

print(f"\n  Digit diagonal: {diagonal_digits}")
print(f"  Bilangan baru:  0.{''.join(map(str,new_number))}")
print(f"  Bilangan ini BERBEDA dari setiap bilangan di daftar")
print(f"  -> Tidak ada daftar yang bisa memuat semua bilangan real!")
print(f"  -> |R| > |N| (himpunan bilangan real tidak bisa dihitung)")

print("\n[Selesai Challenge 1.14]")
