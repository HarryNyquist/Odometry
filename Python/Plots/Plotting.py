import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("Differentiated_output.csv", header = None, skiprows = 1)
jerk_data = df.to_numpy()
t, jerk_x, jerk_y, jerk_z = jerk_data.T 

df2 = pd.read_csv("New_Accn_Data.csv")
acc_data = df.to_numpy()
t_new, a_x, a_y, a_z = acc_data.T 

df3 = pd.read_csv("jerk_Differentiation.csv")
acc_data = df.to_numpy()
t_news, jerkx, jerky, jerkz = acc_data.T 

plt.plot(t,a_x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_z')
plt.savefig('Acc_z')
plt.clf()


plt.plot(t,jerk_z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('jerk_z')
plt.savefig('Jerk_z')
plt.clf()

plt.plot(t,jerkz)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('jerk_z')
plt.savefig('Jerk_diff_z')
plt.clf()
