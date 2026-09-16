# 1.15 Nilai Mutlak — Teori Lengkap

## 1. Definisi
|x| = { x   jika x ≥ 0
       { -x  jika x < 0

Ini adalah fungsi piecewise. Selalu menghasilkan nilai non-negatif.

## 2. Interpretasi Geometri
|x| = jarak dari x ke titik 0 pada garis bilangan
|x - a| = jarak dari x ke a pada garis bilangan

## 3. Sifat-Sifat Nilai Mutlak
| Sifat | Rumus | Catatan |
|-------|-------|---------|
| Non-negatif | |x| ≥ 0 | selalu |
| Definitif | |x| = 0 ⟺ x = 0 | hanya nol bernilai nol |
| Simetri | |-x| = |x| | |
| Perkalian | |xy| = |x|·|y| | |
| Pembagian | |x/y| = |x|/|y|, y≠0 | |
| Kuadrat | |x|² = x² | |
| Akar | √(x²) = |x| | bukan x! |

## 4. Ketidaksamaan Segitiga (Triangle Inequality)
|x + y| ≤ |x| + |y|  untuk semua x, y ∈ R

Bukti:
-(|x|) ≤ x ≤ |x|  dan  -(|y|) ≤ y ≤ |y|
Menjumlahkan: -(|x|+|y|) ≤ x+y ≤ |x|+|y|
Artinya: |x+y| ≤ |x|+|y|  ∎

Ketidaksamaan segitiga terbalik:
||x| - |y|| ≤ |x - y|

## 5. Persamaan Nilai Mutlak
|ax + b| = c  (c > 0):
  → ax + b = c  atau  ax + b = -c

|ax + b| = |cx + d|:
  → ax + b = cx + d  atau  ax + b = -(cx + d)

## 6. Pertidaksamaan Nilai Mutlak
| Tipe | Ekuivalen | Solusi |
|------|-----------|--------|
| |x| < a (a>0) | -a < x < a | interval (-a, a) |
| |x| ≤ a (a>0) | -a ≤ x ≤ a | interval [-a, a] |
| |x| > a (a>0) | x < -a atau x > a | dua ray |
| |x| ≥ a (a>0) | x ≤ -a atau x ≥ a | dua ray |

Untuk |x - k| < d:  ini berarti "jarak dari x ke k kurang dari d"
  → k - d < x < k + d

## 7. Fungsi Nilai Mutlak f(x) = |x|
- Grafik: huruf V, vertex di (0,0)
- Domain: (-∞, ∞)
- Range: [0, ∞)
- Tidak terdiferensialkan di x = 0

## 8. Transformasi Fungsi Mutlak
| Fungsi | Transformasi |
|--------|-------------|
| |x - h| | geser kanan h |
| |x| + k | geser atas k |
| a|x| | stretch vertikal faktor a |
| |ax| | compress horizontal faktor 1/a |
| -|x| | refleksi terhadap sumbu x |

## 9. Nilai Mutlak Dua Variabel
|x - y| = jarak antara x dan y pada garis bilangan
Berguna untuk: batas error, toleransi, jarak

## 10. Modulus Bilangan Kompleks
|a + bi| = √(a² + b²)
Ini adalah jarak dari a+bi ke origin di bidang kompleks.
Sifat: |z₁z₂| = |z₁||z₂|,  |z₁/z₂| = |z₁|/|z₂|

## 11. Norma (Generalisasi)
Nilai mutlak adalah kasus khusus norma pada ruang vektor.
Lp norm: ||x||_p = (|x₁|^p + ... + |xₙ|^p)^(1/p)
- p=1: L1 norm (Manhattan / taxicab distance)
- p=2: L2 norm (Euclidean distance, nilai mutlak biasa)
- p=∞: L∞ norm = max(|xᵢ|) (Chebyshev distance)
