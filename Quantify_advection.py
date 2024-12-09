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
x_series = np.linspace(0, X_max, x_size)  # Positions

# Initialize solution array
u_gaus_init = np.zeros([x_size, t_size], dtype=float)
u_soliton_init=np.copy(u_gaus_init)
# define the gaus initial conditions
def init(x,mu=X_max/2,sig=1):
    return (
        1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.0) / 2)
    )

# Initialize start conditions:
u_gaus_init[:, 0] = np.array([init(x) for x in x_series]) 

# Define, for comparison, the soliton initial condition
x0= 20                                  # Initial time
u_soliton_init[:, 0] = np.array([soliton_solution(x, t=0,x0=x0) for x in x_series])  # Soliton at x0

# Solve the KdV equation
u_solution_sol = KdV_Solver(u_soliton_init, Delta_x, Delta_t, lin=True, mu=0) # Solutions for time up to T_max

u_solution_gaus = KdV_Solver(u_gaus_init, Delta_x, Delta_t, lin=True, mu=0)

eps=-6
T_series = np.linspace(0, 2.5,40)


residals_list=[]
residual_list_gauss=[]
for t in T_series:  # Skip the initial time step (t=0)
    numerical_sol = u_solution_sol[:, int(t / Delta_t)]
    analytical_sol= np.array([soliton_solution(x, t=0,x0=x0+t*eps) for x in x_series])
    numerical_gaus = u_solution_gaus[:, int(t / Delta_t)]
    analytical_gauss= np.array([init(x,X_max/2+t*eps) for x in x_series])
    residual_sol = np.sqrt(np.sum(((numerical_sol - analytical_sol)) ** 2))
    #residual_sol = np.sum(np.abs((numerical_sol - analytical_sol)))
    residals_list.append(residual_sol)
    residual_gauss = np.sqrt(np.sum(((numerical_gaus - analytical_gauss)) ** 2))
    residual_list_gauss.append(residual_gauss)
np.savez('Data\\Res_list',sol_list=residals_list, gauss_list=residual_list_gauss)
#np.savez('Data/Res_list',sol_list=residals_list, gauss_list=residual_list_gauss) # Linux