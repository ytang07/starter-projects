# euclidean algorithm
def iterative_gcd(x: int, y: int):
    while(y):
        if x == 1 or y == 1:
            return 1
        x, y = y, x%y
    return x

def recursive_gcd(x: int, y: int):
    if y == 0:
        return x
    if x == 1 or y == 1:
        return 1
    return recursive_gcd(y, x%y)

print(iterative_gcd(10, 20)) # 10
print(iterative_gcd(33, 41)) # 1
print(iterative_gcd(48, 64)) # 16
print(iterative_gcd(99, 81)) # 9
print(iterative_gcd(210, 70)) # 70

print(recursive_gcd(10, 20)) # 10
print(recursive_gcd(33, 41)) # 1
print(recursive_gcd(48, 64)) # 16
print(recursive_gcd(99, 81)) # 9
print(recursive_gcd(210, 70)) # 70