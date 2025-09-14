import numpy as np
#              0  1  2  3  4  
arr1=np.array([10,20,30,40,50])
#              -5 -4 -3 -2 -1
print(arr1[0])
print(arr1[-1])

# 2d 
import numpy as np
arr1=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr1[1,2])
print(arr1[0,:])
print(arr1[:,1])