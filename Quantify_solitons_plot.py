import matplotlib.pyplot as plt
import numpy as np

res_list=np.load("Data\\Res_list.npy")

fig,ax = plt.subplots(1,1,figsize=(6,6))
T_series = np.linspace(0, 18,40)

ax.plot(T_series, res_list,label="Residuals") 

# Axes title
ax.set_title("Quantifying solver performance at different times")

# Axes label
ax.set_xlabel('Time', fontsize = 15)
ax.set_ylabel('Sum of norm of Residuals', fontsize = 15)

# Ticks font size
ax.tick_params(axis='both', labelsize=15)  

# To prevent overlap
plt.tight_layout()
plt.savefig("Figures\\soliton_res.png")
plt.show()