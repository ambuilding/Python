## HarvardX: PH526x Using Python for Research

## Basics of Python 3
### Part 1: Objects and Methods

- 1.1 the meaning of object type, value, and identity
- the difference between data attributes and methods
- modules
- the numeric types in Python: integers, floating-point numbers, and complex numbers
- basic operations you can conduct with num
- random.choice
- the Boolean operations or, and, and not
- the Python comparison operations and the Boolean values they return

### Part 2: Sequence Objects

- 1.2 some of the Python sequence types and sequence operations
- construct / index Python lists
- some of the methods that can be applied to lists
- Sequence Objects: tuples, range, strings,
- Python sets and the differences between a set and a frozenset. set operations
- Python dictionaries and the key-value pairs they contain
- the dynamically updated view objects `dict.keys(), dict.values(), and dict.items()`

### Part 3: Manipulating Objects

- 1.3  the difference between static and dynamic typing
- how dynamic typing in Python works for mutable and immutable objects
- the distinction between shallow and deep copies of objects
- the structure of Python compound statements such as the if statement
- for and while
- use a list comprehension to apply an operation to all items in a list
- read and write files line-by-line
- function / common mistakes and errors

### DataCamp

- Consider a circle enclosed by a square. The ratio of their areas is `pi / 4` .
- find a way to approximate this value.
- A list of numbers can be very unsmooth, meaning very high numbers can be right next to very low numbers.
- One way to smooth the values in the list is to replace each value with the average of each value's neighbors, including the value itself.


## Week 2: Python Libraries and Concepts Used in Research

### Part 1: Scope Rules and Classes

- the LEGB rule for scope
  - local, the current function you're in
  - Enclosing function, the func that called the current func, if any
  - global, the module in which the func was defined
  - built-in refers to Python's built-in namespace.

### Part 2: NumPy

- NumPy arrays, including vectors and matrices of zeros and ones
- an important distinction between slicing an array and indexing an array
  - slice, using the colon operator, get a view of the object
  - index, return a copy of the original data.
- construct, `np.lenspace() / np.logspace`
- `shape / size`
- determine whether the elements of an array fulfill a logical condition using `np.any() / np.all()`


### Part 3: Matplotlib and Pyplot

- 2.3 Create simple plots using matplotlib.pyplot
- Customize your plots by adding a legend, adjusting and labeling the axes, and saving your figures
- create plots with logarithmic axes using semilogx, semilogy, and loglog
- generate histograms using plt.hist()
- create subplots using plt.subplot()



- 2.4 use random.choice to simulate random processes such as coin flips or the roll of a die
- explore simulations of randomness and data visualization
- use the numpy.random module to simulate randomness

```
help iPython
np.sum?
```

- 2.5 measure running time using the time module
- Compare the running time of a simulation written in pure Python to one written using NumPy
- Numpy implementation is faster than the Python-based implemetaion.
-  generate random walks using NumPy


## Week 3: Case Studies Part 1

- 3.1how to translate DNA
- how to process texts
- how to classify items using the k-nearest neighbors method


