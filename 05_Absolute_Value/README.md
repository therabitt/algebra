# 1.15 Absolute Value / Nilai Mutlak

## Overview / Gambaran Umum

The absolute value (nilai mutlak) of a number measures its distance from zero
on the number line — ignoring direction. Simple in concept yet deep in
application, absolute value underlies inequalities, distance metrics,
error analysis, and the generalization to norms in higher mathematics.

## What You Will Learn / Yang Akan Dipelajari

- **Definisi (Definition):** piecewise definition and geometric meaning
- **Properti (Properties):** non-negativity, symmetry, multiplicativity, triangle inequality
- **Persamaan Nilai Mutlak (Equations):** |ax+b| = c, |x| = |y|
- **Pertidaksamaan Nilai Mutlak (Inequalities):** |x| < a, |x| > a and their solution sets
- **Fungsi Nilai Mutlak (Function):** graph, transformations, reflections
- **Jarak (Distance):** |x - y| as distance between x and y
- **Complex Modulus:** |a+bi| = √(a²+b²)
- **Generalization:** L1 norm, Chebyshev distance, taxi-cab geometry

## Prerequisites / Prasyarat

- Real number line and number ordering
- Basic algebra and inequalities (Topic 1.6)
- Functions and graphs (helpful)

## File Structure

| File | Description |
|------|-------------|
|  | Full theory with proofs of all properties |
|  | Python implementations: equations, inequalities, distances |
|  | Practice problems with step-by-step solutions |
|  | Plots of |x|, transformations, solution sets on number line |
|  | L1 norm, Chebyshev distance, taxicab geometry |

## Quick Reference / Referensi Cepat

### Definition
|x| = x   if x ≥ 0
|x| = -x  if x < 0

### Key Properties
- |x| ≥ 0 always
- |xy| = |x||y|
- |x+y| ≤ |x| + |y|  (Triangle Inequality)

### Solving |ax+b| = c (c > 0)
- ax+b = c  OR  ax+b = -c

### Solving |x| < a (a > 0)
- Solution: -a < x < a

### Solving |x| > a (a > 0)
- Solution: x < -a  OR  x > a

## Summary / Ringkasan

Absolute value is the gateway to metric spaces and norms — the mathematical
formalization of "distance." From error bounds in engineering to gradient
descent in machine learning (L1 regularization), its applications are
everywhere in applied mathematics.
