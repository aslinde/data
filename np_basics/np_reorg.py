import numpy as np
a = np.array([[9.0,2.0,9,8,2],[0.5,56,2,4,5]])
b = np.array([[9.0,2.0,9,8,2],[0.5,56,2,4,5]])
b = b/2
a_post = a.reshape((10,1))
print(a_post)


# Vertically stacking
print(np.vstack([a,b]))