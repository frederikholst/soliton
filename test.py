from solver import KdV_Solver
from soliton_plot import *
import numpy as np


## UNIT TESTS:
def test_sech_symmetry():
    x_values = np.array([-1.0, 0.0, 1.0, 2.0], dtype=np.float64)
    for x in x_values:
        assert np.isclose(sech(x), sech(-x), atol=1e-6), f"sech({x}) != sech({-x})"


def test_no_change_with_zero_coefficients():
    # Initialize a simple wave
    x_size, t_size = 10, 5
    u = np.random.rand(x_size, t_size)  # Random initial condition
    
    # Solve with zero coefficients
    result = KdV_Solver(u.copy(), mu=0, eps=0)

    # The result should match the initial condition
    np.testing.assert_array_almost_equal(
        result[:, 0], u[:, 0], 
        decimal=6,
        err_msg="Wave should remain unchanged when mu=0 and eps=0"
        )


### FUNCTIONAL TEST ###


# Test function
def test_squared_residuals():
    # Set tolerance for testing
    

    # Define constants
    Delta_x = 0.2                  # Spatial step size
    X_max = 40                     # System length
    x_size = int(X_max / Delta_x)  # Number of spatial steps

    Delta_t = 0.001                # Time step size
    T_max = 20                     # Maximum time
    t_size = int(T_max / Delta_t)  # Number of time steps
    tol = 0.001*x_size
    # Initialize the solution array
    u = np.zeros([x_size, t_size], dtype=float)

    # Initial condition
    x_series = np.linspace(0, X_max, x_size)  # Array of positions
    t_0 = 10                                 # Initial time
    u[:, 0] = np.array([soliton_solution(x, t_0) for x in x_series])  # Soliton at t=0

    # Compute the numerical solution
    u_solution = KdV_Solver(u, Delta_x, Delta_t)

    # Define time series for plotting and testing
    T_series = range(0, 6,1)

    for t in T_series[1:]:  # Skip the initial time step (t=0)
        numerical = u_solution[:, int(t / Delta_t)]
        analytical = np.array([soliton_solution(x, t + t_0) for x in x_series])
        residual = np.sum(np.sqrt((numerical - analytical) ** 2))
        assert residual < tol, f"Residual {residual} exceeds tolerance at t = {t + t_0}"
