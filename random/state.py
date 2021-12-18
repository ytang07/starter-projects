import random

"""Random State"""
x = random.getstate()
random.setstate(x)
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
random.setstate(x)
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
print(random.randint(1, 5))
print(len(x[1]))
print(len(x))

"""Random Seed"""
# random.seed(22)
# print(random.randint(1, 5))
# print(random.randint(1, 5))
# print(random.randint(1, 5))
# print(random.randint(1, 5))
# print(random.randint(1, 5))
