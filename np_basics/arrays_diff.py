import numpy as np
#Zeros
print(np.zeros((5,5,5)))
print(np.full((5,5),2))

## Random
print(np.random.rand(5,5))

a = np.array([1,2,3], dtype="int16")
print(np.random.random_sample(a.shape))