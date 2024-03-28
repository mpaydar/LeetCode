import numpy as np

mean_difference=np.array([[0],[-1.3]])
mean_difference_transpose=np.array([0,-1.3])
inverse_matrix=np.array([[1.1,0.57],[0.57,3.23]])
exponent_term=mean_difference_transpose @ inverse_matrix @ mean_difference
print(exponent_term)
