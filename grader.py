def grader(score: float):
    if score > 90.0:
        return 'A'
    if score > 80.0:
        return 'B'
    if score > 70.0:
        return 'C'
    if score > 60.0:
        return 'D'
    else:
        return 'F'

print(grader(91.0))
print(grader(88.5))
print(grader(71))
print(grader(89.9))
print(grader(64))