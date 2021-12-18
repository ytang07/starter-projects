import random

print(f"Sample from basic random distribution from 0 to 1: {random.random()}")
print(f"Uniform Random Sample from 2 to 4: {random.uniform(2, 4)}")
print(f"Triangle Random Sample from 1 to 10 with a mode of 8: {random.triangular(1, 10, 8)}") #defaults to 0, 1, 0.5
print(f"Sample from the Beta distribution alpha=1, beta=2: {random.betavariate(1, 2)}") #a, b > 0
print(f"Sample from exponential distribution with a mean of 1/9: {random.expovariate(9)}") #parameter != 0
print(f"Sample from Gamma distribution with alpha=1, beta=2: {random.gammavariate(1, 2)}") #a, b > 0
print(f"Sample from Gaussian (Normal) with mean 1 and standard deviation 0.1: {random.gauss(1, 0.1)}") #not-thread-safe but faster version of normalvariate
print(f"Sample from Log Normal Distribution with mean 1 and standard deviaiton 0.1: {random.lognormvariate(1, 0.1)}") #the exponential of the normal around a, b
print(f"Sample from Normal Distribution with mean 1 and standard deviation 0.1: {random.normalvariate(1, 0.1)}") #normal distribution
print(f"Sample from von Mises/circular Normal Distribution with mean ~pi, concentration 0.1: {random.vonmisesvariate(3.14, 0.1)}") #a, b are angle and concentration, b=0 gives uniform random angle
print(f"Sample from Pareto distribution with shape 1: {random.paretovariate(1)}") #a is the shape parameter
print(f"Sample from Weibull distribution with scale 2 and shape 3: {random.weibullvariate(2, 3)}") #a is the scale, b is the shape 