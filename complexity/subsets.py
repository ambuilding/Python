def genSubsets(L):
    if len(L) == 0:
        return [[]] #list of empty list

    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []

    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    return smaller+new  # combine those with last element and those without

test = [1,2,3,4]

super = genSubsets(test)

