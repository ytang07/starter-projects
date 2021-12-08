# lcm = x * y / gcd(x, y)
def gcd(x: int, y: int):
    if y == 0:
        return x
    return gcd(y, x%y)

def lcm_w_gcd(x: int, y: int):
    return int(x * y/gcd(x, y))

def iterative_lcm(x: int, y: int):
    if x < y:
        small = x
        big = y
    else:
        small = y
        big = x
    lcm = small
    while lcm % big != 0:
        lcm += small
    return lcm

print(lcm_w_gcd(27, 3)) # 27
print(lcm_w_gcd(15, 55)) # 105
print(lcm_w_gcd(21, 99)) # 693

print(iterative_lcm(27, 3)) # 27
print(iterative_lcm(15, 55)) # 105
print(iterative_lcm(21, 99)) # 693