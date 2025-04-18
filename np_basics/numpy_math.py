import numpy as np
#a = np.array([[9.0,2.0,9,8,2],[0.5,56,2,4,5]])

#print(a+2)

## Linear Algebra

b = np.full((1,3),4)
c = np.full((3,2),2)

print(np.matmul(b,c))

d= np.identity(3)
print(np.linalg.det(d))