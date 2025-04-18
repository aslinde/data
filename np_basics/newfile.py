import numpy as np
print(np.__version__)

a = np.array([1,2,3], dtype="int16")
print(a)

b = np.array([[9.0,2.0],[0.5,56]])
print(b)

## Get dimendsion
print(a.ndim, b.ndim)
print(a.shape, b.shape)
print(a.dtype, b.dtype)