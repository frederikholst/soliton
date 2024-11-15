### In this script we will implement the finite difference method to solve the Korteveg DeVries equation. 

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

def KdV_Solver(u,T,Delta_x,Delta_t=0.005,mu=1,eps=-6):
    """
    Computes the solution to the KdV equation using finite difference method.

    :param u: A soliton (or other wavefunction) at a time t=0.
    :type u: np.array, shape (N,)

    :param T: Maximum time that should be solved for.
    :type T: float

    :param Delta_x: Position step size.
    :type Delta_x: float

    :param Delta_t: Time step size.
    :type Delta_t: float

    :param mu: Dispersion coefficient.
    :type mu: float (optional)

    :param eps: Nonlinearity coefficient, epsilon.
    :type eps: float (optional)

    :param N_step_x: Number of spatial steps.
    :type N_step_x: int

    :return: The solution at time T.
    :rtype: np.array, shape (N,)
    """
    N_step_x = len(u)
    t=0
    u_prev=np.copy(u)
    
    
    while t<T:
        u_new=np.copy(u)
        for i in range(3,N_step_x-3):
            
            du_dx = (u[i+1] - u[i-1]) / (2 * Delta_x)
            du3_dx3 = (u[i+3] - 3 * u[i+1] + 3 * u[i-1] - u[i-3]) / (2**3 * Delta_x**3)
            if t>0:
                # Central difference in time for subsequent steps after the first two
                u_new[i] = u_prev[i] - 2*Delta_t * (du_dx + eps * u[i] * du_dx + mu * du3_dx3)
            else:
                # Forward difference in time from the first (t=0) to the second (t=dt) step:
                u_new[i] = u[i] - Delta_t * (du_dx + eps * u[i] * du_dx + mu * du3_dx3)
            
        # To fix the derivative to be zero at the boundary:
        u_new[0]=u_new[1] 
        u_new[-1]=u_new[-2]

        # Updating the previous and current position step:
        u_prev=np.copy(u)
        u=u_new
            
        # Updating the time:            
        t+=Delta_t
    return u # The solution to KdV as a wave function at time T (np.array, shape: (N,))
        
## Let's test the solver:
if __name__ == "__main__":

    ## Defining constants: ##
    Delta_x=0.5 # Spacial step size
    X_max=40 # System length

    N_step_x=int(X_max/Delta_x) # Number of steps in position

    x_series=[n*Delta_x for n in range(N_step_x)] # A 1xN array of the positions 
    # With the imported function from soliton_plot.py we find the Soliton for t=0.
    u=np.array([soliton_solution(x,10) for x in x_series]) 

    # Let's compute the solutions!
    T_series=range(0,18,3)
    u_list=[KdV_Solver(u,T_max,Delta_x) for T_max in T_series]

    fig,axes=plt.subplots(2,3,figsize=(12,8))

    # Each subplot of A_series[i] vs. x_series:
    for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_list[i],".")  # Plot each A_series element
        ax.set_title(f'Numerical solution at time = {T_series[i]}')
        ax.set_xlabel('x [A.U.]')
        ax.set_ylabel('Amplitude [A.U.]')


    # To prevent overlap
    plt.tight_layout()
    plt.savefig("Soliton_plot_solver.png")
    plt.show()
