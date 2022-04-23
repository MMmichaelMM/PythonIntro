def powRec1(x, n):
    if n == 0:
        res = 1
    else:
        res = x * powRec1(x, n-1)
    return res


print(powRec1(2, 6))

