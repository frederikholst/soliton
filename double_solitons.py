from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np
import matplotlib.pyplot as plt


# Define constants
Delta_x = 0.2                  # Spatial step size
X_max = 80                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.001                # Time step size
T_max = 20                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

# Initialize start condition
x_series = np.linspace(0, X_max, x_size)  # Positions
u[:, 0] = np.array([soliton_solution(x, t=0,c=1, x0=20.)+soliton_solution(x,t=0,c=2,x0=10.) for x in x_series])  # Soliton at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t) # Solutions for time up to T_max

# Extract six sample points from the solutions:
T_series=range(0,18,3)
u_sol_list=[u_solution[:, int(i / Delta_t)] for i in T_series]

# Save zip file:
np.savez('Data\\double_solitons.npz', u_sol=u_sol_list, x_series=x_series)