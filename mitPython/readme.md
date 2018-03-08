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
