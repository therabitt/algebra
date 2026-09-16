"""
Challenge: Functions and Relations  |  Phase 1 — Topic 1.8
"""
import math
print("CHALLENGE 1.8 — FUNGSI DAN RELASI")

# Challenge 1: Function class
print("\n[Ch1] Kelas Function dengan komposisi dan invers")

class Function:
    def __init__(self, fn, name="f"):
        self.fn = fn
        self.name = name
    def __call__(self, x):
        return self.fn(x)
    def compose(self, other):
        return Function(lambda x: self.fn(other.fn(x)), f"{self.name}∘{other.name}")
    def inverse_approx(self, y, a=-100, b=100, tol=1e-8):
        """Bisection untuk numerik invers: cari x sehingga f(x)=y"""
        for _ in range(200):
            mid = (a+b)/2
            if abs(b-a) < tol: return mid
            if (self(mid)-y)*(self(a)-y) < 0: b=mid
            else: a=mid
        return (a+b)/2

f = Function(lambda x: 2*x+3, "f")
g = Function(lambda x: x**2-1, "g")
fog = f.compose(g)
gof = g.compose(f)

print(f"  f(4) = {f(4)}, g(4) = {g(4)}")
print(f"  (f∘g)(4) = {fog(4)}, (g∘f)(4) = {gof(4)}")
y = f(7)
x_inv = f.inverse_approx(y)
print(f"  f(7)={y}, f^-1({y}) ≈ {x_inv:.6f}")

# Challenge 2: Fixed Point Iteration
print("\n[Ch2] Fixed Point Iteration: x = g(x)")
def fixed_point(g, x0, tol=1e-8, max_iter=200):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, max_iter

# cos(x) = x (Banach fixed point)
result, iters = fixed_point(math.cos, 1.0)
print(f"  cos(x)=x -> x ≈ {result:.10f} (setelah {iters} iterasi)")
print(f"  Verifikasi: cos({result:.6f}) = {math.cos(result):.10f}")

# sqrt(x) -> fixed point of g(x)=(x+2/x)/2 starting at x=2 (sqrt(2))
result2, iters2 = fixed_point(lambda x: (x + 2/x)/2, 1.0)
print(f"  Newton sqrt(2) -> x ≈ {result2:.10f} (iters={iters2})")
print(f"  Actual √2 = {math.sqrt(2):.10f}")

print("\n[Selesai Challenge 1.8]")
