def powRec2(x, n):
    if n == 0:
        res = 1
    elif n == 1:
        res = x
    elif n % 2 == 1:
        res = x*powRec2(x*x, (n-1)/2)
    else:
        res = powRec2(x*x, n/2)
    return res


print(powRec2(2, 6))