from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np
import matplotlib.pyplot as plt

# Set tolerance for testing
tol = 1e-3

# Define constants
Delta_x = 0.2                  # Spatial step size
X_max = 40                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.001                # Time step size
T_max = 20                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

# Initial condition
x_series = np.linspace(0, X_max, x_size)  # Positions
t_0 = 10                                 # Initial time
u[:, 0] = np.array([soliton_solution(x, t_0) for x in x_series])  # Soliton at t=0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t)

# Analytical solution at different times
T_series = np.arange(0, 18, 3)  # Time steps for comparison
u_analytic = np.array([soliton_solution(x, t_0) for x in x_series])

# Calculate residual for a specific time
res_sq_sum = np.sum((u_solution[:, int(T_series[2] / Delta_t)] - 
                     np.array([soliton_solution(x, T_series[2] + t_0) for x in x_series])) ** 2)

# Plot results
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    numerical = u_solution[:, int(T_series[i] / Delta_t)]
    analytical = np.array([soliton_solution(x, T_series[i] + t_0) for x in x_series])
    ax.plot(x_series, numerical, ".", label="Numerical")
    ax.plot(x_series, analytical, label="Analytical")
    ax.set_title(f"t = {t_0 + T_series[i]}")
    ax.set_xlabel("x [A.U.]")
    ax.set_ylabel("Amplitude [A.U.]")
    ax.legend()

plt.tight_layout()
plt.savefig("Soliton_plot_try.png")
plt.show()

# Test function
def test_squared_residuals():
    for t in T_series[1:]:  # Skip the first time step as it is the initial condition
        numerical = u_solution[:, int(t / Delta_t)]
        analytical = np.array([soliton_solution(x, t + t_0) for x in x_series])
        res_sq_sum = np.sum((numerical - analytical) ** 2)
        assert res_sq_sum < tol, f"Residual {res_sq_sum} exceeds tolerance at t = {t + t_0}"
