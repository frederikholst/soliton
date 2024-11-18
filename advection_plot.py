# Plotter

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

# Load the .npz file
data = np.load('Data\\advection.npz')

# Access individual arrays
u_solution_sol = data['u_sol']
u_solution_kink= data['u_kink']
x_series = data['x_series']
T_series=data['T']
# Plotting 
fig,axes = plt.subplots(2,3,figsize=(12,8))


for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution_kink[i],".",label="Kink")
        ax.plot(x_series, u_solution_sol[i],".",label="Soliton")
        # Axes title
        ax.set_title(f't = {round(T_series[i],2)}', fontsize=15)
        
        # Axes label
        if i == 3 or i == 4 or i == 5:
            ax.set_xlabel('x [A.U.]', fontsize = 15)
        if i==2:
            ax.legend()
        if i == 0 or i == 3:
            ax.set_ylabel('Amplitude [A.U.]', fontsize = 15)
        
        # Ticks font size
        ax.tick_params(axis='both', labelsize=15)  

# To prevent overlap
plt.tight_layout()
plt.savefig("Figures//advection.png")
plt.show()