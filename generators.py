def sample_generator(i):
    for j in range(i):
        yield j
# for value in sample_generator(5):
#     print(value)

def yf_generator(i):
    yield from sample_generator(i)
# for value in yf_generator(5):
#     print(value)
    
f = sample_generator(6)
print(next(f))
print(next(f))