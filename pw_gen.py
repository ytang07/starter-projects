import random
import string

def pw_gen(length, lower=True, upper=True, digits=True, punctuation=True):
    char = ""
    if lower:
        char += string.ascii_lowercase
    if upper:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    if punctuation:
        char += string.punctuation
    
    return ''.join(random.choice(char) for i in range(length))

_length = int(input("How long do you want your password to be? "))
adjust = input("Do you want to customize your password parameters?(y/n) ")
if adjust == "y":
    _lower = input("Do you want to include lowercase letters?(y/n) ").lower()
    _upper = input("Do you want to include upper case letters?(y/n) ").lower()
    _digits = input("Do you want to include digits?(y/n) ").lower()
    _punc = input("Do you want to include punctuation?(y/n) ").lower()
    lower = True if _lower == "y" else False
    upper = True if _upper == "y" else False
    digits = True if _digits == "y" else False
    punc = True if _punc == "y" else False
    print(pw_gen(_length, lower, upper, digits, punc))
else:
    print(pw_gen(_length))
