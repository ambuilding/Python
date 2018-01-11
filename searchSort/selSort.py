def selection_sort(L):
    suffixStart = 0

    while suffixStart != len(L):
        print(L)
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]

        suffixStart += 1


def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal= L[i]
        j = i + 1

        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1

        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp


test = [1, 5, 3, 8, 4, 9, 6, 2]
