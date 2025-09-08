import numpy as np
array_3d = np.array([[[1, 2, 3], 
                      [4, 5, 6]], 
                     [[7, 8, 9], 
                      [10, 11, 12]]])
print(array_3d.ndim)  # 3
print(array_3d.shape) # (2, 2, 3) - 2 layers, 2 rows, 3 columns



element = array_3d[0][1][2]  # Accessing the element at layer 0, row 1, column 2
print(element)  # 6 because it is the 3rd element in the 2nd row of the 1st layer


element = array_3d[0, 1, 2]  # Faster and more efficient because it accesses the 3D array in one step
