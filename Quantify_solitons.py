from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np

# Set tolerance for testing
tol = 1e-3

# Define constants
Delta_x = 0.2                  # Spatial step size
X_max = 40                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.001                # Time step size
T_max = 20                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize the solution array
u = np.zeros([x_size, t_size], dtype=float)

# Initial condition
x_series = np.linspace(0, X_max, x_size)  # Array of positions
t_0 = 10                                 # Initial time
u[:, 0] = np.array([soliton_solution(x, t_0) for x in x_series])  # Soliton at t=0

# Compute the numerical solution
u_solution = KdV_Solver(u, Delta_x, Delta_t)

# Define time series for plotting and testing
T_series = np.linspace(0, 18,40)


residals_list=[]
for t in T_series:  # Skip the initial time step (t=0)
    numerical = u_solution[:, int(t / Delta_t)]
    analytical = np.array([soliton_solution(x, t + t_0) for x in x_series])
    residual = np.sum(np.sqrt((numerical - analytical) ** 2))
    residals_list.append(residual)

np.save("Data\\Res_list",residals_list)