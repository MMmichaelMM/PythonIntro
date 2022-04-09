import math
def binSearch(arr, x):
    left = 0
    right = len(arr) - 1
    while right > left:
        mid = math.floor((left + right)/2)
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    if arr[left] == x:
        ind = left
    else:
        ind = []
    return ind


ind = binSearch([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)
print(ind)