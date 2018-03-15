def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data(((1, 'mine'),
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))

print(small, large, words)
print((small, large, words))


US = ['MIT', 'Harvard', 'Yale']
UK = ['Cambridge', 'Oxford']

Unis = [US, UK]
Unisnew = [['MIT', 'Harvard', 'Yale'], ['US', 'UK']]

US.append('Princeton')
# avoid mutating a list as you are iterating over it
def remove_dups_new(L1, L2):
    # clone list
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1)
print(L2)


def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # slicing by 2 to achieve the result
    return aTup[::2]

# -*- coding: utf-8 -*-

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element,
       e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


def applyFuns(L, x):
    for f in L:
         print(f(x))

L = [1, -2, 3.4]
applyToEach(L, abs)
applyToEach(L, int)
applyToEach(L, fact)
applyToEach(L, fib)

applyFuns([abs, int, fact, fib], 4)

# Generalization of hops
for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, L1, L2):
    print(elt)
