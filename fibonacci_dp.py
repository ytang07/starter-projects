table = [-1 for _ in range(20)]

def fibonacci(n):
    if n == 0:
        table[0] = 0
        return 0
    if n == 1:
        table[0] = 0
        table[1] = 1
        return 1
    if table[n] != -1:
        return table[n]
    table[n] = fibonacci(n-1) + fibonacci(n-2)
    return table[n]

for i in range(20):
    print(fibonacci(i))