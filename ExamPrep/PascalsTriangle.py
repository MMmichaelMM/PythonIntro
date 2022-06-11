# Print Pascal's Triangle in Python


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)


def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            # for left spacing
            print(end=' ')
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=' ')
        # for new line
        print()


pascal_triangle(8)
