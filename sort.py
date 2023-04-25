import math
from sys import maxsize


def mergesort(A, p, q):
    if p < q:
        m = math.floor((p+q)/2)
        mergesort(A, p, m)
        mergesort(A, m+1, q)
        sort(A, p, q)
    return A


def sort(A, p, q):
    m = math.floor((p+q)/2)
    n1 = m + 1-p
    n2 = q-m
    L = [0 for i in range(n1+1)]
    R = [0 for j in range(n2+1)]

    for i in range(0, n1):
        L[i] = A[p+i]
    L[n1] = maxsize

    for j in range(0, n2):
        R[j] = A[m+1+j]
    R[n2] = maxsize
    i = 0
    j = 0
    for k in range(p, q+1):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1


def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i >= 0 and A[i] >= key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


# A = [1, 5, 7, 4, 15, 99, 420, 3, 99, 8, 77, 1, 20, 23, 1]

# mergesort(A, 0, len(A)-1)
# print(A)
# output = insertionsort(A)

# mergesort(A, 0, len(A)-1)

# print(output)
