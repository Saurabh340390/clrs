#!/usr/bin/env python3
# Key_Object.py

# Clrs Problem utility function
# Saurabh Verma

#########################################################################
#                                                                       #
# key-object-function                                                   #
# 1. Ir consist of Key_object class that encompasses these function     #
# 2. __init__ to initalize object with a string and a key               #
# 3. get-key to fetch key of an object                                  #
# 4. set key to set the new key for object without accessing self       #
# 5. __gt__ defines greater than function that use the key to compare.  #
# 6. __str__ to define print of the object                              #
#                                                                       #
#########################################################################

class KeyObject :

	def __init__(self, string, key):
		self.string = string
		self.key = key
	@staticmethod
	def getkey(x):
		return x.key
	@staticmethod
	def setkey(x, key):
		x.key = key
	
	def __gt__(self, obj2):
		return self.key > obj2.key
	
	def __str__(self):
		return self.string


# Testing
if __name__ == "__main__":

	objA = KeyObject("Alice",7)
	objB = KeyObject("Bob", 9)
	print(objA>objB)
	print(objA<objB)
