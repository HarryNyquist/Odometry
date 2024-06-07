import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt


def simple_moving_average(signal, window_size):
    kernel = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(signal, kernel, mode = 'same')
    return smoothed_signal

df = pd.read_csv("To_send.csv", header = None, skiprows = 1)
acc_data = df.to_numpy()
t, a_x, a_y, a_z, a_mag = acc_data.T 

kernel_size = 100
smoothed_using_SMA = simple_moving_average(a_y, kernel_size)
plt.plot(t,smoothed_using_SMA, color = 'blue')
plt.scatter(t,a_y, color = 'red')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("Filtered_using_SMA")
plt.clf()

t_downsampled = t[::10]
downsampled_SMA = smoothed_using_SMA[::10]
downsampled_a_y = a_y[::10]
plt.plot(t_downsampled,downsampled_SMA, color = 'blue')
plt.scatter(t_downsampled,downsampled_a_y, color = 'black')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("Filtered_using_SMA_downsampled")
plt.clf()