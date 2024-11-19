from solver import KdV_Solver
from soliton_plot import soliton_solution
import numpy as np
import matplotlib.pyplot as plt


# Define constants
Delta_x = 0.8                  # Spatial step size
X_max = 40                     # System length
x_size = int(X_max / Delta_x)  # Number of spatial steps

Delta_t = 0.001                # Time step size
T_max = 20                     # Maximum time
t_size = int(T_max / Delta_t)  # Number of time steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

# Initialize start condition
x_series = np.linspace(0, X_max, x_size)  # Positions
x0 = 10                                  # Initial space
u[:, 0] = np.array([soliton_solution(x,t=0, x0=x0) for x in x_series])  # Soliton at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t) # Solutions for time up to T_max

# Extract six sample points from the solutions:
T_series=range(0,18,3)
u_sol_list=[u_solution[:, int(i / Delta_t)] for i in T_series]
u_ana_list=[np.array([soliton_solution(x,t=i,x0=x0) for x in x_series]) for i in T_series]


## PART 2: We now double the grid size by a factor of 2 and 4 respectively to check for convergence. 

## FACTOR 2: ##
# Define constants
Delta_x = Delta_x/2            # Spatial step size
x_size = int(X_max / Delta_x)  # Number of spatial steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

x_series2 = np.linspace(0, X_max, x_size)  # Positions

u[:, 0] = np.array([soliton_solution(x, t=0,x0=x0) for x in x_series2])  # Soliton at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t) # Solutions for time up to T_max

# Extract one sample with:
u_sol_2=u_solution[:, int(T_series[3] / Delta_t)]
u_ana_2=np.array([soliton_solution(x, T_series[3],x0=x0) for x in x_series2])

## FACTOR 4: ##
# Define constants
Delta_x = Delta_x/2            # Spatial step size
x_size = int(X_max / Delta_x)  # Number of spatial steps

# Initialize solution array
u = np.zeros([x_size, t_size], dtype=float)

x_series4 = np.linspace(0, X_max, x_size)  # Positions

u[:, 0] = np.array([soliton_solution(x, t=0,x0=x0) for x in x_series4])  # Soliton at t0

# Solve the KdV equation
u_solution = KdV_Solver(u, Delta_x, Delta_t) # Solutions for time up to T_max

# Extract one sample at t=19:
u_sol_4=u_solution[:, int(T_series[3] / Delta_t)]
u_ana_4=np.array([soliton_solution(x, T_series[3],x0=x0) for x in x_series4])


# Save zip file:
np.savez('Data\\solitons_comparison.npz',
         u_sol=u_sol_list, 
         u_ana=u_ana_list, 

         u2=u_sol_2,
         a2=u_ana_2,

         u4=u_sol_4,
         a4=u_ana_4,

         x_series=x_series,
         x_series2=x_series2,
         x_series4=x_series4
         )