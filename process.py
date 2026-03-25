import csv
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
x_data=df['x']
y_data=df['y']
z_data=df['z']

r=np.sqrt(x_data**2+y_data**2+z_data**2)
theta=np.arccos(z_data/r)
phi=np.arctan2(x_data,y_data)

#print(r, theta, phi)

df['r'] = r
df['theta'] = theta
df['phi'] = phi

df.to_csv('processed.csv', index=False)


