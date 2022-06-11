def bubble_sort(l, n):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n > 1:
        bubble_sort(l, n-1)


l = [13, 6, 2, 9, 11, 9, 3, 7, 12]
n = len(l)
bubble_sort(l, n)
print(l)

