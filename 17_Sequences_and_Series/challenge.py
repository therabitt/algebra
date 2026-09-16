"""
Challenge: Sequences and Series  |  Phase 1 — Topic 1.12
"""
import math
print("CHALLENGE 1.12 — BARISAN DAN DERET")

# Challenge 1: Matrix Fibonacci O(log n)
print("\n[Ch1] Fibonacci O(log n) dengan Matrix Exponentiation")
def mat_mul(A, B):
    """2x2 matrix multiplication."""
    return [
        [A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
        [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]],
    ]

def mat_pow(M, n):
    """Matrix power dengan fast exponentiation."""
    if n == 1: return M
    if n % 2 == 0:
        half = mat_pow(M, n//2)
        return mat_mul(half, half)
    return mat_mul(M, mat_pow(M, n-1))

def fib_matrix(n):
    if n == 0: return 0
    M = [[1,1],[1,0]]
    result = mat_pow(M, n)
    return result[0][1]

def fib_iter(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

for n in [10, 50, 100, 1000]:
    m_result = fib_matrix(n)
    i_result = fib_iter(n)
    print(f"  F({n}): matrix={m_result}, iteratif={i_result}, sama={m_result==i_result}")

# Challenge 2: Zeno's Paradox (infinite geometric series)
print("\n[Ch2] Paradoks Zeno — Deret Geometrika Tak Hingga")
print("  Achilles lari 100m, kura-kura start 10m di depan, kura-kura setengah kecepatan")
print("  Setiap interval: Achilles tutup jarak, kura-kura maju setengahnya...")
steps = []
gap = 10.0; total_time = 0.0; v = 10  # Achilles: 10m/s, kura: 5m/s
for i in range(10):
    t = gap / (v - v/2)  # waktu menutup gap
    total_time += t
    steps.append((i+1, gap, total_time))
    gap /= 2
print(f"  {'Step':>5} | {'Gap':>10} | {'Total Time':>12}")
for step, gap_val, t_val in steps:
    print(f"  {step:>5} | {gap_val:>10.6f} | {t_val:>12.6f}")
print(f"  Jumlah tak hingga waktu = {10/(10-5)*10:.4f} detik (konvergen!)")

# Challenge 3: Series convergence tests
print("\n[Ch3] Uji Konvergensi Deret")
print("  Harmonic series: Σ1/n -> DIVERGE")
s = 0
for n in range(1, 1001):
    s += 1/n
print(f"  Σ1/n (n=1..1000) = {s:.6f}  (terus bertambah -> divergen)")

print("  Basel problem: Σ1/n² -> π²/6")
s2 = sum(1/n**2 for n in range(1, 10001))
print(f"  Σ1/n² (n=1..10000) = {s2:.8f}")
print(f"  π²/6  = {math.pi**2/6:.8f}")
print(f"  Error = {abs(s2 - math.pi**2/6):.2e}")

print("\n[Selesai Challenge 1.12]")
