import numpy as np
import matplotlib.pyplot as plt 

nx = 41 # no of grid points
dx = 2.0 / (nx - 1) # distance between grid points
nt = 20 # no of time steps
nu = 0.3 # kinematic viscosity or diffusion coefficient
dt = 0.0025 # length of time step

x = np.linspace(0, 2.0, nx)

u = np.ones(nx)
u[10:20] = 2.0
un = u.copy()

for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * (dt / dx**2) * (un[i+1] - 2 * un[i] + un[i-1])

plt.figure(figsize=(8, 5))
plt.plot(x, u, label='Diffusion (nu = 0.3)', color='royalblue', linewidth=2, marker='o', markersize=4, )
plt.title('1D Diffusion Equation Simulation')
plt.xlabel('Spatial Position (x)')
plt.ylabel('Velocity Field (u)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('diffusion_result.png', dpi=300)
plt.show()
plt.close()

print(
    "Success! Your diffusion simulation finished and saved 'diffusion_result.png' in your folder."
)