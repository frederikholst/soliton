from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np
import matplotlib.pyplot as plt


# Define constants
Delta_x = 0.2                  # Spatial step size
X_max = 40                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.001                # Time step size
T_max = 20                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

# define the kink initial conditions
def kink(x,x0,sig=1):
    return 0.5*(1-np.tanh(x-x0/sig))

# Initialize start condition
x_series = np.linspace(0, X_max, x_size)  # Positions
t_0 = 10                                  # Initial time
u[:, 0] = np.array([kink(x,X_max/2) for x in x_series])  # Soliton at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t, bounds=(1,0)) # Solutions for time up to T_max

# Extract six sample points from the solutions:
T_series=range(0,18,3)
u_sol_list=[u_solution[:, int(i / Delta_t)] for i in T_series]

# Save zip file:
np.savez('Data\\kink.npz', u_sol=u_sol_list, x_series=x_series)