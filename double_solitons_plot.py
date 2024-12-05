# Plotter

import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

# Load the .npz file
data = np.load('Data\\double_solitons.npz')

# Access individual arrays
u_solution = data['u_sol']
param = data['parameters']
#print(u_solution)

'''
# Plotting 
fig,axes = plt.subplots(2,3,figsize=(12,8))

for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution[i],".",label="Numerical solutions")
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
        '''

plt.imshow(u_solution, extent=[0, param[1], 0, param[0]], aspect='auto',origin='lower')
plt.ylabel('x [A.U.]', fontsize = 15)
plt.xlabel('t [A.U.]', fontsize = 15)

'''
fig, ax = plt.subplots()
c = ax.pcolor(u_solution)
ax.set_xlabel('x [A.U.]', fontsize = 15)
ax.set_ylabel('t [A.U.]', fontsize = 15)
cbar=plt.colorbar(c, ax)
cbar.set_label('amplitude [A.U.]',rotation=270)
'''

# To prevent overlap
#plt.tight_layout()
plt.savefig("Figures//double_solitons3.png")
plt.show()