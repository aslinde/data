import numpy as np
a = np.array([[9.0,2.0,9,8,2],[0.5,56,2,4,5]])
#print(a, a.shape)
'''
## get specific element
print(a[1,4])

## get specific row
print(a[0,:])
## get specific column
print(a[:,0])

#[startIndex:endIndex:stepSize]
print(a[0, 1:4:2])

a[1,1] = 202
print(a)

## get specific row
a[:,2] = [11,22]
print(a)
'''
## 3D array
b = np.array([[[9.0,2.0,9,8,2],[0.5,56,2,4,5]], [[1.5,66,33,46,56], [19.0,12.0,19,18,12]]])
print(b[1,1,1])
print(b[0,1,1])