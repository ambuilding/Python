# -*- coding: utf-8 -*-

x = int(input('Enter an integer: '))

if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')

def is_even(i):
	"""
	Input: i, a positive int
	Returns True if i is even, otherwise False
	"""
	print("hi")
	return i%2 == 0
