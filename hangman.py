import random

# make a word list
wordlist = ["scary", "ginger", "sporty", "baby", "posh"]
# pick a word and show length
word = wordlist[random.randint(0, 4)]
blanks = "_"*len(word)
print(blanks)
# set up guesses and is found
strikes = 0
found = False
# take a letter as input
# check if the letter is in the word
while strikes < 5 and not found:
    guess = input("Guess a letter! ")
    if guess in word:
        index = word.find(guess)
        blanks = blanks[:index] + guess + blanks[index+1:]
    else:
        strikes += 1
        print(f"You have {strikes} strikes!")
    print(blanks)
    if "_" not in blanks:
        found = True