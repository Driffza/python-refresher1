import numpy as np

a = np.array([ 1, 2, 3])
b = np.array([ 4, 5, 6])

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

"Problem #1"

sum_vector = a + b
diff_vector = a - b
print (f"Sum of verctors a and b: {sum_vector}")
print(f"Difference of vectors a and b: {diff_vector}")
"Problem #2"


sum_matrix = A + B
diff_matrix = A - B
print(f"Sum of matrices A and B: {sum_matrix}")
print(f"Difference of matrices A and B: {diff_matrix}")
"Problem #3"

dot_product = np.dot(a, b)
print(f"Dot product of vectors a and b: {dot_product}")

"Problem #4"

"""Given the matrices 
C = [[ 1, 2, 3], [ 4, 5, 6]] and D =[[ 7, 8, 9, 10], [ 11, 12, 13, 14], [ 15, 16, 17, 18]]
 , find the product of the matrices."""

C= np.array([[ 1, 2, 3], [ 4, 5, 6]])
D = np.array([[ 7, 8, 9, 10], [ 11, 12, 13, 14], [ 15, 16, 17, 18]])