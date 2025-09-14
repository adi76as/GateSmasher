# Attributes of Numpy Array:
# 1. ndim= dimension [1D, 2D] (number of brackets)
# 2.shape= shape [(2,3)2 rows,3 cols]
# 3.size= [(2,3) 6 numbers of elements]
# 4.datatype= kon type er data ase ,same type er thak e
# 5.itemsize= every element koto byte niche seta showed

# import numpy as np
# list1=[[10,20,30],[40,50,60],[70,80,90]]
# array1=np.array(list1)
# print(array1.ndim)
# print(array1.shape)

import numpy as np
list1=([[[10,20,30],[40,50,60]],
      [[70,80,90],[100,110,120]]])
array1=np.array(list1)
print(array1.ndim)
print(array1.shape)
# 2d array er 2 ta layer hobe
print(array1.size)
print(array1.dtype)
# 64 = protita 8 byte kore (1 byte=8 bit)
print(array1.itemsize)