import random
random.seed(69)

seq = [random.randint(1, 100) for _ in range(10)]
print(seq)

"""Random Sample"""
print(random.sample(seq, 5))
seq2 = [2, 3, 4]
random.seed(10)
print(random.sample(seq2, 5, counts=[2, 3, 4]))
seq3 = [2, 2, 3, 3, 3, 4, 4, 4, 4]
random.seed(10)
print(random.sample(seq3, 5))

"""Random Choice"""
# print(random.choice(seq))

"""Random Choices"""
# weights = [random.randint(1, 10) for _ in range(10)]
# print(weights)
# cum_weights = [sum(weights[:i+1]) for i in range(10)]
# print(cum_weights)
# random.seed(1)
# print(random.choices(seq, weights=weights, k=5))
# random.seed(1)
# print(random.choices(seq, cum_weights=cum_weights, k=5))
# print(random.choices(seq, k=5))
# print(random.choices(seq))

"""Random Shuffle"""
# random.shuffle(seq)
# print(seq)
