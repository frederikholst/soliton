# Here we perform 
from solver import *
from soliton_plot import *

# A tolerance is set:
tol=1e-2

## Defining constants: ##
Delta_x = 0.2                  # Spacial step size
X_max = 40                          # System length
x_size = int(X_max/Delta_x)         # Number of steps in position

Delta_t = 0.0005
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
u_analytic=np.array([soliton_solution(x,t_0) for x in x_series])
# Each subplot of A_series[i] vs. x_series:
for i, ax in enumerate(axes.flat):
    ax.plot(x_series, u_solution[:,int(1./Delta_t * (T_series[i]))],".")  # Plot each A_series element
    ax.plot(x_series, np.array([soliton_solution(x,T_series[i]) for x in x_series]))
    ax.set_title(f't = {t_0 + T_series[i]}')
    ax.set_xlabel('x [A.U.]')
    ax.set_ylabel('Amplitude [A.U.]')


# To prevent overlap
plt.tight_layout()
plt.savefig("Soliton_plot_try.png")
plt.show()


# Test 
#def test_add():
#    assert

