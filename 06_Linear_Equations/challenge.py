"""
Challenge: Linear Equations  |  Phase 1 — Topic 1.4
"""
print("CHALLENGE 1.4 — PERSAMAAN LINEAR")

# Challenge: Step-by-step solver dengan output rinci
def solve_with_steps(equation_str, var="x"):
    """Solver persamaan linear dengan langkah-langkah ditampilkan."""
    try:
        import sympy as sp
        x = sp.Symbol(var)
        # Parse kedua sisi
        sides = equation_str.split("=")
        lhs = sp.sympify(sides[0].strip())
        rhs = sp.sympify(sides[1].strip())
        eq = sp.Eq(lhs, rhs)
        
        print(f"\n  Persamaan: {equation_str}")
        print(f"  LHS = {lhs}")
        print(f"  RHS = {rhs}")
        print(f"  LHS - RHS = {sp.expand(lhs - rhs)}")
        
        sol = sp.solve(eq, x)
        if not sol:
            print("  Tidak ada solusi atau tak hingga solusi")
        else:
            print(f"  Solusi: {var} = {sol[0]}")
            # Verifikasi
            for s in sol:
                check = lhs.subs(x, s) - rhs.subs(x, s)
                print(f"  Verifikasi: substitusi {var}={s} -> error = {check}")
    except Exception as e:
        print(f"  Error: {e}")

equations = [
    "3*x + 7 = 22",
    "2*(x - 3) + 5 = x + 8",
    "x/3 + x/4 = 7",
    "0.5*x - 1.5 = 2.5",
]
for eq in equations:
    solve_with_steps(eq)

# Mixture problem solver
print("\n[Ch2] Mixture Problem Solver")
def mixture(c1, v1, c2, v2, c_target):
    """
    Berapa banyak larutan 1 (konsentrasi c1) dan larutan 2 (c2)
    yang dicampur untuk mendapatkan c_target?
    c1*v1 + c2*x = c_target*(v1+x)
    """
    # c1*v1 + c2*x = c_target*v1 + c_target*x
    # x(c2 - c_target) = c_target*v1 - c1*v1
    # x = v1*(c_target - c1) / (c2 - c_target)
    if abs(c2 - c_target) < 1e-10:
        return "Tidak bisa — konsentrasi sama"
    x = v1 * (c_target - c1) / (c2 - c_target)
    return x

x = mixture(0.20, 100, 0.50, None, 0.30)
print(f"  Larutan 20% sebanyak 100ml + Larutan 50% sebanyak {x:.1f}ml")
print(f"  = Larutan 30% sebanyak {100+x:.1f}ml")
print("\n[Selesai Challenge 1.4]")
