#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chop.py
#  
#  Copyright 2015 Eusebio Aguilera <eusebio.aguilera@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
	This function returns the index of the of the value if is present in
	the array, and -1 otherwise. The array is supposed to be ordered, so
	we can apply the binary search in order to optimize the execution
"""

def chop(value, array):
	init = 0
	end = len(array)
	exit_cond = False
	
	# This condition is only for an empty list of values case
	if end > 0:
		# To minimize the code we can change this condition for "while (step)"
		# However this code would be a bit more unreadable
		while (not exit_cond): 
			
			step = ((end-init) / 2)
			
			exit_cond = not step # This is True if step is zero (False)
			
			idx = init + step
			
			# Uncomment next line to see the steps take by the algorithm
			# print "(%d, %d) --> %d" % (init, end, idx)
			
			if (array[idx] > value):
				end = idx
			elif (array[idx] < value):
				init = idx
			else:
				return idx
	
	# The code will exit the loop in case that the 
	return -1
	
"""
	This method is used to test the values that the method chop must 
	return.
"""
def test_chop():
	
	assert -1 == chop(3, []), "Incorrect result"
	
	assert -1 == chop(3, [1]), "Incorrect result"
	assert 0 ==  chop(1, [1]), "Incorrect result"
	#
	assert 0 ==  chop(1, [1, 3, 5]), "Incorrect result"
	assert 1 ==  chop(3, [1, 3, 5]), "Incorrect result"
	assert 2 ==  chop(5, [1, 3, 5]), "Incorrect result"
	assert -1 == chop(0, [1, 3, 5]), "Incorrect result"
	assert -1 == chop(2, [1, 3, 5]), "Incorrect result"
	assert -1 == chop(4, [1, 3, 5]), "Incorrect result"
	assert -1 == chop(6, [1, 3, 5]), "Incorrect result"
	#
	assert 0 ==  chop(1, [1, 3, 5, 7]), "Incorrect result"
	assert 1 ==  chop(3, [1, 3, 5, 7]), "Incorrect result"
	assert 2 ==  chop(5, [1, 3, 5, 7]), "Incorrect result"
	assert 3 ==  chop(7, [1, 3, 5, 7]), "Incorrect result"
	assert -1 == chop(0, [1, 3, 5, 7]), "Incorrect result"
	assert -1 == chop(2, [1, 3, 5, 7]), "Incorrect result"
	assert -1 == chop(4, [1, 3, 5, 7]), "Incorrect result"
	assert -1 == chop(6, [1, 3, 5, 7]), "Incorrect result"
	assert -1 == chop(8, [1, 3, 5, 7]), "Incorrect result"



def main():
	
	test_chop()
	
	return 0

if __name__ == '__main__':
	main()

