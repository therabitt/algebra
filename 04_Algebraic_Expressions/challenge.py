"""
Challenge: Algebraic Expressions  |  Phase 1 — Topic 1.3
"""
print("CHALLENGE 1.3 — EKSPRESI ALJABAR")
print("=" * 50)

# Challenge 1: Polynomial Arithmetic dari nol
print("\n[Ch1] Kelas Polynomial dari nol")

class Poly:
    """Polinomial direpresentasikan sebagai list koefisien.
       coeffs[i] = koefisien x^i
       Contoh: 3x^2 + 5x - 1 = Poly([-1, 5, 3])
    """
    def __init__(self, coeffs):
        self.c = list(coeffs)
        while len(self.c) > 1 and self.c[-1] == 0:
            self.c.pop()

    def degree(self): return len(self.c) - 1

    def __call__(self, x):
        # Horner's method: lebih efisien
        result = 0
        for coef in reversed(self.c):
            result = result * x + coef
        return result

    def __add__(self, other):
        n = max(len(self.c), len(other.c))
        c1 = self.c + [0]*(n-len(self.c))
        c2 = other.c + [0]*(n-len(other.c))
        return Poly([a+b for a,b in zip(c1,c2)])

    def __mul__(self, other):
        result = [0] * (len(self.c)+len(other.c)-1)
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):
                result[i+j] += a*b
        return Poly(result)

    def __repr__(self):
        terms = []
        for i,c in enumerate(reversed(self.c)):
            d = self.degree()-i
            if c==0: continue
            if d==0: terms.append(str(c))
            elif d==1: terms.append(f"{c}x")
            else: terms.append(f"{c}x^{d}")
        return " + ".join(terms).replace("+ -","- ") or "0"

p1 = Poly([-5, 3, 2])   # 2x^2 + 3x - 5
p2 = Poly([2, 1])        # x + 2
print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1+p2 = {p1+p2}")
print(f"p1*p2 = {p1*p2}")
print(f"p1(3) = {p1(3)}  (expected: {2*9+3*3-5})")

# Challenge 2: Parser ekspresi sederhana
print("\n[Ch2] Evaluator ekspresi string sederhana (safe eval)")
import ast, operator, math

SAFE_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.USub: operator.neg,
}

def safe_eval(expr_str, variables=None):
    """Evaluasi ekspresi matematika string dengan aman."""
    variables = variables or {}
    tree = ast.parse(expr_str, mode="eval")
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            if node.id in variables: return variables[node.id]
            raise ValueError(f"Variabel tidak dikenal: {node.id}")
        elif isinstance(node, ast.BinOp):
            op = SAFE_OPS.get(type(node.op))
            if op is None: raise ValueError("Operator tidak aman")
            return op(_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            op = SAFE_OPS.get(type(node.op))
            return op(_eval(node.operand))
        raise ValueError(f"Node tidak didukung: {type(node)}")
    return _eval(tree)

exprs = ["3*x**2 - 5*x + 2", "2*x + 3*y", "(x+3)**2"]
for expr in exprs:
    try:
        val = safe_eval(expr, {"x": 2, "y": 4})
        print(f"  {expr} at x=2,y=4 = {val}")
    except Exception as e:
        print(f"  Error: {e}")

print("\n[Selesai Challenge 1.3]")
