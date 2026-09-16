"""
Challenge: Absolute Value  |  Phase 1 — Topic 1.15
"""
import math
print("CHALLENGE 1.15 — NILAI MUTLAK")

# ─── Ch1: Norma L1, L2, L-inf ────────────────────────────────
print("\n[Ch1] Berbagai Norma (Generalisasi Nilai Mutlak)")

def lp_norm(v, p):
    """Hitung Lp norm dari vektor v."""
    if p == float("inf"):
        return max(abs(x) for x in v)
    return sum(abs(x)**p for x in v)**(1/p)

vectors = [[3,4], [1,-1,1,-1], [5,0,0], [1,1,1,1]]
for v in vectors:
    l1 = lp_norm(v, 1)
    l2 = lp_norm(v, 2)
    linf = lp_norm(v, float("inf"))
    print(f"  v={v}")
    print(f"    L1={l1:.4f},  L2={l2:.4f},  L∞={linf:.4f}")
    print(f"    L∞ ≤ L2 ≤ L1? {linf<=l2+1e-10 and l2<=l1+1e-10}")

# ─── Ch2: Taxicab / Manhattan Distance ───────────────────────
print("\n[Ch2] Jarak Taksi (Taxicab / Manhattan Geometry)")
print("  d_taxi(P,Q) = |x1-x2| + |y1-y2|")
print("  Ini adalah L1 norm dari selisih koordinat")

def taxi_dist(P, Q):
    return sum(abs(P[i]-Q[i]) for i in range(len(P)))

def eucl_dist(P, Q):
    return math.sqrt(sum((P[i]-Q[i])**2 for i in range(len(P))))

points = [((0,0),(3,4)), ((1,2),(4,6)), ((0,0),(1,1))]
print(f"  {'P':>10} {'Q':>10} | {'Taxi':>8} | {'Euclidean':>10} | {'Taxi≥Eucl?':>10}")
for P,Q in points:
    t = taxi_dist(P,Q); e = eucl_dist(P,Q)
    print(f"  {str(P):>10} {str(Q):>10} | {t:>8.4f} | {e:>10.4f} | {t>=e-1e-10}")

# ─── Ch3: L1 Minimization (Median is L1-optimal) ─────────────
print("\n[Ch3] L1 Minimization — Mengapa Median Meminimalkan Σ|x-m|?")

data = [1, 3, 7, 8, 10, 15, 20]
median_val = sorted(data)[len(data)//2]  # karena ganjil
mean_val = sum(data)/len(data)

def l1_cost(data, m):
    return sum(abs(x-m) for x in data)

def l2_cost(data, m):
    return sum((x-m)**2 for x in data)

print(f"  Data: {data}")
print(f"  Mean = {mean_val:.4f},  Median = {median_val}")
print(f"  L1(mean)   = Σ|x-mean|   = {l1_cost(data, mean_val):.4f}")
print(f"  L1(median) = Σ|x-median| = {l1_cost(data, median_val):.4f}")
print(f"  L2(mean)   = Σ(x-mean)²  = {l2_cost(data, mean_val):.4f}")
print(f"  L2(median) = Σ(x-median)² = {l2_cost(data, median_val):.4f}")
print(f"  → Median minimal L1, Mean minimal L2!")

# Grid search untuk konfirmasi
best_m, best_cost = None, float("inf")
for m_test in [x/10 for x in range(-100, 300)]:
    cost = l1_cost(data, m_test)
    if cost < best_cost:
        best_cost = cost
        best_m = m_test
print(f"  Grid search: minimum L1 di m={best_m} (cost={best_cost:.4f})")
print(f"  Konfirmasi: best_m ≈ median = {median_val}? {abs(best_m-median_val)<0.5}")

print("\n[Selesai Challenge 1.15]")
