from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np
import matplotlib.pyplot as plt


# Define constants
Delta_x = 0.8                  # Spatial step size
X_max = 80                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.0005               # Time step size
T_max = 40                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

# Define gaussian
def gaussian(x, mu, sig):
    return (
        1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.0) / 2)
    )

# Initialize start condition
x_series = np.linspace(0, X_max, x_size)  # Positions                                 # Initial time
u[:, 0] = np.array([gaussian(x, X_max/2, 8) for x in x_series])  # gaussian at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t,mu=0) # Solutions for time up to T_max, with mu=0

# Extract six sample points from the solutions:
T_series=range(0,42,7)
u_sol_list=[u_solution[:, int(i / Delta_t)] for i in T_series]

# Save zip file:
np.savez('Data\\burgers.npz', u_sol=u_sol_list, x_series=x_series)