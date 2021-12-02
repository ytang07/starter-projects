import math

def is_square(num: int):
    if math.sqrt(num).is_integer():
        return True
    return False

print(is_square(20))
print(is_square(100)) 
print(is_square(625))
print(is_square(1337))
print(is_square(2025))