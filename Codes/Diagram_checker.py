import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Filtered_Accn.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t_new, a_x_new, a_y_new, a_z_new= acc_data.T

# N = len(a_x_new)

# a_x_new = a_x_new 
# a_y_new = a_y_new 
# a_z_new = a_z_new 

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

plt.plot(t_new, a_z_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('Filtered_az_vs_Time')
plt.clf()

df2 = pd.read_csv("Three_June_20-32.csv", header = None, skiprows = 1)
acc = df2.to_numpy()

t, a_x, a_y, a_z, a_mag = acc.T 

plt.plot(t, a_x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('ax_vs_Time')
plt.clf()

plt.plot(t, a_y)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('ay_vs_Time')
plt.clf()

plt.plot(t, a_z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('az_vs_Time')
plt.clf()