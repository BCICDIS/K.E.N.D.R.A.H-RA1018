# KENDRAH — Physics

**Module:** `.kendrah-ra1018/Physics/`
**Domain:** Physical Sciences, Simulation & Quantitative Reasoning
**Status:** Active

---

## Overview

The Physics module equips KENDRAH with deep capability in physical science reasoning, mathematical derivation, numerical computation, simulation, and the ability to apply physical principles to real-world problems. KENDRAH can operate across the full spectrum of physics — from classical mechanics and thermodynamics to quantum theory, electromagnetism, relativity, and modern theoretical physics.

Physics is KENDRAH's most quantitative domain. Precision, dimensional consistency, and mathematical rigor are non-negotiable.

---

## Branches of Physics Covered

| Branch                          | Topics                                                                       |
|---------------------------------|------------------------------------------------------------------------------|
| **Classical Mechanics**         | Kinematics, dynamics, Newton's laws, energy, momentum, rotation, oscillation|
| **Thermodynamics**              | Laws of thermodynamics, entropy, heat engines, phase transitions            |
| **Electromagnetism**            | Maxwell's equations, circuits, optics, electromagnetic waves                |
| **Quantum Mechanics**           | Wave-particle duality, Schrödinger equation, quantum states, uncertainty    |
| **Relativity**                  | Special and general relativity, spacetime, gravity, black holes             |
| **Fluid Mechanics**             | Fluid dynamics, Bernoulli, viscosity, turbulence, Navier-Stokes            |
| **Statistical Mechanics**       | Boltzmann distribution, partition functions, ensemble theory                |
| **Nuclear Physics**             | Nuclear structure, radioactive decay, fission, fusion                       |
| **Astrophysics**                | Stellar evolution, orbital mechanics, cosmology, dark matter/energy         |
| **Condensed Matter**            | Solid state physics, band theory, superconductivity, semiconductors         |
| **Plasma Physics**              | Ionized gases, MHD, plasma confinement, astrophysical plasmas               |
| **Optics**                      | Geometric and wave optics, interference, diffraction, lasers                |
| **Particle Physics**            | Standard Model, fundamental forces, particle interactions, collider physics |

---

## Core Capabilities

### Conceptual Explanation
- Explain any physical concept at any level — from intuitive analogies to graduate-level formalism
- Derive equations from first principles
- Explain the physical meaning behind mathematical expressions
- Connect abstract physics to observable phenomena

### Quantitative Problem Solving
- Solve numerical physics problems with full working shown
- Apply dimensional analysis to verify equations and identify errors
- Propagate uncertainty through calculations
- Convert between unit systems (SI, CGS, natural units, imperial)

Example:
```
Problem: A 2 kg block slides down a frictionless 30° incline of length 5 m. Find its velocity at the bottom.

Solution:
Height h = 5 × sin(30°) = 2.5 m
Energy conservation: ½mv² = mgh
v² = 2gh = 2 × 9.81 × 2.5 = 49.05
v = √49.05 ≈ 7.00 m/s
```

### Mathematical Physics
- Apply vector calculus, differential equations, linear algebra, and complex analysis in physical contexts
- Solve PDEs relevant to physics: wave equation, heat equation, Schrödinger equation, Laplace/Poisson
- Perform perturbation theory, variational methods, and Green's function analysis

### Computational Physics (Python)
- Simulate physical systems numerically using Python (NumPy, SciPy, Matplotlib)
- Solve ODEs and PDEs numerically: Euler, Runge-Kutta, finite difference
- Run Monte Carlo simulations for statistical physics problems
- Generate publication-quality physics plots and visualizations

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Simple harmonic oscillator
def sho(t, y, omega=1.0):
    return [y[1], -omega**2 * y[0]]

sol = solve_ivp(sho, [0, 20], [1, 0], dense_output=True)
t = np.linspace(0, 20, 300)
plt.plot(t, sol.sol(t)[0])
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Simple Harmonic Oscillator")
plt.savefig("sho.png")
```

### Physical Modeling
- Build mathematical models of physical systems from first principles or empirical data
- Validate models against physical constraints (conservation laws, symmetry, limiting cases)
- Estimate orders of magnitude using Fermi estimation

### Literature & Theory
- Summarize the current state of understanding in any branch of physics
- Explain the historical development of physical theories
- Compare competing physical theories and their experimental support
- Identify open problems and active research frontiers

---

## Physical Constants Reference

| Constant                        | Symbol | Value (SI)                            |
|---------------------------------|--------|---------------------------------------|
| Speed of light                  | c      | 2.998 × 10⁸ m/s                       |
| Planck's constant               | h      | 6.626 × 10⁻³⁴ J·s                    |
| Gravitational constant          | G      | 6.674 × 10⁻¹¹ N·m²/kg²               |
| Boltzmann constant              | k_B    | 1.381 × 10⁻²³ J/K                    |
| Elementary charge               | e      | 1.602 × 10⁻¹⁹ C                      |
| Electron mass                   | m_e    | 9.109 × 10⁻³¹ kg                     |
| Avogadro's number               | N_A    | 6.022 × 10²³ mol⁻¹                   |
| Permittivity of free space      | ε₀     | 8.854 × 10⁻¹² F/m                    |
| Permeability of free space      | μ₀     | 1.257 × 10⁻⁶ H/m                     |

---

## Commands

```
/physics explain "[concept]" --level [intuitive|undergrad|grad] — Explain a physics concept
/physics solve "[problem statement]"                             — Solve a physics problem
/physics derive "[equation or law]"                             — Derive from first principles
/physics simulate "[physical system]"                           — Generate Python simulation
/physics units "[expression]"                                   — Dimensional analysis
/physics model "[system description]"                           — Build physical model
/physics constants                                               — List physical constants
/physics research "[topic]"                                     — Summarize physics literature
```

---

## Example Tasks

- "Kendrah, derive the Lorentz transformation from the postulates of special relativity."
- "Kendrah, simulate a double pendulum in Python and plot the phase space."
- "Kendrah, explain quantum entanglement at a level suitable for a physics undergraduate."
- "Kendrah, calculate the escape velocity from the surface of Mars."
- "Kendrah, what is the current experimental status of detecting gravitational waves from primordial black holes?"
