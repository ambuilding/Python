### Introduction to Computer Science and Programming Using Python

- Thanks, Professor Eric Grimson
- paying attention, repetition of the concepts, and practice practice practice!
- computational methods
- [Resources to Help you Succeed](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/c77f2cc9fb2a42589f0d723e8fefbd35/c58684c1812443db80c4b0028aba9bc3/?child=first)

#### Python Basics
- Core elements of programs
  - Binds, strings, in/output, loop

#### Simple Programs
- Iterative algorithms
  - Generatig guesses
  - Exhaustive enumeration
  - Bisection search
  - Newton-Raphson(for root finding)

#### Function
- Iteration vs recursion
- Factorial
- Towers of Hanoi
- fibonacci
- a “divide and conquer” algorithm
- Modules and files
  - import batteries
  - from batteries import *

#### A credit card statement
- the option for you to pay a minimum amount of your charge, usually 2% of the balance due.
- earn money by charging interest on the balance that you don't pay.
- calculate the remaining balance

#### Paying Debt off in a Year
- 1 calculate the credit card balance after one year if a person only
- pays the minimum monthly payment required by the credit card company each month.
- balance/Updated balance each month, Monthly uppaidbalance,
- MinimumMonthlyPaymentRate, annualInterestRate/Monthly interest rate
- For each month:
  - Compute the monthly payment, based on the previous month’s balance.
  - Update the outstanding balance by removing the payment, then charging interest on the result.
  - Output the month, the minimum monthly payment and the remaining balance.
  - Keep track of the total amount of paid over all the past months so far.

- 2 calculates the minimum fixed monthly payment needed
- in order pay off a credit card balance within 12 months.
- balance, annualInterestRate/Monthly interest rate,
- Monthly unpaid balance, Updated balance each month

- 3 Using Bisection Search to Make the Program Faster
- calculate a more accurate fixed monthly payment
- the monthly payment is a multiple of $0.01, any dollar and cent amount.
- lower/upper bound

### Structured types
#### Tuples and Lists
- Tuples, lists, list operations, mutation, aliasing, cloning, functions as objects
- Dictionaries

###Debugging 🕷
- Defensive programming
- Use bisection method
- Put print halfway in code
- Decide where bug may be depending on values
- Narrow down space of possible sources of error

#####Test
- Remove syntax errors
- Remove static semantic errors
- Have a set of expected results

#####Classes
- Unit testing
  - Instead of waiting until the entire game is ready, you should test each function you write, individually, before moving on.
  - This approach is known as unit testing, and it will help you debug your code.
- Regression testing
- Integration testing

######Approaches
- intuition about natural boundaries
- Black box, explore paths through specification
- Glass box, explore paths through code

##### Hints
- look for the usual suspects
- ask why the code is doing what it is, not why it is not doing what you want
- the bug is probably not where you think it is – eliminate locations
- explain the problem to someone else
- don’t believe the documentation
- take a break and come back to the bug later

### Exceptions/Assertions

##### common error types:
- SyntaxError: Python can’t parse program
- NameError: local or global name not found
- AttributeError: attribute reference fails "
- TypeError: operand doesn’t have correct type
- ValueError: operand type okay, but value is illegal
- IOError: IO system reports malfunction (e.g. file not found)

- try else exception finally
- assert

### PS4, word game

- Word scores
  - calculate the score for a single word.
- Dealing with Hands
  - A hand is the set of letters held by a player during the game.
- Valid Words
  - At this point, we have written code to generate a random hand and display that hand to the user.
  - We can also ask the user for a word (Python's input) and score the word (using your getWordScore).
  - Now, verify that a word given by a player obeys the rules of the game.
- Playing a hand: Allows the user to play the given hand, print the total score.
- Playing a game: A game consists of playing multiple hands `playGame`.
  - Allow the user to play an arbitrary number of hands.
  - implement one final function to complete the word-game program.

- Give the computer the option to play, choose a Word, Play a Hand

### Object Oriented Programming

- each is an instance of an object, and every object has:
  - a type
  - an internal data representation (primitive or composite)
  - a set of procedures for interaction with the object
- each instance is a particular type of object

- everything in Python is an object and has a type
- objects are a data abstraction that capture:
  - internal representation through data attributes
  - interface for interacting with object through methods (procedures), defines behaviors but hides implementation
- can create new instances of objects
- can destroy objects
  - explicitly using del or just “forget” about them
  - Python system will reclaim destroyed or inaccessible objects – called “garbage collection”

- The Power of OOP
  - bundle together objects that share
    - common attributes and
    - procedures that operate on those attributes
  - use abstraction to make a distinction between how to implement an object vs how to use the object
  - build layers of object abstractions that inherit behaviors from other classes of objects
  - create our own classes of objects on top of Python’s basic classes

- update dict
  - gets rid of the key letter in the attribute hand dictionary when the frequency of the letter falls to 0,
  - leaves the key letter in the attribute hand dictionary even when the frequency of the letter falls to 0.

- Modularity
  - by isolating methods in classes, makes it easier to change behaviors

- create class that includes instances of other classes within it

##### Generators
- any procedure or method with yield statement called a generator

#### Encryption
- Encryption - the process of obscuring or encoding messages to make them unreadable until they are decrypted
- Decryption - making encrypted messages readable again by decoding them
- Cipher - algorithm for performing encryption and decryption
- Plaintext - the original message
- Ciphertext - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish.

##### Build the Shift Dictionary and Apply Shift
- The Message class contains methods that could be used to apply a cipher to a string,
- either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

##### PlaintextMessage
- `PlaintextMessage` is a subclass of Message and has methods to encode a string using a specified shift value.
- Our class will always create an encoded version of the message, and will have methods for changing the encoding.

##### CiphertextMessage
- Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial.
- If message is the encrypted message, and s is the shift used to encrypt the message,
- then apply_shift(message, 26-s) gives you the original plaintext message.
- tries each shift


- Searching and sorting algorithms
  - linear search
  - bisection search
  - monkey sort
  - bubble sort
  - selection sort
  - merge sort
- O(1), O(n), O(log n), O(n^2), O(2^n)
- Visualization of data
  - pylab, plots, labels
  - comparing plots, display details

- Course 6.00.1x / 6.00.2x
