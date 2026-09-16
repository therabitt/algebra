# 1.11 Eksponen dan Logaritma — Teori Lengkap

## 1. Definisi Eksponen
a^n = a × a × ... × a (n kali), untuk a ∈ R, n ∈ N

Generalisasi:
- a^0 = 1 (untuk a ≠ 0)
- a^(-n) = 1/a^n
- a^(p/q) = q-th root of a^p = (ᵍ√a)^p

## 2. Tujuh Hukum Eksponen
| Hukum | Rumus | Contoh |
|-------|-------|--------|
| Perkalian basis sama | a^m · a^n = a^(m+n) | 2³·2⁴ = 2⁷ |
| Pembagian basis sama | a^m / a^n = a^(m-n) | 5⁶/5² = 5⁴ |
| Pangkat dari pangkat | (a^m)^n = a^(mn) | (3²)³ = 3⁶ |
| Pangkat perkalian | (ab)^n = a^n·b^n | (2·3)⁴ = 2⁴·3⁴ |
| Pangkat pembagian | (a/b)^n = a^n/b^n | (2/5)³ = 8/125 |
| Pangkat nol | a^0 = 1 (a≠0) | 100⁰ = 1 |
| Pangkat negatif | a^(-n) = 1/a^n | 2⁻³ = 1/8 |

## 3. Notasi Ilmiah (Scientific Notation)
a × 10^n di mana 1 ≤ |a| < 10
Contoh: 6.022 × 10²³ (Avogadro), 1.6 × 10⁻¹⁹ (muatan elektron)

## 4. Fungsi Eksponensial f(x) = aˣ
- Domain: semua bilangan real (-∞, ∞)
- Range: (0, ∞) — selalu positif
- Selalu melalui (0, 1) karena a⁰ = 1
- Jika a > 1: fungsi naik (pertumbuhan)
- Jika 0 < a < 1: fungsi turun (peluruhan)
- Horizontal asymptote: y = 0

## 5. Bilangan e
e = lim(n→∞) (1 + 1/n)^n ≈ 2.71828182845...

e muncul secara alami dalam:
- Pertumbuhan kontinu (bunga, populasi)
- Probabilitas (distribusi normal)
- Kalkulus (turunan e^x = e^x)

f(x) = e^x disebut fungsi eksponensial natural.

## 6. Definisi Logaritma
log_b(x) = y  ⟺  b^y = x  (b > 0, b ≠ 1, x > 0)

- log_10(x) = log(x)  → logaritma umum (common log)
- log_e(x)  = ln(x)   → logaritma natural

## 7. Hukum-Hukum Logaritma
| Hukum | Rumus |
|-------|-------|
| Perkalian | log(ab) = log(a) + log(b) |
| Pembagian | log(a/b) = log(a) - log(b) |
| Pangkat | log(aⁿ) = n·log(a) |
| Perubahan basis | log_b(x) = log(x)/log(b) |
| Identitas | log_b(b) = 1, log_b(1) = 0 |
| Invers | b^(log_b(x)) = x |

## 8. Hubungan Invers
e^x dan ln(x) adalah fungsi invers satu sama lain:
- ln(e^x) = x untuk semua x
- e^(ln(x)) = x untuk x > 0

## 9. Persamaan Eksponen
Strategi: samakan basis, atau ambil logaritma kedua sisi.
- 2^x = 64 → 2^x = 2^6 → x = 6
- 3^x = 20 → x·ln(3) = ln(20) → x = ln(20)/ln(3)

## 10. Persamaan Logaritma
Strategi: konversi ke bentuk eksponen, atau gunakan hukum log.
- log(x) = 3 → x = 10^3 = 1000
- ln(2x-1) = 4 → 2x-1 = e^4 → x = (e^4+1)/2
- log(x) + log(x-3) = 1 → log[x(x-3)] = 1 → x(x-3) = 10

## 11. Model Pertumbuhan/Peluruhan Kontinu
P(t) = P₀ · e^(kt)
- k > 0: pertumbuhan (growth)
- k < 0: peluruhan (decay)

Waktu penggandaan: T₂ = ln(2)/k
Waktu paruh: T₁/₂ = ln(2)/|k|

## 12. Aplikasi Nyata
- pH = -log₁₀([H⁺])
- Skala Richter: M = log₁₀(I/I₀)
- Desibel: dB = 10·log₁₀(P/P₀)
- Bunga majemuk kontinu: A = Pe^(rt)
- Peluruhan radioaktif: N(t) = N₀·e^(-λt)
