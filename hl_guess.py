import random

print("This program picks a random number between 1 and 100 and tells you if your guess is high or low until you guess it")
num = random.randint(1, 100)
guessing = True
while guessing:
    guess = int(input("What is your guess? "))
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        print("Nice, you got it!")
        guessing = False