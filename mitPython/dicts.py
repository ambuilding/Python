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

# dics operations
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
grades['Sylvan'] = 'A'
'John' in grades
'Daniel' in grades
del(grades['Ana'])
grades.keys()
grades.values()

# function to analyze song lyrics
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)

def most_common_words(freqs):
    #values = freqs.values()
    best = max(freqs.values())
    words = []

    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dictionary
        else:
            done = True
    return result

print(words_often(beatles, 5))

# fibonacci recursive
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

# fibonacci with a dictionary
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}

argToUse = 34
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))


def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        print(n, d[n])
        return ans


# global variables, tracking efficiency
numFibCalls = 0
fibArg = 34

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2}
print(fib_efficient(fibArg, d))
print('function calls', numFibCalls)


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result

def how_many(aDict):
    '''
    Another way to solve the problem.
    aDict: A dictionary, where all the values are lists.
    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
