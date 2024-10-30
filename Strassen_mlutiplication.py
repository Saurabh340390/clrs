#!usr/bin/env python3
# strassen_matrix_multiply.py

# clrs problem
# Saurabh Verma

#########################################################################
#                                                                       #
# Strassen-matrix-multiply(A,B,C)                                       #
#                                                                       #
# 1. Divide the matrices (A, B, C) into n/2 x n/2 submatrices.          #
#    A = ( [a, b] ) B = ( [e, f] ) and C = ( [c1, c2] )                 #
#        ( [c, d] )     ( [g, h] )         ( [c3, c4] )                 #
# 2. Create 10 matrices, each of n/2 x n/2 dimension, which is sum and  #
#    difference of two matrices created in step 1.                      #
#    i.e. S1, S2, ... S10.                                              #
# 3. Using submatrices in step 1 and step 2,recursively compute seven   #
#    matrix products P1, P2, ..., P7.                                   #   
#    these are expressed as  P1 = a(f-h), P2 = (a+b)h, P3 = (c+d)e,     #
#    P4 = d(g-e), P5 = (a+d)(e+h), P6 = (b-d)(g+h), P7 = (a-c)(e+f)     #
# 4. Compute the desired submatrices c1, c2, c3, c4 of result matrix C  #
#    by adding and subtracting various combination of Pi matrices.      #
#    c1 = P5 + P4 - P2 + P6, c2 = P1 + P2, c3 = P3 + P4,                #
#    c4 = P5 + P1 - P3 - P7                                             #
######################################################################### 

def matrix_multiply(A, B, C, n):
	""" function to check for exact power of 2 """
	if n>0 and n&(n-1) == 0 :
		strassen_matrix_multiply_aux(A, B, C, n,0,0,0,0,0,0)
	else:
		raise RuntimeError("Matrix dimension " + str(n) + " is not exact power of 2" )

# strassen auxiliary function for matrix multiplication
def strassen_matrix_multiply_aux(A, B, C, n, A_row, A_col, B_row, B_col, C_row, C_col):
	if n==1:
		C[C_row, C_col] += A[A_row, A_col] * B[B_row, B_col] 
	else :
		half = n//2
		
		# sub-matrices of A
		a = A[A_row : A_row + half, A_col : A_col + half]
		b = A[A_row : A_row + half, A_col + half : A_col + half*2]
		c = A[A_row + half : A_row + half*2, A_col : A_col + half]
		d = A[A_row + half : A_row + half*2, A_col + half : A_col + half*2]
		# sub-matrices of B
		e = B[B_row : B_row + half, B_col : B_col + half]
		f = B[B_row : B_row + half, B_col + half : B_col + half*2]
		g = B[B_row + half : B_row + half*2, B_col : B_col + half]
		h = B[B_row + half : B_row + half*2, B_col + half : B_col + half*2]
		
		# 10 matrices : S1, S2, ..., S10
		S1 = f - h
		S2 = a + b
		S3 = c + d
		S4 = g - e
		S5 = a + d
		S6 = e + h
		S7 = b - d
		S8 = g + h
		S9 = a - c
		S10 = e + f
		
		#initialize matrices P1, P2, ..., P7
		P1 = np.zeros((half, half))
		P2 = np.zeros((half, half))
		P3 = np.zeros((half, half))
		P4 = np.zeros((half, half))
		P5 = np.zeros((half, half))
		P6 = np.zeros((half, half))
		P7 = np.zeros((half, half))
		
		# recursively finding product i.e. P1, P2, ..., P7
		strassen_matrix_multiply_aux(A, S1, P1, half,  A_row, A_col, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(B, S2, P2, half,  B_row + half, B_col + half, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(B, S3, P3, half, B_row, B_col, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(A, S4, P4, half, A_row + half, A_col + half, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(S5, S6, P5, half,  0, 0, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(S7, S8, P6, half, 0, 0, 0, 0, 0, 0)
		strassen_matrix_multiply_aux(S9, S10, P7, half,  0, 0, 0, 0, 0, 0)
		
		# compute the value of submatrices of result matrix C
		C[C_row : C_row + half, C_col : C_col + half] += P5 + P4 - P2 + P6
		C[C_row : C_row + half, C_col + half : C_col + half*2] += P1 + P2
		C[C_row + half : C_row + half*2, C_col : C_col + half] += P3 + P4
		C[C_row + half : C_row + half*2, C_col + half : C_col + half*2] = P5 + P1 - P3 - P7
		
# Testing
if __name__ == "__main__" :
	import numpy as np
	n = 8
	A = np.arange(n*n).reshape(n, n)
	print(A)
	B = np.zeros((n, n))
	# permutation matrix for reversal of column_order
	for i in range(n):
		B[i, n-i-1] = 1
	C = np.zeros((n, n))
	matrix_multiply(A, B, C, n)
	print(C)
