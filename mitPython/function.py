def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


def is_even(i):
	"""
	Input: i, a positive int
	Returns True if i is even, otherwise False
	"""
	print("hi")
	return i%2 == 0

is_even(3)


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

printName('Eric', 'Grimson', False)

def mult_iter(a, b):
	result = 0
	while b > 0:
		result += a
		b -= 1
	return result
def mult(a, b):
	if b == 1:
		return a
	else:
		return a + mult(a, b-1)

# recursion
def fact(n):
    if n == 1:
    	return 1
    else:
    	return n*fact(n-1)
print(fact(4))

# iteration
def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
    	prod *= i
    return prod

# Towers of hanoi
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))


# files and modules

# The greatest common divisor of two positive integers
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue

# Recursive case
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # Base case is when b = 0
    if b == 0:
        return a
    return gcdRecur(b, a % b)

# use the idea of bisection search to determine if a character is in a string
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: See if the character in the middle of aStr equals the
    #   test character
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        # We found the character!
        return True

    # Recursive case: If the test character is smaller than the middle
    #  character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Otherwise the test character is larger than the middle character,
    #  so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[midIndex+1:])
