"""
Challenge: Linear Inequalities  |  Phase 1 — Topic 1.5
"""
print("CHALLENGE 1.5 — PERTIDAKSAMAAN LINEAR")

# Challenge 1: Linear Programming (intro)
print("\n[Ch1] Linear Programming Sederhana")
print("  Maksimalkan: P = 3x + 5y")
print("  Subject to: x+y<=4, x>=0, y>=0")
print("  Titik-titik ekstrem (corner points):")

corners = [(0,0), (4,0), (0,4)]
print(f"  {'Titik':>10} | {'P=3x+5y':>10}")
best = None
for (x,y) in corners:
    P = 3*x + 5*y
    print(f"  ({x},{y}):        {P:>10}")
    if best is None or P > best[1]:
        best = ((x,y), P)
print(f"  Maksimum P = {best[1]} di titik {best[0]}")

# Challenge 2: Interval Intersection
print("\n[Ch2] Operasi Interval")

class Interval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        self.a, self.b = a, b
        self.lc, self.rc = left_closed, right_closed

    def __contains__(self, x):
        l = (x >= self.a) if self.lc else (x > self.a)
        r = (x <= self.b) if self.rc else (x < self.b)
        return l and r

    def intersect(self, other):
        new_a = max(self.a, other.a)
        new_b = min(self.b, other.b)
        if new_a > new_b: return None
        lc = self.lc if self.a > other.a else (other.lc if other.a > self.a else (self.lc and other.lc))
        rc = self.rc if self.b < other.b else (other.rc if other.b < self.b else (self.rc and other.rc))
        return Interval(new_a, new_b, lc, rc)

    def __repr__(self):
        l = "[" if self.lc else "("
        r = "]" if self.rc else ")"
        return f"{l}{self.a}, {self.b}{r}"

I1 = Interval(-2, 5)
I2 = Interval(1, 8)
inter = I1.intersect(I2)
print(f"  I1 = {I1},  I2 = {I2}")
print(f"  I1 ∩ I2 = {inter}")
print(f"  x=3 ∈ I1∩I2? {3 in inter}")
print(f"  x=6 ∈ I1∩I2? {6 in inter}")

print("\n[Selesai Challenge 1.5]")
