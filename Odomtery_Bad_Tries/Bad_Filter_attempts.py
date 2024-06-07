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

smoothed_using_SMA = simple_moving_average(a_x, 10)
plt.plot(t,smoothed_using_SMA, color = 'blue')
plt.scatter(t,a_y, color = 'red')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_x')
plt.savefig("Filtered_using_SMA")
plt.clf()