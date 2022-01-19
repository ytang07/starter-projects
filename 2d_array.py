example_2d = [[1, 2], [3, 4], [5, 6]]

example_1d = [1, 2, 3]

print(sum(sum(example_2d, [])))
print(sum(example_2d, []))
print(sum([sum(x) for x in example_2d]))

_sum=0
for x in example_2d:
    _sum += sum(x)
print(_sum)

sum(example_2d)