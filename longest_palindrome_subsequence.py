#!/usr/bin/env python3
# longest_palindrome_subsequence.py

# clrs problem
# Saurabh verma

#########################################################################
# LONGEST-PALINDROME-SUBSEQUENCE(X)                                     #
# 	n = X.length                                                    #
#   Let p[0..n, 0..n] and b[1..n, 1..n]                                 #
#   for i = 1 to n-1                                                    #
#   	p[i, i] = 1                                                     #
#   	j = i + 1                                                       #
#       if xi == xj                                                     #
#   		p[i, j] == 2                                            #
# 			b[i, j] = " southwest arrow "                   #
#       else                                                            #
#           p[i, j] == 1                                                #
# 			b[i, j] = " down arrow "                        #
# 	p[n, n] = 1                                                     #
# 	for i = n-2 downto 1                                            #
#   	for j = i + 2 to n                                              #
#       	if xi == xj                                             #
#           	p[i, j] = p[i+1, j-1] + 2                               #
# 				b[i, j] = " northwest arrow "           #
# 			elseif p[i+1, j] >= p[i, j-1]                   #
# 				p[i, j] = [i+1, j]                      #
# 				b[i, j] = " down arrow "                #
# 			else p[i, j] = p[i, j-1]                        #
# 				 b[i, j] = " left arrow "               #
# 	return p and b                                                  #
#                                                                       #
# GENERATE-LPS(b, X, i, j, S)                                           #
#  if i > j                                                             #
#  	return S                                                        #
#  elseif i==j                                                          #
#  	return S||xi                                                    #
#  elseif b[i, j] == " southwest arrow "                                #
#  	return GENERATE-LPS(b, X, i+1, j-1, S) || xi                    #
#  elseif b[i, j] == " down arrow "                                     #
#  	return GENERATE-LPS(b, X, i+1, j, S)                            #
#  else  return GENERATE-LPS(b, X, i, j-1, S)                           #
#                                                                       #
#########################################################################

""" A palindrome is string with 1 or more than one that read same forward and backward.
"""

DOWN_AND_LEFT = "\u2199"  # northwest arrow
DOWN = "\u2193"           # down arrow
LEFT = "\u2190"           # left arrow

import numpy as np

def longest_palindrome(X, n):
	""" Recursively compute the length lps of given sequence 
	Arguments:
	X -- a sequence represented as string or array/list
	n -- length of X 
	
	Returns :
	p -- an array in which p[i, j] is the length of sequence X[i:j].
	     Entries used are p[0:n, 0:n]
	b -- an array in which b[i, j] is points to the table entries corresponding 
	     to optimal subproblem solution chosen when computing p[i, j].
	     Entries used are b[1:n, 1:n]
	"""
	
	b = np.empty(shape = [n+1, n+1], dtype = str) # using indices 1:n, 1:n
	p = np.zeros(shape = [n+1, n+1] )             # using indices 0:n, 0:n
	for i in range(1, n): # fill row by row
		p[i, i] = 1
		j = i + 1
		if X[i-1] == X[j-1]: # -1 for 0-origin indexing
			p[i,j] = 2
			b[i,j] = DOWN_AND_LEFT
		else :
			p[i, j] = 1
			b[i, j] = DOWN
	p[n, n] = 1
	
	for i in range (n-2, 0, -1):
		for j in range(i+2, n+1):
			if X[i-1] == X[j-1]:
				p[i, j] = p[i+1, j-1] + 2
				b[i, j] = DOWN_AND_LEFT
			elif p[i+1, j] >= p[i, j-1]:
				p[i, j] = p[i+1, j]
				b[i, j] = DOWN
			else :
				p[i, j] = p[i, j-1]
				b[i, j] = LEFT
	return p, b

def generate_lps(b, X, i, j) -> str:
	""" Return lps of the sequence X.
		
	Arguments:
	b -- an array in which b[i, j] points to table corresponding
	to the optimal subproblem solution when computing p[i, j].
	Entries used are b[1:n, 1:n].
	X -- a sequence represented as string or array/list.
	i -- first index of subsequence, on first call equal to 1
	j -- second index of subsequence, on first call equal to X.length, n. 
	S -- returned lps sequence, on first call it is empty.
	"""
	if i> j:
		return ""
	elif i == j:
		return X[i-1]
	elif b[i,j] == DOWN_AND_LEFT :
		return X[i-1] + generate_lps(b, X, i+1, j-1) + X[i-1]
	elif b[i, j] == DOWN :
		return generate_lps(b, X, i+1, j)
	else :
		return generate_lps(b, X, i, j-1)


# Testing
if __name__ == "__main__":
	X = "aacabdkacaa"
	Y = "ccc"
	m = len(X)
	n = len(Y)
	p1, b1 = longest_palindrome(X, m)
	S1 = generate_lps(b1, X, 1, m)
	print(S1)                           # should be aacakacaa
	print()
	
	p2, b2 = longest_palindrome(Y, n)
	S2 = generate_lps(b2, Y, 1, n) 
	print(S2)                           # should be ccc
	print()
