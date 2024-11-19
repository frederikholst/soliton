# Plotter

import numpy as np
import matplotlib.pyplot as plt


# Loading data to plot

filename = 'test_solver_data.npy'
data = np.load(filename)

x_series = data[:, 0]
u_solution = data[:, 1:]

# Paramateres needed for plotting
Delta_t = 0.001                     # Time step
t_0 = 10                            # Initial time
T_series=range(0,18,3)              # t values to plot 

# Plotting 
fig,axes = plt.subplots(2,3,figsize=(12,8))


for i, ax in enumerate(axes.flat):
        ax.plot(x_series, u_solution[:, int(1./Delta_t * (T_series[i]))],".") 

        # Axes title
        ax.set_title(f't = {t_0 + T_series[i]}', fontsize=15)
        
        # Axes label
        if i == 3 or i == 4 or i == 5:
            ax.set_xlabel('x [A.U.]', fontsize = 15)
        if i == 0 or i == 3:
            ax.set_ylabel('Amplitude [A.U.]', fontsize = 15)
        
        # Ticks font size
        ax.tick_params(axis='both', labelsize=15)  

# To prevent overlap
plt.tight_layout()
plt.savefig("Figures\\test_solver.png")
plt.show()