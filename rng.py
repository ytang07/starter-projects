import random

print("This program generates a random number between two given numbers")
low = int(input("What is the lower limit? "))
high = int(input("What is the higher limit? "))
num = random.randint(low, high)
print(f"Your randomly generated number is: {num}")
