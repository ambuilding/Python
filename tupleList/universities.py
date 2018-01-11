US = ['MIT', 'Harvard', 'Yale']
UK = ['Cambridge', 'Oxford']

Unis = [US, UK]
Unisnew = [['MIT', 'Harvard', 'Yale'], ['US', 'UK']]

# US.append('Princeton')
# avoid mutating a list as you are iterating over it
def remove_dups_new(L1, L2):
	L1_copy = L1[:]
	for e in L1_copy:
		if e in L2:
			L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1)
print(L2)
