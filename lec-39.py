# Slicing is a way to extract a subset of data from a numpy array
import numpy as np
# #                 -7 -6 -5 -4 -3 -2 -1
array1= np.array([10,20,30,40,50,60,70])
# #                 0  1  2  3  4  5  6
print(array1[1:3])
print(array1[1:6:2])
print(array1[-1:-3:-1])
print(array1[::2])
print(array1[::-1])
# direction reverse hole -1 must dithe hobe

import numpy as np
array2= np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]])
print(array2[1, ])
print(array2[:,1])
print(array2[1:3, ])
print(array2[1:3,1:3])
print(array2[:,1:3])
print(array2[1:3,1])
print(array2[1:3, :1])
print(array2[1:3,1:])
# line 22 end na dile last porjonto sob nibe
# arry2[row,col]
# khali rakha jai na colon(:) dithe hoi row er somoi , col e na dileo hoi
