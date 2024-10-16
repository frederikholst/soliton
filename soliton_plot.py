import numpy as np
import matplotlib.pyplot as plt

### The plot of u(x,t) for amplitude the soliton.

def sech(x):
    """ 
    Input: x, float64/float32 
    Output: sech(x), flaot64/float32
    """
    return 2*np.cosh(x)/(np.cosh(2*x)+1)

def soliton_solution(x,t,c=1,x0=0):
    """ 
    Input: 
    position x, float64/float32 
    time t, float64/float32
    optional:
    speed c, float64/float32
    start position x0, float64/float32
 
    Output: 
    u(x,t), flaot64/float32
    """
    return -c/2*sech(1/2*np.sqrt(c)*(x-c*t-x0))**2

x_series =np.arange(0,1,100)
t_series=np.arange(0,6)
A_series=[soliton_solution(x_series,t) for t in t_series]


fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Each subplot of A_series[i] vs. x_series:
for i, ax in enumerate(axes.flat):
    ax.plot(x_series, A_series[i],".")  # Plot each A_series element
    ax.set_title(f'Soliton Solution at t={t_series[i]}')
    ax.set_xlabel('x')
    ax.set_ylabel('Amplitude')

# To prevent overlap
plt.tight_layout()

plt.show()