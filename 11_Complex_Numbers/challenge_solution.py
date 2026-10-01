"""
Challenge: Complex Numbers  |  Phase 1 — Topic 1.18
"""
import math, cmath
print("CHALLENGE 1.18 — BILANGAN KOMPLEKS")

# Challenge 1: Implement Complex class from scratch
print("\n[Ch1] Kelas Bilangan Kompleks dari Nol")

class MyComplex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real+other.real, self.imag+other.imag)

    def __mul__(self, other):
        # (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        r = self.real*other.real - self.imag*other.imag
        i = self.real*other.imag + self.imag*other.real
        return MyComplex(r, i)

    def __truediv__(self, other):
        # z1/z2 = z1·z̄2 / |z2|²
        denom = other.real**2 + other.imag**2
        r = (self.real*other.real + self.imag*other.imag) / denom
        i = (self.imag*other.real - self.real*other.imag) / denom
        return MyComplex(r, i)

    def conjugate(self): return MyComplex(self.real, -self.imag)
    def modulus(self):   return math.sqrt(self.real**2 + self.imag**2)
    def argument(self):  return math.atan2(self.imag, self.real)

    def power(self, n):
        """Pangkat menggunakan De Moivre."""
        r = self.modulus()**n
        theta = self.argument() * n
        return MyComplex(r*math.cos(theta), r*math.sin(theta))

    def nth_roots(self, n):
        """Temukan n akar ke-n."""
        r = self.modulus()**(1/n)
        theta = self.argument()
        return [MyComplex(r*math.cos((theta+2*math.pi*k)/n),
                          r*math.sin((theta+2*math.pi*k)/n))
                for k in range(n)]

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real:.4f} {sign} {abs(self.imag):.4f}i)"

z1 = MyComplex(3, 4)
z2 = MyComplex(1, -2)
print(f"  z1 = {z1},  |z1| = {z1.modulus():.4f}")
print(f"  z2 = {z2}")
print(f"  z1+z2 = {z1+z2}")
print(f"  z1*z2 = {z1*z2}")
print(f"  z1/z2 = {z1/z2}")
print(f"  z1^3 = {z1.power(3)}")
print(f"  Cube roots of z1: {z1.nth_roots(3)}")

# Challenge 2: Fourier Series Preview
print("\n[Ch2] Preview Fourier Series dengan Bilangan Kompleks")
print("  f(t) = Σ cₙ·e^(2πint/T)")
print("  Kita hitung beberapa koefisien untuk gelombang kotak")

import math
def square_wave_fourier(t, T=1.0, n_terms=5):
    """
    Aproksimasi gelombang kotak dengan deret Fourier.
    f(t) = (4/π) Σ sin(2π(2k-1)t/T) / (2k-1)  untuk k=1,2,...
    """
    result = 0
    for k in range(1, n_terms+1):
        n = 2*k - 1  # hanya harmonik ganjil
        result += math.sin(2*math.pi*n*t/T) / n
    return 4/math.pi * result

print("\n  Gelombang kotak T=1, 10 suku Fourier:")
print(f"  {'t':>6} | {'Fourier':>10} | {'Ideal':>8}")
for t in [0, 0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1.0]:
    ideal = 1 if (t % 1.0) < 0.5 else -1
    if t % 0.5 == 0: ideal = 0
    approx = square_wave_fourier(t, n_terms=10)
    print(f"  {t:>6.2f} | {approx:>10.6f} | {ideal:>8}")

print("\n[Selesai Challenge 1.18]")
