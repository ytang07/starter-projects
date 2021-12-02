def prime_factorization(num: int):
    # deal with edge cases
    if num == 1:
        return [1]
    # set up empty list of factors
    factors = []
    # start at 1
    n = 2
    # factor up to sqrt num - there's no prime factors
    # above the sqrt of a number
    while n**2 <= num:
        # check if the number is divisible by the factor
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    # if we have a number greater than 1 at the end
    # that number is a prime factor
    if num > 1:
        factors.append(num)
    
    return factors

print(prime_factorization(225))
print(prime_factorization(1776))
print(prime_factorization(2012))
print(prime_factorization(893))
print(prime_factorization(7392))