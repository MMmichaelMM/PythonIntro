import math
def mergeSort(arr):
    n = len(arr)
    if(n == 1):
        sortedArr = arr
    else:
        mid = math.floor(n/2)
        half1 = mergeSort(arr[:mid])
        half2 = mergeSort(arr[mid:])
        sortedArr = mergeTwoArrays(half1, half2)
    return sortedArr


def mergeTwoArrays(x, y):
    n = len(x)
    m = len(y)
    z = [0] * (n+m) # list with n+m zeros
    ix = 0
    iy = 0
    for iz in list(range(n+m)):
        if ix >= n:
            z[iz] = y[iy]
            iy = iy + 1
        elif iy >= m:
            z[iz] = x[ix]
            ix = ix + 1
        elif x[ix] <= y[iy]:
            z[iz] = x[ix]
            ix = ix + 1
        else:
            z[iz] = y[iy]
            iy = iy + 1
    return z


arr = [7, 2, 9, 4, 3, 8, 6, 1]
print("unsorted array: ", arr)
print("sorted array: ", mergeSort(arr))
