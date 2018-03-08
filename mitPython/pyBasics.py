# -*- coding: utf-8 -*-
'''
variables branch
'''
# binding variables and values
pi = 3.14159
pi_approx = 22/7
radius = 2.2
area = pi * (radius**2)
# re-bind
radius = radius + 1

# branch, conditional, Even or Odd
x = int(input('Enter an integer: '))
if x%2 == 0:
	print('')
	print('Even')
else:
	print('')
	print('Odd')
print('Done with conditional')

# nested conditionals
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

if x < y and x < z:
	print('x is least')
elif y < z:
	print('y is least')
else:
	print('z is least')


x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
	print("x and y are equal")
	if y != 0:
		print("therefore, x / y is", x/y)
elif x < y:
	print("x is smaller")
else:
	print("y is smaller")
print("thanks!")

x=7
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

# control flow
n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
	n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

# break
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
  	    break
print(mysum)

# Iteration
# squares the value of x by repetiive addition
x=3
ans = 0
itersLeft = x
while (itersLeft != 0):
	ans = ans + x
	itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

# guess and check
# cube root of integer
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
	ans = ans + 1
	if ans**3 != x:
		print(str(x) + ' is not a perfect cube')
	else:
		print('Cube root of ' + str(x) + ' is ' + str(ans))

# solution to positive case
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
	if x < 0:
		ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))ositive case

cube = 8
for guess in range(cube+1):
	if guess**3 == cube:
		print("Cube root of ", cube, " is ", guess)

cube = 8
for guess in range(abs(cube)+1):
	if guess**3 >= abs(cube):
		break
if guess**3 != abs(cube):
	print(cube, ’is not a perfect cube’)
else:
    if cube < 0:
    	guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

# Square root
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
	ans += 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")

# strings and loops
s = "abcdefgh"
for index in range(len(s)):
	if s[index] == 'i' or s[index] == 'u':
		print("There is an i or u")
for char in s:
	if char == 'i' or char == 'u':
		print("There is an i or u")


an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]

    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)

    i += 1

print("What does that spell?")

for i in range(times):
    print(word, "!!!")

# Approximate solution, cube root
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
# try with cube = 27, and large step (e.g. 2.0, 0.01)
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)

if abs(guess**3 - cube) >= epsilon:
	print('Failed on cube root of', cube)
else:
	print(guess, 'is close to the cube root of', cube)
