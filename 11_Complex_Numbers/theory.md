# 1.18 Bilangan Kompleks — Teori Lengkap

## 1. Definisi
i didefinisikan sebagai: i² = -1
Bilangan kompleks: z = a + bi, di mana a, b ∈ ℝ
- a = Re(z) = bagian real
- b = Im(z) = bagian imajiner

## 2. Representasi Geometri
Setiap z = a + bi sesuai dengan titik (a, b) pada bidang kompleks (Argand plane).

## 3. Operasi Aljabar
z₁ = a+bi,  z₂ = c+di

| Operasi | Rumus |
|---------|-------|
| Penjumlahan | (a+c) + (b+d)i |
| Pengurangan | (a-c) + (b-d)i |
| Perkalian | (ac-bd) + (ad+bc)i |
| Pembagian | z₁/z₂ = z₁·z̄₂/|z₂|² |

## 4. Konjugat
z̄ = a - bi
Sifat: z·z̄ = a² + b² = |z|² (selalu bilangan real!)

## 5. Modulus (Nilai Mutlak)
|z| = √(a² + b²)
Sifat: |z₁z₂| = |z₁||z₂|,  |z₁/z₂| = |z₁|/|z₂|

## 6. Argument
arg(z) = θ = arctan(b/a)  (perhatikan kuadran!)
Gunakan atan2(b, a) untuk presisi.

## 7. Bentuk Polar (Euler)
z = r·e^(iθ) = r(cos θ + i sin θ)
di mana r = |z|, θ = arg(z)

Pembuktian Euler: e^(iθ) = cos θ + i sin θ (deret Taylor)

Rumus Euler yang indah: e^(iπ) + 1 = 0  ← paling indah dalam matematika!

## 8. Perkalian dalam Bentuk Polar
z₁·z₂ = r₁r₂ · e^(i(θ₁+θ₂))
→ Moduli dikalikan, argument dijumlahkan

## 9. Teorema De Moivre
(cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)
Berguna untuk menghitung sin(nθ) dan cos(nθ) secara eksplisit.

## 10. Akar-n dari Bilangan Kompleks
Persamaan z^n = w memiliki tepat n solusi:
zₖ = r^(1/n) · e^(i(θ + 2πk)/n),  k = 0, 1, ..., n-1

Akar-n dari unity: zₖ = e^(2πik/n)  →  membentuk segi-n beraturan!

## 11. Teorema Fundamental Aljabar
Setiap polinomial derajat n dengan koefisien kompleks memiliki
tepat n akar (dihitung dengan multiplisitas) di ℂ.

## 12. Bilangan Kompleks dalam Python
Python punya tipe built-in `complex`:
- z = 3 + 4j  (gunakan j, bukan i!)
- z.real → 3.0
- z.imag → 4.0
- z.conjugate() → 3-4j
- abs(z) → 5.0
