import matplotlib.pyplot as plt
import numpy as np

#data=np.load("Data\\Res_list.npz")
data=np.load("Data/Res_list.npz") # Linux

res_sol=data['sol_list']
res_gaus=data['gauss_list']


fig,ax = plt.subplots(1,2,figsize=(12,6))
T_series = np.linspace(0,2.5,40)

ax[0].plot(T_series, res_sol ,label="Residuals soliton") 
ax[1].plot(T_series, res_gaus ,label="Residuals soliton") 

# Axes title
ax[0].set_title("Quantifying soliton advection")
ax[1].set_title("Quantifying gauss advection")

# Axes label
ax[0].set_xlabel('Time', fontsize = 15)
ax[0].set_ylabel('Sum of Norm of Residuals', fontsize = 15)
ax[1].set_xlabel('Time', fontsize = 15)
ax[1].set_ylabel('Sum of Norm of Residuals', fontsize = 15)

# Ticks font size
ax[0].tick_params(axis='both', labelsize=15)  
ax[1].tick_params(axis='both', labelsize=15)  

# To prevent overlap
plt.tight_layout()
plt.savefig("Figures\\advection_res.png")
#plt.savefig("Figures/advection_res.png") # Linux
plt.clf()