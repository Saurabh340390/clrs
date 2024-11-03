#!/usr/bin/env python3
# direct_address_hashtable.py

# CLRS problem
# Saurabh Verma

#########################################################################
#                                                                       #
# Direct-address-table                                                  #
#                                                                       #
# DIRECT-ADDRESS-SEARCH(T,k)                                            #
#    return T[k]                                                        #
#                                                                       #
# DIRECT-ADDRESS-INSERT(T,k)                                            #
#    T[X.key] = x                                                       #
#                                                                       #
# DIRECT-ADDRESS-DELETE(T,X)                                            #
#    T[X.key] = NIL                                                     #
#                                                                       #
#########################################################################

# This technique works well when the universe of key is reasonably small.
class Direct_Address_Hashtable:
	def __init__(self, m, get_key_func=None):
		"""Initialize hashtable with direct address table of size m""" 
		self.m = m
		self.table = [None]*m
		# If get-key-function is not defined then identity function is used
		if get_key_func==None:
			self.is_identity=True
			self.get_key = lambda x : x
		else : 
			self.is_identity=False
			self.get_key = get_key_func
	
	def direct_address_search(self, k):
		"""Return the object at slot k"""
		return self.table[k]
	def direct_address_insert(self, x):
		"""Insert the object with a key into the table"""
		self.table[self.get_key(x)] = x
	def direct_address_delete(self, x):
		"""Delete the object with a key in the table"""
		self.table[self.get_key(x)] = None
	def direct_address_maximum(self):
		"""Return the maximum object only in case of number stored with key as identity function"""
		if self.is_identity == True:
			return self.table_maximum(self.m - 1)
		else :
			raise RuntimeError("This hashtable with direct-address-table doesn't use identity function for key")
			
	def table_maximum(self,k):
		"""A recursive function that traverse from highest slot to seek first non-None one."""
		if k<0:
			return None
		elif self.direct_address_search(k) != None :
			return k
		else :
			return self.table_maximum(k-1)
	def __str__ (self):
		""" Returns a string representation of the table"""
		string = "["
		if self.m>0:
			for i in range(self.m-1):
				string += str(self.table[i]) + ","
			string += str(self.table[self.m-1]) 
			string += "]"
		return string


#Testing
if __name__ == "__main__":
	from key_object import KeyObject
	
	#Hashtable of integers
	hashtable1 = Direct_Address_Hashtable(10)
	for i in range(10):
		hashtable1.direct_address_insert(i)
	print(hashtable1)
	hashtable1.direct_address_delete(9)
	print(hashtable1)
	print(hashtable1.direct_address_search(7))
	print(hashtable1.direct_address_search(9))
	print(hashtable1.direct_address_maximum())
	try:
		hashtable1.direct_address_insert(11)
	except IndexError as e:
		print(e)

	#Hashtable of objects
	hashtable2 = Direct_Address_Hashtable(10, KeyObject.get_key)
	hashtable2.direct_address_insert(KeyObject("Thomas",4))
	hashtable2.direct_address_insert(KeyObject("Bob",6))
	hashtable2.direct_address_insert(KeyObject("Alice",7))
	david = KeyObject("David",5)
	hashtable2.direct_address_insert(david)
	print(hashtable2)
	print(hashtable2.direct_address_search(7))
	hashtable2.direct_address_delete(david)
	print(hashtable2)
	try:
		print(hashtable2.direct_address_maximum())
	except RuntimeError as e:
		print(e)
	hashtable2.direct_address_delete(hashtable2.direct_address_search(7))
	print(hashtable2)
