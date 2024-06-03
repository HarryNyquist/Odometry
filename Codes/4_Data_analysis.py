import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import data_functions as data 
from vpython import *

df = pd.read_csv("Filtered_Accn.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t_new, a_x_new, a_y_new, a_z_new= acc_data.T

A_x = np.fft.fft(a_x_new)
A_y = np.fft.fft(a_y_new)
A_z = np.fft.fft(a_z_new)

index_array = np.fft.fftfreq(len(A_x), t_new[1] - t_new[0])
squared = np.where(index_array == 0, 1, index_array ** 2)

X = A_x/squared * (-1)
Y = A_y/squared * (-1)
Z = A_z/squared * (-1)

x = np.fft.ifft(X)
y = np.fft.ifft(Y)
z = np.fft.ifft(Z)

N = len(x)

x = x*N*N
y = y*N*N
z = z*N*N


plt.plot(t_new, x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('x_vs_Time')
plt.clf()

plt.plot(t_new, y)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('y_vs_Time')
plt.clf()

plt.plot(t_new, x)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('z')
plt.savefig('z_vs_Time')
plt.clf()



phone = sphere(pos = vector(0,0,0), radius = 5, color = color.yellow, make_trail = True)
for i in range(len(t_new)):
    rate(500)
    phone.pos = vector(z[i],x[i],y[i])


#displacement_data = np.column_stack((t_new,x,y,z))
# np.savetxt("Displacement.txt",displacement_data, fmt = "%f", delimiter = " ")

# displacement_before_ifft_data = np.column_stack((t_new,trial1, trial2, trial3))
# np.savetxt("FFT_of_Displacement.txt", displacement_before_ifft_data, fmt = "%f", delimiter = " ")

# original_displacement_before_ifft = np.column_stack((t_new,X,Y,Z))
# np.savetxt("FFT_of_displacement-original.txt", original_displacement_before_ifft, fmt = "%f", delimiter = " ")


# freq_x = np.fft.fftfreq(len(X), data.SamplingTime(t))
# magnitude = np.abs(X)
# plt.plot(freq_x,magnitude)
# plt.savefig('Displacement_fft')

# mul = -1*(len(A_x)**2)/(4*np.pi*np.pi)


# x_trial = np.fft.ifft(A_x)
# y_trial = np.fft.ifft(A_y)
# z_trial = np.fft.ifft(A_z)


# X = X*mul
# Y = Y*mul
# Z = Z*mul

# freq_x = np.fft.fftfreq(len(A_x), data.SamplingTime(t))
# magnitude = np.abs(A_x)
# plt.plot(freq_x,magnitude)
# plt.savefig('Accn_fft')

# plt.plot(t_new, A_x)
# plt.grid(True)
# plt.xlabel('t')
# plt.ylabel('x')
# plt.savefig('axNew_vs_Time')
# plt.clf()

# t = np.insert(t,0,0) 
# a_x = np.insert(a_x,0,0)
# a_y = np.insert(a_y,0,0)
# a_z = np.insert(a_z,0,a_z[0])
# np.savetxt("Time_before_uniform_sampling.txt",t)
# #T_s = data.SamplingTime(t)
# #print(sampl_time)
# #print(data.avg_sampling_rate(t))

# if(data.is_uniformly_sampled(t)):
#     t_new = t 
#     a_x_new = a_x
#     a_y_new = a_y 
#     a_z_new = a_z
# else:
#     T_s = data.SamplingTime(t)
#     a_x_new = data.linear_interpolation(a_x,t,T_s)
#     a_y_new = data.linear_interpolation(a_y,t,T_s)
#     a_z_new = data.linear_interpolation(a_z,t,T_s)
#     t_new = data.uniform_samples(t, T_s)
#     idx , t_new = data.trim_time_array(t,t_new)
#     a_x_new = a_x_new[idx:]
#     a_y_new = a_y_new[idx:]
#     a_z_new = a_z_new[idx:]

# uniform_sampled_data = np.column_stack((t_new, a_x_new, a_y_new, a_z_new))
# np.savetxt("Uniformly_Sampled_Values.csv", uniform_sampled_data, fmt = "%f", delimiter = ",")

#print(data.is_uniformly_sampled(t))



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

# J_x = A_x * index_array * (0+1j)
# J_y = A_y * index_array * (0+1j)
# J_z = A_z * index_array * (0+1j)

# j_x = np.fft.ifft(J_x)
# j_y = np.fft.ifft(J_y)
# j_z = np.fft.ifft(J_z)

# Jerk_data = np.column_stack((t_new,j_x,j_y,j_z))
# np.savetxt("Jerk_data.csv", Jerk_data, fmt = "%f", delimiter = ",")

# J_deriv_x = J_x * index_array * (0+1j) 
# J_deriv_y = J_y * index_array * (0+1j)
# J_deriv_z = J_z * index_array * (0+1j)

# j_deriv_x = np.fft.ifft(J_deriv_x)
# j_deriv_y = np.fft.ifft(J_deriv_y)
# J_deriv_z = np.fft.ifft(J_deriv_z)

# Jerk_deriv_data = np.column_stack((t_new, j_x, j_y,j_z))
# np.savetxt("Jerk_derivative.csv", Jerk_deriv_data, fmt = "%f" , delimiter = ",")