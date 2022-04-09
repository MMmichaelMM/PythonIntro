
def fibonacci(n):
    if n <= 1:
        res = n
    else:
        res = fibonacci(n-1)+fibonacci(n-2)
    return res

print(fibonacci(8))
print(fibonacci(13))
