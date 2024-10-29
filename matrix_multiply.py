#!/usr/bin/env python3
# recursive_matrix_multiply.py

# CLRS problem
# Saurabh Verma

#########################################################################
#                                                                       #
# recursive matrix multiplication(A,B)                                  #
#                                                                       #
# 1. N X N matrix, where N is exact power of 2                          #
# 2. Let C be a new N X N matrix.                                       #
# 3. if N == 1                                                          #
#       compute c11 = a11 * b11                                         #
# 4. else partition A,B and C as                                        #
#            A= ( [A11 A12] [A21 A22] ) ; B = ([B11 B12] [B21 B22]) and #
#            C= ( [C11 C12] [C21 C22] )                                 #
# 5. Then compute C11, C12, C21, and C22 recurisvely                    #
# 6. C11 =  recursive-matrix-multiplication(A11, B11) +                 #
#           recursive-matrix-multiplication(A12, B21)                   #
# 7. C12 = recursive-matrix-muiltiplication(A11, B12) +                 #
#           recursive-matrix-multiplication(A12, B22)                   #
# 8. C21 = recursive-matrix-multiplication(A21, B11) +                  #
#           recursive-matrix-multiplication(A22, B21)                   #
# 9. C22 = recursive-matrix-multiplication(A21, B12) +                  #
#          recursive-matrix-multiplication(A22, B22)                    #
# 10. return C                                                          #
#                                                                       #
#########################################################################

def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B, C):
	n = A.shape[0]
	# A wrapper method to verify n is exact power of 2
	# then it calls for an auxiliary function for multiplication
	if(n>0 and n&(n-1) == 0):
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A,B,C,n,0,0,0,0,0,0)
	else:
		raise RuntimeError("matrix dimension " + str(n) + " is not an exact power of 2.")

# auxiliary function for matrix multiplication
def SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, n, A_row, A_col, B_row, B_col, C_row, C_col):
	""" there are 9 parameter i.e. matrix A & B, result matrix, and thier starting row and column """
	if n == 1 :
		C[C_row, C_col] += A[A_row, A_col]*B[B_row, B_col]
	else:
		half = n//2
		
		# using index calculation to figure out the sub-matrices
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row, A_col, B_row, B_col, C_row, C_col)
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row, A_col + half, B_row + half, B_col, C_row, C_col)
		
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row, A_col, B_row, B_col + half, C_row, C_col+half)
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row, A_col+ half, B_row+ half, B_col+half, C_row, C_col+half)
		
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row + half, A_col, B_row, B_col, C_row + half, C_col)
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row + half, A_col + half, B_row + half, B_col, C_row + half, C_col)
		
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row + half, A_col, B_row, B_col+ half, C_row + half, C_col + half)
		SQUARE_MATRIX_MULTIPLY_RECURSIVE_AUX(A, B, C, half, A_row + half, A_col + half, B_row + half, B_col + half, C_row + half, C_col + half) 

# Testing
if __name__ == "__main__":
	
	import numpy as np
	from matrix_inverse import almost_equal
	n = 8
	A = np.arange(n*n).reshape(n, n)
	B = np.zeros((n, n))
	C = np.zeros((n, n))
	# permutation matrix to reverse the column order
	for i in range(n):
		B[i, n-i-1] = 1
	SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B, C)
	print(C) # should be A with its column order reversed
	
	# Try with random numbers
	rg = np.random.default_rng(1) # random generator with fixed seed
	A = rg.random((n, n))
	print(A)
	B = rg.random((n, n))
	print(B)
	C = np.zeros((n, n))
	SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B, C)
	print(C)
	
	npC = A @ B
	print(npC)
	print(almost_equal(C, npC, n))
	# check for the case when n is not an exact power of 2
	n = 6 
	A = np.arange(n*n).reshape(n,n)
	B = np.zeros((n, n))
	for i in range(n):
		B[i, n-i-1] = 1
	C = np.zeros((n, n))
	try:
		SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B, C)
		print(C)
	except RuntimeError as e:
		print(e)
