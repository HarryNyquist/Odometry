import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import data_functions as data 

df = pd.read_csv("May_26_09-16.csv",header = None,skiprows = 1)
acc_data = df.to_numpy()
#print(acc_data)
t, a_x, a_y, a_z, a_mag = acc_data.T
np.savetxt("Time.txt",t)
sampl_time = data.SamplingTime(t)
#print(sampl_time)

