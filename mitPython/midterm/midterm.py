def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 5
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        else:
            guess -= 1
    return guess

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
#    total = 0
#    for i in range(len(L)):
#        total += L[i] * x**(len(L)-i-1)
    def total(x):
        return sum([L[i] * x**(len(L)-i-1) for i in range(len(L))])

    return total

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    result = []
    for i in aList:
        if type(i) != list:
            result.append(i)
        else:
            result.extend(flatten(i))

    return result

#[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    unique = {}
    for k, v in aDict.items():
        if list(aDict.values()).count(v) == 1:
            unique[k] = v
    if len(unique) == 0:
        result = []
    else:
        result = sorted(list(unique.keys()))
    return result

def uniqueValues2(aDict):
	uniqueKeys = [k for k,v in aDict.items() if list(aDict.values).count(v) == 1]
	uniqueKeys.sort()

	return uniqueKeys

