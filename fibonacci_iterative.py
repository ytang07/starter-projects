def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f

print(fibonacci(10))