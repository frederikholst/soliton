import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *
from finite_difference import *

## Defining constants: ##
Delta_x = 0.1 # Spacial step size
X_max=30 # System length

N_step_x=int(X_max/Delta_x) # Number of steps in position

x_series=[n*Delta_x for n in range(N_step_x)] # A 1xN array of the positions 
# With the imported function from soliton_plot.py we find the Soliton for t=15.
start_T=10
u=np.array([soliton_solution(x,start_T) for x in x_series]) 

# Let's compute the solutions!
T_series=np.linspace(0,9,6)
u_list=[KdV_Solver(u,T_max,Delta_x,Delta_t=0.001) for T_max in T_series]

fig,axes=plt.subplots(2,3,figsize=(12,8))
plt.rcParams['font.size'] = 12

# Each subplot of A_series[i] vs. x_series:
for i, ax in enumerate(axes.flat):
    ax.plot(x_series, u_list[i],".")  # Plot each A_series element
    ax.set_title(f'Numerical solution at time = {T_series[i]+start_T}')
    ax.set_xlabel('x [A.U.]')
    ax.set_ylabel('Amplitude [A.U.]')

# To prevent overlap
plt.tight_layout()
plt.savefig("Soliton_plot_solver.png")
plt.show()