import math
def recursiveBinSearch(arr, x, left, right):
    if left == right:
        if arr[left] == x:
            ind = left
        else:
            ind = []
    else:
        mid = math.floor((left + right)/2)
        if arr[mid] < x:
            ind = recursiveBinSearch(arr, x, mid + 1, right)
        else:
            ind = recursiveBinSearch(arr, x, left, mid)
    return ind

ind = recursiveBinSearch([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23, 0, 9)
print(ind)