# 1.16 Pecahan Aljabar — Teori Lengkap

## 1. Definisi
Ekspresi rasional: R(x) = P(x)/Q(x) di mana P, Q adalah polinomial dan Q ≠ 0.

## 2. Domain
Domain = semua x ∈ R kecuali akar-akar dari Q(x).
Contoh: (x+1)/(x²-4) → penyebut = (x+2)(x-2) → domain: x ≠ ±2

## 3. Ekspresi Rasional Paling Sederhana
R(x) paling sederhana jika gcd(P(x), Q(x)) = 1.
Cara: faktorkan P dan Q, bagi faktor sekutu.

## 4. Operasi

### Perkalian
(P₁/Q₁) × (P₂/Q₂) = (P₁P₂)/(Q₁Q₂)
Sederhanakan sebelum mengalikan jika memungkinkan!

### Pembagian
(P₁/Q₁) ÷ (P₂/Q₂) = (P₁/Q₁) × (Q₂/P₂) = (P₁Q₂)/(Q₁P₂)

### Penjumlahan / Pengurangan
KPK (LCD) penyebut dulu, lalu:
(P₁/Q₁) + (P₂/Q₂) = (P₁·(LCD/Q₁) + P₂·(LCD/Q₂)) / LCD

## 5. Persamaan Rasional
P(x)/Q(x) = R(x)/S(x)

Langkah:
1. Kalikan kedua sisi dengan LCD
2. Selesaikan persamaan polinomial hasil
3. **Periksa solusi extraneous** (yang membuat penyebut = 0!)

## 6. Ekspresi Kompleks (Complex Fractions)
Pecahan di dalam pecahan: sederhanakan dari dalam keluar.

## 7. Dekomposisi Parsial
P(x)/Q(x) di mana deg P < deg Q, Q terdekomposisi:

| Faktor Q(x) | Bentuk parsial |
|-------------|----------------|
| (x-a)       | A/(x-a) |
| (x-a)ⁿ     | A₁/(x-a) + ... + Aₙ/(x-a)ⁿ |
| (x²+bx+c) irreduksi | (Ax+B)/(x²+bx+c) |

Kegunaan: integrasi dalam kalkulus!

## 8. Asymptotes Fungsi Rasional f(x) = P(x)/Q(x)
- **Vertikal asymptote:** x = a jika Q(a)=0 dan P(a)≠0
- **Horizontal asymptote:**
  - deg P < deg Q: y = 0
  - deg P = deg Q: y = leading_P/leading_Q
  - deg P > deg Q: tidak ada (oblique asymptote)
- **Oblique asymptote:** jika deg P = deg Q + 1, bagi P dengan Q
