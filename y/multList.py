# -*- coding: utf-8 -*-

def mult_list_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0]*mult_list_recur(L[1:])

print(mult_list_recur([1,3,5,7,9]))

def mult_iter(a, b):
	result = 0

	while b > 0:
		result += a
		b -= 1
	return result

def mult_recur(a, b):
	if b == 1:
		return a
	else:
		return a + mult(a, b-1)
