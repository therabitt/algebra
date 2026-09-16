# 1.19 Teorema Binomial — Teori Lengkap

## 1. Definisi Koefisien Binomial
C(n,k) = n! / (k!(n-k)!)  =  "n pilih k"

Ini adalah jumlah cara memilih k elemen dari n elemen tanpa urutan.

## 2. Segitiga Pascal
Baris ke-n berisi C(n,0), C(n,1), ..., C(n,n).
```
n=0:     1
n=1:    1  1
n=2:   1  2  1
n=3:  1  3  3  1
n=4: 1  4  6  4  1
```
Aturan: C(n,k) = C(n-1,k-1) + C(n-1,k)  (setiap elemen = jumlah dua di atasnya)

## 3. Teorema Binomial
(a + b)ⁿ = Σₖ₌₀ⁿ C(n,k) · aⁿ⁻ᵏ · bᵏ

Contoh (a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴

## 4. Suku Umum (General Term)
Suku ke-(k+1): T_{k+1} = C(n,k) · aⁿ⁻ᵏ · bᵏ

## 5. Suku Tengah
- n genap: suku tengah ke-(n/2 + 1), yaitu T_{n/2+1} = C(n, n/2) · aⁿ/² · bⁿ/²
- n ganjil: dua suku tengah, T_{(n+1)/2} dan T_{(n+3)/2}

## 6. Identitas Binomial Penting
| Identitas | Rumus |
|-----------|-------|
| Jumlah satu baris | Σ C(n,k) = 2ⁿ |
| Alternating sum | Σ (-1)ᵏ C(n,k) = 0 |
| Jumlah rata-rata | Σ C(n,k)/2ⁿ = 1 (probabilitas) |
| Pascal | C(n,k) = C(n-1,k-1)+C(n-1,k) |
| Vandermonde | C(m+n,r) = Σ C(m,k)C(n,r-k) |

## 7. Aproksimasi Binomial
Untuk |x| << 1:  (1+x)ⁿ ≈ 1 + nx + n(n-1)x²/2! + ...

Penting di fisika dan engineering!
Contoh: (1+0.01)¹⁰ ≈ 1 + 10(0.01) = 1.10  (aktual: 1.10462...)

## 8. Distribusi Binomial (Preview)
P(X=k) = C(n,k) · pᵏ · (1-p)ⁿ⁻ᵏ
Probabilitas mendapat tepat k sukses dari n percobaan dengan probabilitas sukses p.
