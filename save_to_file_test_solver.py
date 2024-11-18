# Save_to_file -> testing KdV equation solver, creating a txt file
import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *
from solver import *

## Defining constants: ##
Delta_x = 0.2                       # Spacial step size
X_max = 40                          # System length
x_size = int(X_max/Delta_x)         # Number of steps in position

Delta_t = 0.001
T_max = 20
t_size = int(T_max/Delta_t)

# we create a grid with all zeros which will contain the solution
u = np.zeros([x_size, t_size], dtype = float)

# Initial condition
x_series=[n*Delta_x for n in range(x_size)]                      # Array of the positions 
t_0 = 10                                                         # Initial time
u[:,0]=np.array([soliton_solution(x,t_0) for x in x_series])     # With the imported function from soliton_plot.py we find the Soliton for t=0.
    
# Let's compute the solution!
u_solution = KdV_Solver(u, Delta_x, Delta_t)
    
# Writing the solution on a txt file
output_data = np.column_stack((x_series, u_solution))

#file_name = 'test_solver.txt'
#np.savetxt(file_name, output_data, delimiter=' ', fmt='%10.5f', header='position' + ' '.join([f't_{i*Delta_t:.3f}' for i in range(t_size)]))

filename = 'test_solver_data.npy'
np.save(filename, output_data)
    
    