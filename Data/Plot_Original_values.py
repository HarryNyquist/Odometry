import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("To_send.csv", header = None, skiprows = 1)
acc_data = df.to_numpy()
t,a_x,a_y,a_z,a_mag = acc_data.T 

df2 = pd.read_csv("Jerk_data.csv", header = None)
jerk_data = df2	.to_numpy()
t_new ,j_x, j_y, j_z = jerk_data.T 

t_new = np.real(t_new)
j_x = np.real(j_x)
j_y = np.real(j_y)
j_z = np.real(j_z)


plt.plot(t,a_x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_x')
plt.savefig("a_x vs t")

plt.clf ()

plt.plot(t,a_y)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("a_y vs t")

plt.clf()

plt.plot(t,a_z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_z')
plt.savefig("a_z vs t")
plt.clf()

plt.plot(t_new,j_x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('j_x')
plt.savefig("j_x vs t")

plt.clf ()

plt.plot(t_new,j_y)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('j_y')
plt.savefig("j_y vs t")

plt.clf()

plt.plot(t_new,j_z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('j_z')
plt.savefig("j_z vs t")
plt.clf()


