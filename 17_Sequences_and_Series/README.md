# 1.12 Sequences and Series / Barisan dan Deret

## Overview / Gambaran Umum

Sequences (barisan) and series (deret) are foundational concepts in mathematics,
bridging arithmetic patterns with the power of infinite summation. This module
explores how ordered lists of numbers behave and how their sums can converge to
finite values — or diverge to infinity.

## What You Will Learn / Yang Akan Dipelajari

- **Barisan (Sequences):** arithmetic, geometric, Fibonacci, and other special sequences
- **Deret (Series):** finite and infinite sums, sigma notation
- **Convergence & Divergence:** when does an infinite sum give a finite answer?
- **Rumus Jumlah (Sum Formulas):** for arithmetic and geometric series
- **Applications:** compound interest, Zeno's paradox, fractal geometry

## Prerequisites / Prasyarat

- Algebra basics (functions, exponents)
- Basic summation concepts
- Understanding of limits (helpful but not required)

## File Structure

| File | Description |
|------|-------------|
|  | Full theoretical treatment with proofs |
|  | Working Python implementations of all concepts |
|  | Practice problems with full solutions |
|  | Matplotlib plots: convergence, spirals, partial sums |
|  | Golden ratio, Collatz conjecture, convergence tests |

## Quick Reference / Referensi Cepat

### Arithmetic Sequence
- **General term:** a_n = a_1 + (n-1)d
- **Sum:** S_n = n(a_1 + a_n)/2

### Geometric Sequence
- **General term:** a_n = a_1 * r^(n-1)
- **Sum:** S_n = a_1(1 - r^n)/(1 - r)
- **Infinite sum (|r|<1):** S = a_1/(1 - r)

### Fibonacci
- F_1=1, F_2=1, F_n = F_{n-1} + F_{n-2}
- Ratio F_{n+1}/F_n → φ (golden ratio ≈ 1.618...)

## Summary / Ringkasan

Sequences give us structure; series give us power. The ability to sum infinitely
many terms and arrive at a finite answer (convergence) is one of mathematics'
most profound ideas — underpinning calculus, physics, and computer science.
