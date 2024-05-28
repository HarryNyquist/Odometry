import numpy as np

def SamplingTime(arr):
    T_min = arr[1] - arr[0]
    for i in range(1, len(arr)):
        T_min = min(T_min, arr[i]-arr[i-1])
    return (T_min/2)   #we want to take some sampling time according to Nyquist law, so T_min >= 2T_sampling

def Discrete_Fourier_Transform(x):
    N = len(x)
    X = np.zeros(N) + 1j*np.zeros(N)
    for k in range(0,N):
        for n in range(0,N):
            X[k] += x[n]*np.exp(-1j*2*np.pi*n*k/N)
    return x

def Inverse_Discrete_Fourier_Transform(X):
    X_len = len(X)
    x = np.zeros(X_len) + 1j*np.zeros(X_len)
    for n in range(0,X_len):
        for k in range(0,X_len):
            x[n]+= (1/X_len)*(X[k])*np.exp(1j*2*np.pi*n*k/N)
    return X

def avg_sampling_rate(arr):
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i] - arr[i-1]
    return sum/len(arr)


def is_uniformly_sampled(arr):
    t_s_ideal = arr[1] - arr[0]
    for i in range(1,len(arr)):
        if abs(arr[i] - arr[i-1]) != t_s_ideal:
            return False
    return True

# def cubic_interpolation(signal, time, new_time,sampl_time):
#     def find_nearest(array, value):
#         array = np.asarray(array)
#         idx = (np.abs(array - value)).argmin()
#         return idx

#     new_signal = np.zeros_like(new_time)
#     for i, x_val in enumerate(new_time):
#         idx = find_nearest(x, x_val)
#         if idx == 0:
#             idx = 1
#         elif idx == len(x) - 1:
#             idx = len(x) - 2

#         x0, x1, x2, x3 = x[idx - 1], x[idx], x[idx + 1], x[idx + 2]
#         y0, y1, y2, y3 = y[idx - 1], y[idx], y[idx + 1], y[idx + 2]

#         t = (sampl_time) / (x2 - x1) # the interpolation 
#         a0 = y1
#         a1 = 0.5 * (y2 - y0)
#         a2 = 0.5 * (2 * y0 - 5 * y1 + 4 * y2 - y3)
#         a3 = 0.5 * (y3 - 3 * y0 + 3 * y1 - y2)

#         new_y[i] = a0 + a1 * t + a2 * t ** 2 + a3 * t ** 3

#     return new_y

def nearest_index(arr,value):
    nearest_idx = -1
    for i in range(len(arr)):
        if arr[i] > value:
            break
        nearest_idx = i
    return nearest_idx
  
def uniform_samples(time,sampling_time):
    no_of_samples = int((max(time) - min(time))//sampling_time)
    new_time = np.zeros(no_of_samples)
    for n in range(1,no_of_samples):
        new_time[n] = n*sampling_time
    return new_time

def linear_interpolation(signal, time, sampling_time):
     no_of_samples = int((max(time) - min(time))//sampling_time)
     #print(no_of_samples)
     new_signal = np.zeros(no_of_samples)
     for n in range(1,no_of_samples):
         idx = nearest_index(time, n*sampling_time)
         new_signal[n] = signal[idx] + (signal[idx + 1] - signal[idx])*(n*sampling_time - time[idx])/(time[idx+1] - time[idx])
     return new_signal

def trim_time_array(original_array, new_array):
    idx = nearest_index(new_array,original_array[1]) + 1 #idx = 1 cuz original_array[0] = 0 which we had padded. 
    #new_array[:idx]
    return (idx, new_array[idx:])


    



         

  