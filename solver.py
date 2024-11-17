### In this script we will implement the finite difference method to solve the Korteveg DeVries equation. 

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

def KdV_Solver(u, Delta_x = 0.2, Delta_t=0.001, bounds = (0,0), mu=1, eps=-6):
    """
    Computes the solution to the KdV equation using finite difference method.

    :param u: A soliton (or other wavefunction) at a time t=0.
    :type u: np.array, shape (x_size, t_size)

    :param Delta_x: Position step size.
    :type Delta_x: float

    :param Delta_t: Time step size.
    :type Delta_t: float

    :param mu: Dispersion coefficient.
    :type mu: float (optional)

    :param eps: Nonlinearity coefficient, epsilon.
    :type eps: float (optional)

    :return: The solution 
    :rtype: np.array, shape (x_size, t_size)
    """
   
    t_size = len(u[0,:])
    x_size = len(u[:,0])

    
    for j in range(t_size-1):
        for i in range(2, x_size -2):

            if j == 0:
                u[i,j+1] = u[i, j] - Delta_t/(2*Delta_x) * eps * u[i,j] * (u[i+1,j] - u[i-1,j]) - Delta_t/(2*Delta_x**3) * mu *(u[i+2,j] - 2*u[i+1,j] +2*u[i-1,j]-u[i-2,j] )
            
            else:
                u[i,j+1] = u[i, j-1] - Delta_t/Delta_x * eps * u[i,j] * (u[i+1,j] - u[i-1,j]) - Delta_t/Delta_x**3 * mu *(u[i+2,j] - 2*u[i+1,j] +2*u[i-1,j]-u[i-2,j] )

        # We assume fixed values for
        u[0,j+1] = bounds[0]
        u[-1,j+1] = bounds[1]

        # We fix the derivative to be zero at the boundary:
        u[1,j+1] = u[0,j+1] 
        u[-2,j+1] = u[-1,j+1]
    
    return u
 

 

        
## Let's test the solver:
if __name__ == "__main__":

    ## Defining constants: ##
    Delta_x = 1                       # Spacial step size
    X_max = 40                          # System length
    x_size = int(X_max/Delta_x)         # Number of steps in position

    Delta_t = 0.001
    T_max = 20
    t_size = int(T_max/Delta_t)

    u = np.zeros([x_size, t_size], dtype = float)

    # Initial condition
    x_series=[n*Delta_x for n in range(x_size)]                      # A 1xN array of the positions 
    t_0 = 10                                                         # initial time
    u[:,0]=np.array([soliton_solution(x,t_0) for x in x_series])    # With the imported function from soliton_plot.py we find the Soliton for t=0.
    
    # Let's compute the solution!
    u_solution = KdV_Solver(u, Delta_x, Delta_t)

    # Plotting results
    fig,axes=plt.subplots(2,3,figsize=(12,8))
    T_series=range(0,18,3)

    
    # Each subplot of A_series[i] vs. x_series:
    for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution[:,int(1./Delta_t * (T_series[i]))],".")  # Plot each A_series element
        ax.set_title(f't = {t_0 + T_series[i]}')
        ax.set_xlabel('x [A.U.]')
        ax.set_ylabel('Amplitude [A.U.]')
    
    
    # To prevent overlap
    plt.tight_layout()
    plt.savefig("Soliton_plot_try.png")
    plt.show()