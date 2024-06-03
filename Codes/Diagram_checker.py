import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Filtered_Accn.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t_new, a_x_new, a_y_new, a_z_new= acc_data.T

N = len(a_x_new)

a_x_new = a_x_new 
a_y_new = a_y_new 
a_z_new = a_z_new 

plt.plot(t_new, a_x_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('Filtered_ax_vs_Time')
plt.clf()

plt.plot(t_new, a_y_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('Filtered_ay_vs_Time')
plt.clf()
