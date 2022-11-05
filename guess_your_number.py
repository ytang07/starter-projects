from random import randint

print("Think of a number between 1 and 100")
l = 1
h = 100
x = randint(l, h)
guessed = input(f"Is {x} higher, lower, or did we guess on point?(h, l, y) ")
while guessed != "y":
    if guessed == "l":
        l = x+1
    elif guessed == "h":
        h = x-1
    x = randint(l, h)
    guessed = input(f"How about {x}?(h, l, y) ")