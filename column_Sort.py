#!/usr/bin/env python3
# column_sort.py

# CLRS problem
# Saurabh Verma

#########################################################################
#                                                                       #
# 1. Sort each column                                                   #
# 2. Transpose the array, but reshape it back to r rows and s columns.  #
# 3. Sort each column.                                                  #
# 4. Perform the inversion of the permutation performed in step 2.      #
# 5. Sort each column.                                                  #
# 6. Shift the top half of each column into bottom half of same column, #
#    shift bottom half of the each column into top half of the next     #
#    column to the right. The topmost of leftmost remain empty.         #
#    The bottom of last column to new rightmost column, and leave the   #
#    bottom half of this new column empty.                              #
# 7. Sort each column.                                                  #
# 8. Perform the inverse of the permutation performed in step 6.        #
#                                                                       #
#########################################################################

import numpy as np

# function required at step 6 
def shift_columns(matrix):
	r, s = matrix.shape
	new_matrix = np.zeros((r, s+1), dtype = matrix.dtype)
	half_r = r//2
	# To shift bottom half to next right column and top half to its bottom half
	for col in range(s):
		new_matrix[:half_r, col+1] = matrix[half_r: ,col] 
		new_matrix[half_r:, col] = matrix[:half_r, col]
	# Last column moved to new column 
	new_matrix[:half_r, -1] = matrix[half_r:, -1]
	return new_matrix
	
# function required at step 8
def inverse_shift_columns(matrix):
	r, s = matrix.shape
	s -= 1
	original_matrix = np.zeros((r, s), dtype = matrix.dtype)
	half_r = r//2
	# To shift top half into bottom of left column and bottom half    of column to top column
	for col in range(s):
		original_matrix[:half_r, col] = matrix[half_r:, col]
		original_matrix[half_r:, col] = matrix[:half_r, col+1]
	return original_matrix
# Testing
if __name__ == "__main__":
	matrix = np.array([[10, 14, 5], [8, 7, 17], [12, 1, 6], [16, 9, 11], [4, 15, 2], [18, 3, 13]]) # taking a random matrix
        # step 1
	matrix.sort(axis=0)
	
	# step 2
	r,s = matrix.shape
	matrix = matrix.T.flatten()
	matrix = matrix.reshape(r,s)
	
	# step 3
	matrix.sort(axis=0)
	
	# step 4
	matrix = matrix.flatten()
	matrix = matrix.reshape(s,r)
	matrix = matrix.T

	# step 5
	matrix.sort(axis=0)
	
	# step 6
	matrix = shift_columns(matrix)

	#step 7
	matrix[:,:-1].sort(axis=0)
	
	#step 8
	matrix = inverse_shift_columns(matrix)
	
	print(matrix)	# printing the major column order sorted matrix
