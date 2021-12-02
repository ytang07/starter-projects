# for a list of numbers find the longest monotonically increasing subsequence
t1 = [0, 4, 3, 2, 6, 7, 9] # 2, 6, 7, 9
t2 = [0, 1, 3, 2] # 0, 1, 3
t3 = [8, 5, 4, 1] # 8
t4 = [3, 5, 2, 7, 9, 10, 1] # 2, 7, 9, 10
t5 = [6, 5, 3, 1, 8] # 1, 8
t6 = [6, 6, 9, 10, 11, 0] # 6, 6, 9, 10, 11

def lis(_list):
    longest = [_list[0]]
    current = [_list[0]]
    for i in _list[1:]:
        if i >= current[-1]:
            current.append(i)
        else:
            if len(longest) < len(current):
                longest = current
            current = [i]
    if len(longest) < len(current):
                longest = current
    return longest

print(lis(t1))
print(lis(t2))
print(lis(t3))
print(lis(t4))
print(lis(t5))
print(lis(t6))