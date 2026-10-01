# 1.1 Sistem Bilangan (Number Systems) — Teori Lengkap

## Apa itu Sistem Bilangan?

Sistem bilangan adalah cara kita mengklasifikasikan, mengorganisir, dan bekerja dengan
bilangan-bilangan. Setiap "sistem" adalah himpunan bilangan dengan sifat-sifat tertentu.

---

## Hierarki Sistem Bilangan

```
C (Bilangan Kompleks)
└── R (Bilangan Real)
    ├── Q (Bilangan Rasional)
    │   ├── Z (Bilangan Bulat)
    │   │   ├── W (Bilangan Cacah)
    │   │   │   └── N (Bilangan Asli / Natural)
    │   │   └── {..., -3, -2, -1}
    │   └── {p/q | p,q ∈ Z, q ≠ 0}
    └── Irasional (√2, π, e, ...)
```

> Notasi: N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C

---

## 1. Bilangan Asli (Natural Numbers) — N

**Definisi:** Bilangan yang digunakan untuk menghitung: {1, 2, 3, 4, 5, ...}
(Beberapa definisi menyertakan 0, tergantung konvensi — di sini N = {1,2,3,...})

**Sifat-sifat:**
- Tertutup terhadap penjumlahan: a,b ∈ N → a+b ∈ N
- Tertutup terhadap perkalian: a,b ∈ N → a×b ∈ N
- TIDAK tertutup terhadap pengurangan: 3-5 = -2 ∉ N
- TIDAK tertutup terhadap pembagian: 3/4 ∉ N
- **Well-Ordering Principle**: setiap himpunan non-kosong bilangan asli punya elemen terkecil

**Prinsip Induksi Matematika:** Jika P(1) benar, dan P(k)→P(k+1), maka P(n) benar untuk semua n ∈ N.
> metode pembuktian rumus atau pernyataan matematika yang berlaku untuk semua bilangan asli atau bilangan bulat tertentu.
> metode ini bekerja seperti efek domino. 

---

## 2. Bilangan Cacah (Whole Numbers) — W

**Definisi:** Bilangan asli ditambah nol: W = {0, 1, 2, 3, ...}

**Peran Nol:** Nol adalah elemen identitas penjumlahan: a + 0 = a untuk semua a.
Nol bukan positif, bukan negatif — netral.

---

## 3. Bilangan Bulat (Integers) — Z

**Definisi:** Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}

"Z" dari kata Jerman "Zahlen" (bilangan).

**Sifat-sifat tambahan:**
- Tertutup terhadap pengurangan: a,b ∈ Z → a-b ∈ Z
- Setiap bilangan punya negatif (invers penjumlahan): a + (-a) = 0
- Urutan total: untuk a,b ∈ Z, tepat satu dari: a<b, a=b, a>b

---

## 4. Bilangan Rasional (Rational Numbers) — Q

**Definisi formal:** Q = { p/q | p ∈ Z, q ∈ Z, q ≠ 0 }

"Q" dari kata Latin "Quotiens" (hasil bagi).

**Representasi desimal:** Bilangan rasional selalu memiliki ekspansi desimal yang:
- Berakhir (terminasi): contoh 1/4 = 0.25
- Atau berulang: contoh 1/3 = 0.333... = 0.3̄

**Mengubah desimal berulang ke pecahan:**
Contoh: x = 0.142857142857...
  → 10x = 1.42857142857...
  → 1000000x = 142857.142857...
  → 999999x = 142857
  → x = 142857/999999 = 1/7

**Rumus cepat:**
jumlah digit yang berulang menentukan jumlah angka 9 di bagian penyebut (bawah):

> - 0.333...  → 3/9 = 1/3
> - 0.2525... → 25/99
> - 0.142857... → 142857/999999 = 1/7

---

## 5. Bilangan Irasional (Irrational Numbers)

**Definisi:** Bilangan real yang TIDAK bisa ditulis sebagai p/q (p,q ∈ Z, q≠0).
Ekspansi desimalnya **tidak berakhir** DAN **tidak berulang**.

**Contoh terkenal:**
- √2 ≈ 1.41421356237...
- π ≈ 3.14159265358...
- e ≈ 2.71828182845...
- φ (golden ratio) = (1+√5)/2 ≈ 1.61803398874...

> **Bukti bahwa √2 irasional (`proof by contradiction`):**
>
> > Asumsikan √2 = p/q dalam bentuk paling sederhana (gcd(p,q)=1).
> > Maka 2 = p²/q² → p² = 2q²
> > Berarti p² genap → p genap → tulis p = 2k
> > Maka (2k)² = 2q² → 4k² = 2q² → q² = 2k²
> > Berarti q² genap → q genap.
> > KONTRADIKSI: p dan q keduanya genap, padahal gcd(p,q)=1.
> > Kesimpulan: √2 tidak rasional. ∎

> **Fact!!**
> Pembuktian kontradiksi pada √2 (akar 2) adalah salah satu pembuktian paling dramatis dalam sejarah matematika kuno oleh Hippasus.
> Pembuktian yang sangat epik karena berhasil menghancurkan keyakinan dasar bangsa Yunani Kuno (kamu Pythagorean)
> yang percaya bahwa seluruh alam semesta bisa dijelaskan dengan bilangan bulat dan rasionya (pecahan).

---

## 6. Bilangan Real (Real Numbers) — R

**Definisi:** Gabungan bilangan rasional DAN irasional.
R = Q ∪ Irasional

**Sifat kelengkapan (Completeness):** Setiap himpunan bilangan real yang dibatasi dari
atas memiliki supremum (batas atas terkecil) di R. Ini yang membedakan R dari Q.

**Garis bilangan:** Setiap titik pada garis bilangan berkorespondensi dengan tepat satu
bilangan real, dan setiap bilangan real berkorespondensi dengan tepat satu titik.

**Sifat kerapatan (Density):** Antara dua bilangan real yang berbeda, selalu ada bilangan
real lain (bahkan tak hingga banyaknya).

**Prinsip Archimedes:** Untuk setiap x ∈ R, ada n ∈ N sehingga n > x.

---

## 7. Bilangan Kompleks (Complex Numbers) — C

**Definisi:** C = { a + bi | a, b ∈ R } di mana i = √(-1), i² = -1

- a disebut bagian real: Re(z) = a
- b disebut bagian imajiner: Im(z) = b
**Kondisi khusus:**
- Jika b=0: z => bilangan real biasa/ z = a + 0i => z = a (real)
- Jika a=0, b≠0: z => bilangan imajiner murni/ z = 0 + bi => z = bi (imajiner)

> ![Notes]
> _bisa disimpulkan!_
> bilangan real adalah bilangan kompleks yang memiliki bagian imajiner (z = a + bi): 0 (z = a + 0i => z = a)

**Bidang kompleks (Complex Plane / Argand Diagram):**
- Sumbu horizontal: bagian real
- Sumbu vertikal: bagian imajiner
- Modulus/ nilai mutlak: |z| = |a + bi| = `√(a² + b²)` => jarak dari titik asal (0,0) ke titik koordinat bilangan kompleks(z) 
> contoh => z = 3 + 4i
> |z| = √(3²+4²) = √(9+16) = √25 
> |z| = 5
> **kesimpulan**: jarak lurus dari posisi awal (0,0) ke titik z adalah tepat *5* satuan langkah.
- Argumen: `θ = arctan(b/a)` => besaran sudut yang dihasilkan dari rasio kecuraman (segitiga)
> contoh (sudut istimewa):
> rasio= 1 => θ = 45° (z = 3 + 3i)
> rasio= √3 (1.73) => θ = 60° (z = 1 + √3i)
> rasio= 1/√3 (0.57) => θ = 30° (z = √3i)
- Konjugat (z_conj): > `z = a + bi` => `z_conj = a - bi`, "kembaran cermin" dengan membalik tanda bagian imajiner:
> *contoh => z = 3 + 4i => z_conj = 3 - 4i*
> fungsi utama: sebagai cairan pembersih huruf i. 
> jika dikalikan dengan dirinya sendiri, bagian imajiner musnah total dan berubah menjadi bilangan real biasa: 
> - `z × z_conj = |z|²`
> > `z × z_conj = a² × b²` => `|z|² = a² × b²`
> > *hubungan mutlak:*
> > *z × z_conj = (3 + 4i) × (3 - 4i) = `3² - (4i)²` = 9 - 16(-1) = **25***.
> > *|z|² = √3² + 4² = `3² + 4²` = 9 + 16 = **25***


**Bentuk polar:** `z = r(cos θ + i sin θ) = re^(iθ)`
> _cara berbeda untuk menunjuk tempat yang sama_
> **contoh:**
> z = 5, θ = 53,13°
> z = 5(cosθ + i sinθ)
> z = 5(cos(53,13°) + i sin(53,13°))
> z = 5(0.6 + i 0.8)
> z = 3 + 4i

### **Formula Euler:** `e^(iθ) = cos(θ) + *i*sin(θ)
> > ![Concept]
> pangkat imajiner e^(iθ) bertindak sebagai mesin rotasi,
> di mana satuan imajiner i membelokkan pertumbuhan alami e sebesar 90° secara terus-menerus hingga membentuk lintasan lingkaran sempurna.
>
> > **Euler's Identity: `e^(iπ) + 1 = 0`**
> adalah kondisi saat rotasi dihentikan tepat pada sudut 180 derajat (pi), 
> menciptakan lintasan setengah lingkaran (kubah) dan mendarat di -1 pada sumbu Real 
> - `(e^(iπ) = -1 => e^(iπ) + 1 = 0)`.
>
> > Fact!!
> > formula ini dinobatkan sebagai persamaan matematika paling indah di dunia,
> > karena berhasil menyatukan 5 konstanta paling penting yang awalnya tidak saling berhubungan:
> 
> - e ≈ 2.71828182845... (konstanta pertumbuhan alami dari kalkulus)
> - i = √-1 (satuan imajiner dari aljabar)
> - π ≈ 3.14159265358... (konstanta lingkaran dari geometri)
> - 1 = (identitas perkalian)
> - 0 = (identitas penjumlahan)
```

    ▲ (Im)
    │
4  ─┼────────────● z = 3 + 4i
    │           ╱│
    │         ╱  │
    │        ╱   │
    │      ╱|z|  │ b
    │     ╱      │
    │   ╱        │
    │ ╱θ        †│ 90°
0  ─┼───────────┴┴───────────► (Re)
    0     a      3

```
> ![Notes]
> **Kesimpulan,** Bilangan kompleks terbagi dalam beberapa bentuk diantaranya:
> - bentuk kartesius (rektangular): `z = a + bi`
> - bentuk polar: `z = r(cosθ + i sinθ)`
> - bentuk eksponensial: `z = re^iθ`
>
> > !! Important 
> Setiap kali kita menaikkan dimensi sistem bilangan ke tingkat yang lebih tinggi, kita harus mengorbankan/ "kehilangan" satu sifat dasar matematika.
> Konsep ini dijelaskan secara sistematis melalui melalui metode ***Konstruksi Cayley-Dickson***
>
> *Lebih lengkap dijelaskan di point History*


---

## 8. Notasi Interval

| Notasi | Makna | Contoh |
|--------|-------|--------|
| (a, b) | a < x < b (terbuka) | (1, 5): 1 < x < 5 |
| [a, b] | a ≤ x ≤ b (tertutup) | [1, 5]: 1 ≤ x ≤ 5 |
| [a, b) | a ≤ x < b (setengah terbuka) | [0, 1): 0 ≤ x < 1 |
| (a, b] | a < x ≤ b | (0, 1]: 0 < x ≤ 1 |
| (a, ∞) | x > a | (3, ∞): x > 3 |
| (-∞, b] | x ≤ b | (-∞, 0]: x ≤ 0 |
| (-∞, ∞) | semua bilangan real | R |

> ![Notes]
> Tak hingga (∞) bukanlah sebuah angka konkrit yang bisa ditentukan berapa nilainya,
> melainkan sebuah konsep arah perjalanan yang tidak pernah ada ujungnya.
> Karena itu simbol Tak hingga (∞) harus selalu ditulis menggunakan kurung biasa.
> Contoh: `(a, ∞)`

---

## 9. Nilai Mutlak (Absolute Value) — Definisi Awal

|x| = { x,  jika x ≥ 0
      { -x, jika x < 0

Interpretasi geometri: jarak dari x ke titik 0 pada garis bilangan.
Topik ini dibahas lengkap di 1.15.

> ![Notes]
> Dalam dunia fisik, konsep jarak tidak pernah bernilai negatif.

---

## 10. Fungsi Lantai dan Plafon (Floor & Ceiling)

**Floor:** ⌊x⌋ = bilangan bulat terbesar yang ≤ x
Contoh: ⌊3.7⌋ = 3, ⌊-2.3⌋ = -3

**Ceiling:** ⌈x⌉ = bilangan bulat terkecil yang ≥ x
Contoh: ⌈3.2⌉ = 4, ⌈-2.7⌉ = -2

---

## 11. Sifat-Sifat Operasi (Preview)

Untuk bilangan real a, b, c:
1. Komutatif: a+b = b+a, a×b = b×a
2. Asosiatif: (a+b)+c = a+(b+c), (a×b)×c = a×(b×c)
3. Distributif: a×(b+c) = a×b + a×c
4. Elemen identitas: a+0=a (penjumlahan), a×1=a (perkalian)
5. Invers: a+(-a)=0 (penjumlahan), a×(1/a)=1 jika a≠0 (perkalian)

---


# History

## Sejarah Korban Jiwa Demi Akar 2 (Hippasus & Kaum Pythagorean)

**~500 SM** — Kaum Pythagorean percaya satu dogma mutlak:

> **"Semua adalah bilangan"** — semua yang ada di alam semesta bisa dijelaskan lewat bilangan bulat dan rasionya.

Musik, geometri, kosmos — semuanya adalah rasio. Mereka merasa telah menemukan bahasa sejati alam semesta.

**Yang terjadi:**
- **Hippasus** (salah satu anggota Pythagorean) mencoba: berapa nilai √2 dalam bentuk p/q?
- Ia membuktikan secara formal — *menggunakan kontradiksi* — bahwa **√2 tidak bisa ditulis sebagai rasio apapun**
- Artinya: ada bilangan yang berada di luar seluruh sistem kepercayaan mereka

> **!! Facts:**
> Menurut legenda, Hippasus **dibunuh dan dibuang ke laut** karena dianggap mengkhianati kebenaran.

*Apakah benar terjadi? Sejarawan masih berdebat. Tapi satu hal pasti: mereka berusaha keras menyembunyikan penemuan ini dari publik.*

---

## Penolakan Angka Khayalan (i = √-1)

**Pertanyaan yang memicu segalanya:** Berapa x jika **x² = -1** ?

Selama berabad-abad, jawaban standar adalah: *"Tidak ada. Pertanyaan itu tidak masuk akal."*

**Kronologi:**

| Tahun | Tokoh | Peran |
|---|---|---|
| 1545 | **Gerolamo Cardano** | Formula kubik — di tengah perhitungan muncul √(-121) |
| 1572 | **Rafael Bombelli** | Nekat "pura-pura" √(-1) valid → hasilnya ternyata **benar** |
| 1637 | **René Descartes** | Memberi nama *"bilangan imajiner"* — sebagai **ejekan** |
| ~1800 | **Carl Friedrich Gauss** | Memberi legitimasi geometris: i = **rotasi 90°** pada bidang |

> *Leibniz menyebutnya: "makhluk amfibi antara ada dan tidak ada."*

**Kesimpulan:**
Setelah Gauss memetakannya ke bidang 2D, i bukan lagi "khayalan" — ia mendeskripsikan rotasi yang nyata. Hari ini bilangan kompleks dipakai di: teknik listrik, mekanika kuantum, grafis komputer, pemrosesan sinyal.

---

## Obsesi Triplet dan Kisah Epik di Jembatan Brougham (Sir William Rowan Hamilton)

**Konteks masalah:**
- Bilangan kompleks `a + bi` → sempurna untuk rotasi di **2D**
- Fisika butuh **3D** → logikanya adalah "bilangan triplet" `a + bi + cj`

**Sir William Rowan Hamilton** menghabiskan **>10 tahun** gagal mendefinisikan perkalian triplet yang konsisten. Setiap percobaan berakhir kontradiksi.

> Istrinya tiap pagi bertanya: *"Sudah bisa kalikan triplet, William?"*
> Hamilton tiap hari menjawab: *"Belum bisa."*

**16 Oktober 1843 — Momen eureka:**

Hamilton sedang berjalan di tepi Kanal Kerajaan Dublin. Tiba-tiba tersadar:

> **Triplet tidak cukup. Butuh 4 dimensi: `a + bi + cj + dk`**
> Dan untuk itu, ia harus **melepaskan sifat komutatif** (a×b = b×a).
```
i² = j² = k² = ijk = -1
ij = k,   ji = -k
jk = i,   kj = -i
ki = j,   ik = -j
```
Begitu semangatnya Hamilton, ia **mengeluarkan pisau lipat dan mengukir `ij = k` di batu Jembatan Brougham**

> Ukiran aslinya hilang, tapi **plakat peringatan** ada di sana hingga hari ini.

Sistem baru ini disebut **Quaternion** — pertama kalinya manusia sengaja menciptakan aljabar **tidak komutatif**. Kini dipakai di: grafis 3D, robotika, navigasi satelit, fisika kuantum.

---

## Misteri Konstruksi Cayley-Dickson: Kehilangan Sifat Dasar Matematika

**Pola yang ditemukan** — setiap kali sistem bilangan naik dimensi, satu sifat fundamental hilang:

| Sistem | Dimensi | Sifat yang Hilang |
|---|---|---|
| **Real (ℝ)** | 1 | — *(semua sifat utuh)* |
| **Kompleks (ℂ)** | 2 | Urutan total (`a > b` tidak berlaku) |
| **Quaternion (ℍ)** | 4 | Komutatif (`a×b ≠ b×a`) |
| **Octonion (𝕆)** | 8 | Asosiatif (`(a×b)×c ≠ a×(b×c)`) |
| **Sedenion (𝕊)** | 16 | Zero-divisor (`a×b = 0` meski `a,b ≠ 0`) |


### Alur Historis: Sebelum Cayley-Dickson

Konstruksi Cayley-Dickson baru ada **setelah** semua sistem ditemukan. Para penemu terdahulu masing-masing punya cara berbeda:

| Sistem | Penemu | Metode Penemuan |
|---|---|---|
| **Kompleks (ℂ)** | Cardano, Bombelli (~1570) | *Terpaksa* pakai `√−1` saat menyelesaikan persamaan kubik — awalnya dianggap "bilangan khayalan" |
| **Quaternion (ℍ)** | Hamilton (1843) | Trial-and-error selama **10 tahun**: coba 3D gagal, akhirnya *terpaksa* ke 4D; mendefinisikan aturan `i²=j²=k²=ijk=−1` secara eksplisit |
| **Octonion (𝕆)** | Graves (1843), Cayley (1845) | "**Doubling trick**": gandakan Quaternion jadi pasangan `(q₁, q₂)`, lalu definisikan perkalian baru — ini cikal bakal konstruksi Cayley-Dickson |

**Alur lengkapnya:**

```
Bilangan Real (ℝ)
      │
      │ ~1570 — Bombelli: paksa √−1 masuk untuk
      │         menyelesaikan persamaan kubik
      ▼
Bilangan Kompleks (ℂ)  ← ditemukan "dari kebutuhan", bukan desain
      │
      │ 1843 — Hamilton: coba bangun geometri 3D selama 10 tahun
      │        → gagal terus → sadar butuh dimensi ke-4
      │        → ukir aturan i,j,k di jembatan Brougham
      ▼
Quaternion (ℍ)  ← ditemukan lewat eksperimen dan intuisi geometri
      │
      │ 1843 — Graves (2 bulan setelah Hamilton):
      │        "bagaimana kalau Quaternion digandakan lagi?"
      │        → pasangkan dua Quaternion → Octonion
      │        (Cayley publikasikan lebih dulu di 1845)
      ▼
Octonion (𝕆)  ← ditemukan lewat "doubling trick" ad-hoc
      │
      │ 1919 — Dickson: sadar semua langkah ini punya
      │        pola tunggal → formalisasi jadi satu rumus
      ▼
Konstruksi Cayley-Dickson  ← baru ini yang sistematis & berlanjut ke ∞
      │
      ├─→ Sedenion (𝕊, dim 16)
      ├─→ Trigintaduonion (dim 32)
      └─→ dan seterusnya...
```

> **Kunci:** Para penemu asli *tidak* punya blueprint. Setiap sistem ditemukan karena **terpaksa** oleh masalah yang tidak bisa diselesaikan di dimensi sebelumnya. Cayley-Dickson justru datang **belakangan** — melihat ke belakang dan berkata: *"Oh, ternyata semua ini satu pola yang sama."*

---

**Konstruksi Cayley-Dickson** (Cayley 1845, Dickson 1919):
- Setiap naik level → ambil **pasangan** dari sistem sebelumnya, definisikan perkalian baru
- Dimensi **×2**, tapi **satu sifat aljabar hilang**

> Seperti hukum konservasi fisika: **untuk mendapat sesuatu, harus melepas sesuatu yang lain.**

**Teorema Hurwitz (1898):**
> Satu-satunya sistem dengan norma perkalian `|ab| = |a||b|` adalah: **ℝ, ℂ, ℍ, 𝕆**. Tidak ada yang lain.

Setelah Octonion, terlalu banyak sifat yang hilang untuk berguna secara praktis. Sedenion hampir hanya ada di matematika murni.

> *Matematika bukan tentang sistem "sempurna" — melainkan memahami **apa yang bisa dan tidak bisa ada bersama** dalam satu sistem yang konsisten.*

---

## Kelahiran Nol: Bilangan yang Hampir Tidak Pernah Ada

**Nol bukan bilangan yang "ditemukan" — ia harus diperjuangkan selama ribuan tahun.**

**Kronologi:**

| Periode | Peradaban | Status Nol |
|---|---|---|
| ~3000 SM | Babilonia | Placeholder saja (spasi kosong di antara angka) |
| ~300 SM | Yunani | **Ditolak** — "bagaimana ketiadaan bisa jadi bilangan?" |
| ~628 M | **Brahmagupta (India)** | Pertama mendefinisikan nol sebagai **bilangan** dengan aturan aritmetika |
| ~825 M | Al-Khawarizmi (Arab) | Menyebarkan konsep nol ke dunia Islam lewat sistem desimal |
| ~13 M | Fibonacci (Eropa) | Memperkenalkan nol ke Eropa — disambut dengan **resistensi keras** |

**Mengapa Eropa menolak nol?**
- Gereja menganggap nol sebagai simbol "ketiadaan" yang bertentangan dengan konsep Tuhan yang "penuh"
- Beberapa kota di Italia sempat **melarang penggunaan angka Arab** (termasuk nol) karena dianggap "sihir"
- Pedagang takut nol bisa dipakai untuk memalsukan angka di kontrak

**Aturan Brahmagupta untuk nol** (628 M):
```
a + 0 = a
a − 0 = a
a × 0 = 0
0 ÷ 0 = 0   ← keliru, tapi revolusioner untuk zamannya
```
> Brahmagupta salah soal `0 ÷ 0`, tapi **benar dalam segala hal lainnya** — 12 abad sebelum Eropa menerimanya.

Tanpa nol: tidak ada sistem posisional, tidak ada kalkulus, tidak ada komputer.

---

## Cantor & Perang Tak-Hingga: Ada Tak-Hingga yang Lebih Besar

**Georg Cantor** (1845–1918) mengajukan pertanyaan yang tampak konyol:

> *"Apakah semua tak-hingga itu sama besarnya?"*

Jawabannya menggemparkan dunia matematika: **tidak.**

**Penemuan kunci:**

Cantor membuktikan bahwa bilangan **rasional (Q) bisa dipasangkan satu-satu dengan bilangan asli (N)** — artinya "jumlahnya" sama meski Q terlihat jauh lebih padat.
```
N: 1,  2,  3,  4,  5, ...
Q: 1/1, 1/2, 2/1, 1/3, 3/1, ... (diagonal counting)
```
Tapi bilangan **real (R) tidak bisa** — selalu ada yang "lolos". Ia membuktikannya dengan **Diagonal Argument**:

> Asumsikan semua bilangan real di (0,1) bisa didaftarkan.
> Konstruksi bilangan baru dengan mengubah digit diagonal ke-n dari baris ke-n → bilangan baru ini **pasti tidak ada dalam daftar**. Kontradiksi.

**Kesimpulan:**

| Himpunan | Kardinalitas | Simbol |
|---|---|---|
| N, Z, Q | Tak-hingga hitung (*countable*) | ℵ₀ (aleph-nol) |
| R, C | Tak-hingga tak-hitung (*uncountable*) | **ℵ₁ > ℵ₀** |

> **|R| > |Q|** meski keduanya tak-hingga. Ada lebih banyak bilangan irasional daripada yang bisa kita hitung seumur hidup alam semesta.

**Harga yang dibayar Cantor:**

Temuannya ditolak keras oleh komunitas matematika, terutama oleh **Leopold Kronecker** yang menyebutnya *"penipu"* dan *"perusak generasi muda matematika."*

- Cantor berkali-kali mengalami depresi berat
- Ia meninggal di rumah sakit jiwa pada 1918
- Beberapa dekade setelahnya, David Hilbert berkata:

> *"Tidak seorang pun akan bisa mengusir kita dari surga yang telah Cantor ciptakan."*

Hari ini, teori himpunan Cantor adalah **fondasi dari seluruh matematika modern**.

---

*Topik berikutnya: 1.2 — Operasi Dasar & Sifat-Sifatnya*









