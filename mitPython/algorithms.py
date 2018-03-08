# -*- coding: utf-8 -*-
# Bisection search, square root
# Both low = 1.0 and low = 0.0 work.

x = 25
epsilon = 0.01
numGuesses = 0

low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))

    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))

cube = 54
epsilon = 0.01
num_guesses = 0

low = 0
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
	print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))

    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
# search space: N / 2**guess

# decimal to binary
num = int(input('Enter a decimal number: '))
#num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    # gives us the last binary bit
    num = num//2
    # all the bits get shifted right
    print('result = ' + str(result) + ' num = ' + str(num))

if isNeg:
    result = '-' + result

print(result)

# fractions
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('shift = ' + str((2**p)*x))
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
    print('p = ' + str(p))

num = int(x*(2**p))
print('num = ' + str(num))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

print("result = " + str(result) + " p - len(result) = " + str(p - len(result)))
for i in range(p - len(result)):
    result = '0' + result
print("resultFor = " + str(result))
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))


# newton-raphson
epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))

print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))


# guess my number
print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
high = 100
low = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (high + low)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        high = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        low = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
