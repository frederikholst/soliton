# Plotter

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

# Load the .npz file
data = np.load('Data\\solitons_comparison.npz')

# Access individual arrays
u_solution = data['u_sol']
u_ana_list = data['u_ana']
x_series = data['x_series']

# Plotting 
fig,axes = plt.subplots(2,3,figsize=(12,8))


for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution[i],".",label="Numerical solutions")
        ax.plot(x_series,u_ana_list[i],label="Analytic solutions")
        # Axes title
        ax.set_title(f't = {10 + i*3}', fontsize=15)
        
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
plt.savefig("Figures//solitons_comparison.png")
plt.show()