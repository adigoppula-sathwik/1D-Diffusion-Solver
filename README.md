# 1D Diffusion Solver (CFD Step 3)

A Python implementation of the 1D Diffusion equation using an explicit Forward Euler time-stepping and Central Difference spatial-differencing scheme. This project serves as Step 3 in computational fluid dynamics (CFD), introducing viscous momentum dissipation, heat conduction, and physical smoothing phenomena.

---

## 🧠 Core Physical Concepts: Viscous Spreading & Gradient Smoothing

Unlike the convection models in Steps 1 and 2 where waves propagate horizontally across the domain like a conveyor belt, pure diffusion causes properties to stay anchored in place while expanding and flattening out.

### The Ink Drop Analogy
* Imagine dropping a dense block of ink into a narrow channel of water, or applying a concentrated burst of heat to the center of a metal rod.
* Instead of the entire block traveling sideways, molecular action causes the substance or heat to bleed outward symmetrically in all directions.
* This physical phenomenon causes sharp boundaries (like an initial square wave block) to naturally decay, rounding off corners and forming a smooth, bell-shaped Gaussian curve over time.

---

## 📌 Governing Equation

The 1D diffusion equation models how a field variable $u$ changes over time due to spatial diffusion driven by a kinematic viscosity or diffusion coefficient ($\nu$):

$$ \frac{\partial u}{\partial t} = \nu \frac{\partial^2 u}{\partial x^2} $$

---

## 🧮 Numerical Discretization

We discretize the domain into 40 spatial intervals ($\Delta x = 0.05$). We utilize a **Forward Euler** scheme in time (first-order accurate) and a **Central Difference** scheme in space for the second-order derivative, looking equally to both neighbors ($i+1$ and $i-1$):

$$ \frac{u_i^{n+1} - u_i^n}{\Delta t} = \nu \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2} $$

Solving for the unknown future velocity/concentration field $u_i^{n+1}$ yields our final programmable equation:

$$ u_i^{n+1} = u_i^n + \frac{\nu \Delta t}{\Delta x^2} \left( u_{i+1}^n - 2u_i^n + u_{i-1}^n \right) $$

---

## ⚙️ Simulation Setup & Parameters

| Parameter | Symbol | Value | Description |
| :--- | :--- | :--- | :--- |
| **Domain Length** | $L$ | `2.0` | Total physical size of the simulated space |
| **Grid Points** | $nx$ | `41` | Total number of stationary spatial sensors |
| **Spatial Step** | $\Delta x$ | `0.05` | Distance between grid points ($2.0 / 40$ intervals) |
| **Time Steps** | $nt$ | `20` | Number of temporal loop iterations |
| **Time Step Size** | $\Delta t$ | `0.0025` s | Duration of each time step used in the code |
| **Total Physical Time** | $t$ | `0.05` s | $nt \times \Delta t$ |
| **Kinematic Viscosity** | $\nu$ | `0.3` | Diffusion coefficient controlling spreading rate |

### Initial Conditions (Square Wave Block)
* $u = 2.0$ for $x \in [0.5, 1.0]$ (Indices 10 through 19)
* $u = 1.0$ everywhere else in the domain

---

## 💡 Key Numerical Insights

1. **Diffusion Fourier Number Stability:** Explicit time-stepping schemes for parabolic equations have a strict stability ceiling. With $\nu = 0.3$, $\Delta x = 0.05$, and $\Delta t = 0.0025$, the grid Fourier number evaluates to $\sigma = \frac{0.3 \times 0.0025}{0.0025} = 0.3$. Because $0.3 \le 0.5$, the stability criterion is safely satisfied, preventing numerical divergence.

2. **Stationary Spreading & Peak Decay:** Because there is no convection term, the center of the wave remains locked in place. However, lateral bleeding into neighboring cells causes the maximum peak value to drop (e.g., from $2.0$ down to $1.85$), systematically smoothing the initial discontinuities into a symmetric bell curve.

---

## 🚀 How to Run

### Prerequisites
* Python 3.x
* NumPy
* Matplotlib

### Execution
Run the solver from your terminal:
```bash
python main.py
