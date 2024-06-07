import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt
#import scipy.interpolate as sp


def simple_moving_average(signal, window_size):
    kernel = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(signal, kernel, mode = 'same')
    return smoothed_signal

def Brickwall_LPF(signal, cutoff_freq, fs, num_taps):
    normalized = cutoff_freq / (0.5*fs)
    t = np.arange(-num_taps//2, num_taps//2)
    LPF = np.sinc(2*normalized*t)
    LPF = LPF * np.hamming(num_taps)
    LPF = LPF/np.sum(LPF)
    filtered_signal = np.convolve(signal, LPF, mode = 'same')
    return filtered_signal

df = pd.read_csv("To_send.csv", header = None, skiprows = 1)
acc_data = df.to_numpy()
t, a_x, a_y, a_z, a_mag = acc_data.T 

kernel_size = 100
smoothed_using_SMA = simple_moving_average(a_y, kernel_size)
plt.plot(t,smoothed_using_SMA, color = 'blue')
plt.scatter(t,a_y, color = 'red',s = 1)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("Filtered_using_SMA")
plt.clf()

t_downsampled = t[::10]
# downsampled_SMA = smoothed_using_SMA[::10]
downsampled_a_y = a_y[::10]
plt.plot(t,smoothed_using_SMA, color = 'blue')
plt.scatter(t_downsampled,downsampled_a_y, color = 'black', s = 5)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("Filtered_using_SMA_downsampled")
plt.clf()

sampling_rate = 0.5 * len(t)/(t[-1] - t[0])
cutoff_freq = 5
taps = 101
LPF_output = Brickwall_LPF(a_y, cutoff_freq, sampling_rate, taps)

plt.plot(t,LPF_output, color = 'blue')
plt.scatter(t_downsampled,downsampled_a_y, color = 'black' , s = 1)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('a_y')
plt.savefig("Filtered_using_brickwall_LPF")
plt.clf()