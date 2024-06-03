import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("To_send.csv", header = None, skiprows = 1)
acc_data = df.to_numpy()
t,a_x,a_y,a_z,a_mag = acc_data.T 

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

