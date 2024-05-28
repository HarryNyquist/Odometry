import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import data_functions as data 

df = pd.read_csv("May_26_09-16.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t, a_x, a_y, a_z, a_mag = acc_data.T
t = np.insert(t,0,0) 
a_x = np.insert(a_x,0,0)
a_y = np.insert(a_y,0,0)
a_z = np.insert(a_z,0,a_z[0])
np.savetxt("Time_before_uniform_sampling.txt",t)
#T_s = data.SamplingTime(t)
#print(sampl_time)
#print(data.avg_sampling_rate(t))

if(data.is_uniformly_sampled(t)):
    t_new = t 
    a_x_new = a_x
    a_y_new = a_y 
    a_z_new = a_z
else:
    T_s = data.SamplingTime(t)
    a_x_new = data.linear_interpolation(a_x,t,T_s)
    a_y_new = data.linear_interpolation(a_y,t,T_s)
    a_z_new = data.linear_interpolation(a_z,t,T_s)
    t_new = data.uniform_samples(t, T_s)
    idx , t_new = data.trim_time_array(t,t_new)
    a_x_new = a_x_new[idx:]
    a_y_new = a_y_new[idx:]
    a_z_new = a_z_new[idx:]

# uniform_sampled_data = np.column_stack((t_new, a_x_new, a_y_new, a_z_new))
# np.savetxt("Uniformly_Sampled_Values.txt", uniform_sampled_data, fmt = "%f", delimiter = " ")

#print(data.is_uniformly_sampled(t))

A_x = np.fft.fft(a_x_new)
A_y = np.fft.fft(a_y_new)
A_z = np.fft.fft(a_z_new)

index_array = np.arange(len(A_x))
squared = np.where(index_array == 0, 1, index_array ** 2)

X = A_x/squared
Y = A_y/squared
Z = A_z/squared

mul = -1*(len(A_x)**2)/(4*np.pi*np.pi)

# x_trial = np.fft.ifft(A_x)
# y_trial = np.fft.ifft(A_y)
# z_trial = np.fft.ifft(A_z)


# X = X*mul
# Y = Y*mul
# Z = Z*mul

x = np.fft.ifft(X)
y = np.fft.ifft(Y)
z = np.fft.ifft(Z)

displacement_data = np.column_stack((t_new,x,y,z))
np.savetxt("Displacement.txt",displacement_data, fmt = "%f", delimiter = " ")




















# fft_data = np.column_stack((t_new, A_x, A_y, A_z))
# np.savetxt("FFT_values.txt", fft_data, fmt = "%f", delimiter = " ")


#print(np.sum(a_x_new))


# print(len(a_x_new))
# print(len(A_y))
# print(len(A_z))
# print(len(t_new))

# print(A_x[0])
# print(A_y[0])
# print(A_z[0])

# N = len(A_x)
# mul = (N**2)/(4* np.pi * np.pi)

# A_x = A_x * mul
# A_y = A_y * mul
# A_z = A_z * mul 



# A_x = A_x[1:]
# A_y = A_y[1:]
# A_z = A_z[1:]

# mul_array = np.arange(1,N) ** 2

# X = A_x / mul_array 
# Y = A_y / mul_array 
# Z = A_z / mul_array 
