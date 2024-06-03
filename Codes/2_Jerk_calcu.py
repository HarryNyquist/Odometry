import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("New_Accn_Data.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t_new, a_x_new, a_y_new, a_z_new= acc_data.T
A_x = np.fft.fft(a_x_new)
A_y = np.fft.fft(a_y_new)
A_z = np.fft.fft(a_z_new)

index_array = np.fft.fftfreq(len(A_x), t_new[1] - t_new[0])
J_x = A_x * index_array * (0+1j)
J_y = A_y * index_array * (0+1j)
J_z = A_z * index_array * (0+1j)

j_x = np.real(np.fft.ifft(J_x))
j_y = np.real(np.fft.ifft(J_y))
j_z = np.real(np.fft.ifft(J_z))


df2 = pd.DataFrame({"t":t_new, "j_x":j_x, "j_y":j_y,"j_z":j_z})
df2.to_csv("Jerk_data.csv", index = False)

plt.plot(t_new, a_x_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_x')
plt.savefig('ax_vs_Time')
plt.clf()

plt.plot(t_new,a_y_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig('ay_vs_Time')
plt.clf()