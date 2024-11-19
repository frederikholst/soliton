import numpy as np
import matplotlib.pyplot as plt
from soliton_plot import *

# Plot of a soliton (analytic solution)
x_series =np.arange(0,40,0.1)
t_series=np.arange(10,28,3)
A_series=[soliton_solution(x_series,t) for t in t_series]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for i, ax in enumerate(axes.flat):
        ax.plot(x_series, A_series[i])
        # Axes title
        ax.set_title(f't = {t_series[i]}', fontsize=15)

        # Axes label
        if i == 3 or i == 4 or i == 5:
            ax.set_xlabel('x [A.U.]', fontsize = 15)
        if i == 0 or i == 3:
            ax.set_ylabel('Amplitude [A.U.]', fontsize = 15)
        
        # Ticks font size
        ax.tick_params(axis='both', labelsize=15)  


plt.tight_layout()
plt.savefig("Figures\\Soliton_plot.png")
