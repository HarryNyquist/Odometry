import numpy as np 
#from scipy.integrate import cumtrapz
import pandas as pd
import data_functions as data 
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3D import Axes3D
from matplotlib.animation import FuncAnimation
#import vpython
from scipy.integrate import cumtrapz

df = pd.read_csv("May_28_15-30.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
t, a_x, a_y, a_z, a_mag = acc_data.T
t = np.insert(t,0,0) 
a_x = np.insert(a_x,0,0)
a_y = np.insert(a_y,0,0)
a_z = np.insert(a_z,0,a_z[0])

if(data.is_uniformly_sampled(t)):
    t_new = t 
    a_x_new = a_x
    a_y_new = a_y 
    a_z_new = a_z
else:
    T_s = data.SamplingTime(t)
    a_x_new = data.linear_interpolation(a_x,t,T_s)
    print(len(a_x_new))
    a_y_new = data.linear_interpolation(a_y,t,T_s)
    a_z_new = data.linear_interpolation(a_z,t,T_s)
    t_new = data.uniform_samples(t, T_s)
    idx , t_new = data.trim_time_array(t,t_new)
    a_x_new = a_x_new[idx:]
    a_y_new = a_y_new[idx:]
    a_z_new = a_z_new[idx:]



v_x_new = data.trapezoidal_rule(a_x_new,t_new)
print(len(v_x_new))
x = data.trapezoidal_rule(v_x_new,t_new)


v_y_new = data.trapezoidal_rule(a_y_new,t_new)
y = data.trapezoidal_rule(v_y_new,t_new)

v_z_new = data.trapezoidal_rule(a_z_new,t_new)
z = data.trapezoidal_rule(v_z_new,t_new)

plt.plot(t_new, a_x_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('axNew_vs_Time')
plt.clf()

plt.plot(t_new, a_y_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('ayNew_vs_Time')
plt.clf()

plt.plot(t_new, a_z_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('z')
plt.savefig('azNew_vs_Time')
plt.clf()

plt.plot(t_new, v_x_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('vxNew_vs_Time')
plt.clf()

plt.plot(t_new, v_y_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('vyNew_vs_Time')
plt.clf()

plt.plot(t_new, v_z_new)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('z')
plt.savefig('vzNew_vs_Time')
plt.clf()

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

plt.plot(t_new, z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('z')
plt.savefig('z_vs_Time')
plt.clf()

# fig = plt.figure()
# ax = fig.add_subplot(111,projection = '3d')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title("Trajectory, enjoy!")

# trajectory, = ax.plot([],[],[],'r-')
# point, = ax.plot([],[],[],'bo')

# def update(frame):
#     trajectory.set_data(x[:frame], y[:frame])
#     trajectory.set_3d_properties(z[:frame])
#     point.set_data(x[frame], y[frame])
#     point.set_3d_properties(z[frame])
#     return trajectory, point

# ani = FuncAnimation(fig, update, frames = len(t), interval = 100, blit = True)
# ani.save("Trajectory.mp4",writer = 'ffmpeg',fps = 30)