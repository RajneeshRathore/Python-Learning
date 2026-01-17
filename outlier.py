#Outlier detection and removal functions 
import numpy as np
data=np.array([5,8,10,15,18,22,34,46])

q1=np.percentile(data,25)
q3=np.percentile(data,75)
iqr=q3-q1
lower_bound=q1-(1.5*iqr)
upper_bound=q3+(1.5*iqr)
outliers=data[(data<lower_bound) | (data>upper_bound)]
clear_values=data[(data>=lower_bound) & (data<=upper_bound)]
print(f'q1:{q1}\nq3:{q3}\nIQR:{iqr}\nlower_bound:{lower_bound}\nupper_bound:{upper_bound}\noutliers:{outliers}\nclearData:{clear_values}')
