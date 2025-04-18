import numpy as np

outer_array = np.ones((5,5))
inner_array = np.zeros((3,3))

inner_array[1,1] = 9
outer_array[1:4,1:4] = inner_array
print(outer_array)