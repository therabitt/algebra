# 1.13 Basic Matrices / Matriks Dasar

## Overview / Gambaran Umum

Matrices (matriks) are rectangular arrays of numbers that encode linear
transformations, systems of equations, and multidimensional data.
This module builds matrix algebra from the ground up — from definition
to Gaussian elimination — and bridges to modern NumPy usage.

## What You Will Learn / Yang Akan Dipelajari

- **Definisi Matriks (Matrix Definition):** m×n arrays, element notation a_ij
- **Operasi Matriks (Matrix Operations):** add, subtract, scalar multiply, matrix multiply
- **Transpose, Trace, Determinant, Inverse**
- **Sistem Persamaan Linear (Linear Systems):** augmented matrices, row reduction
- **Gaussian Elimination:** step-by-step row operations
- **Applications:** transformations, graph theory, solving equations

## Prerequisites / Prasyarat

- Systems of linear equations (Topic 1.2)
- Basic function notation and algebra
- Python fundamentals (helpful)

## File Structure

| File | Description |
|------|-------------|
|  | Comprehensive theory with proofs and properties |
|  | Matrix class from scratch + NumPy comparison |
|  | Practice problems covering all operations |
|  | Geometric transformations, system solutions |
|  | LU decomposition, Strassen, eigenvalue iteration |

## Quick Reference / Referensi Cepat

### Matrix Multiplication
- (AB)_ij = Σ_k a_ik * b_kj
- Requires: cols(A) = rows(B)
- Result: rows(A) × cols(B)

### Determinant 2×2
- det([[a,b],[c,d]]) = ad - bc

### Inverse 2×2
- A^{-1} = (1/det(A)) * [[d,-b],[-c,a]]

### Gaussian Elimination
- Augment: [A|b]
- Row reduce to [I|x]

## Summary / Ringkasan

Matrices are the language of linear algebra — every rotation, scaling, and
projection you see in computer graphics is a matrix multiplication.
Mastering matrices opens the door to machine learning, data science,
physics simulations, and much more.
