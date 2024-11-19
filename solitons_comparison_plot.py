# Plotter

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

# Load the .npz file
data = np.load('Data\\solitons_comparison.npz')

# Access individual arrays
u_solution = data['u_sol']
u_ana_list = data['u_ana']

u_sol_2 = data['u2']
u_ana_2 = data['a2']

u_sol_4 = data['u4']
u_ana_4 = data['a4']

x_series = data['x_series']
x_series2 = data['x_series2']
x_series4 = data['x_series4']

# Plot 1: Comparison at different time steps
fig,axes = plt.subplots(2,3,figsize=(12,8))


for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution[i],".",label="Numerical solutions")
        ax.plot(x_series,u_ana_list[i],label="Analytic solutions")
        # Axes title
        ax.set_title(f't = {i*3}', fontsize=15)
        
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
#plt.show()
plt.clf()


# Plot 2: Convergence at different grid size 
fig,axes = plt.subplots(1,3,figsize=(12,4))

u_conv_sol_list=[u_solution[3],u_sol_2,u_sol_4]
u_conv_ana_list=[u_ana_list[3],u_ana_2,u_ana_4]

x_series_list=[x_series,x_series2,x_series4]
DeltaX_list=[0.8,0.4,0.2]
for i, ax in enumerate(axes.flat):
        ax.plot(x_series_list[i],u_conv_sol_list[i],".",label="Numerical solutions")
        ax.plot(x_series_list[i],u_conv_ana_list[i],label="Analytic solutions")
        # Axes title
        ax.set_title(f'Step size = {DeltaX_list[i]}', fontsize=15)
        
        # Axes label
        ax.set_xlabel('x [A.U.]', fontsize = 15)
        if i==2:
            ax.legend()
        ax.set_ylabel('Amplitude [A.U.]', fontsize = 15)
        
        # Ticks font size
        ax.tick_params(axis='both', labelsize=15)  

        ax.set_ylim(-0.2,0.05)

# To prevent overlap
plt.tight_layout()
plt.savefig("Figures//solitons_convergence.png")
plt.show()
plt.clf()