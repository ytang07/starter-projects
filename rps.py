import random

_dict = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

def generate():
    num = random.randint(0, 2)
    return _dict[num]

player = input("Rock, Paper, or Scissors? ").lower()
computer = generate()
if player == computer:
    print(f"Tie! You chose {player} and the computer chose {computer}")
elif player == "rock" and computer == "paper":
    print(f"Computer wins! You chose {player} and the computer chose {computer}")
elif player == "rock" and computer == "scissors":
    print(f"You win! You chose {player} and the computer chose {computer}")
elif player == "paper" and computer == "rock":
    print(f"You win! You chose {player} and the computer chose {computer}")
elif player == "paper" and computer == "scissors":
    print(f"Computer wins! You chose {player} and the computer chose {computer}")
elif player == "scissors" and computer == "rock":
    print(f"Computer wins! You chose {player} and the computer chose {computer}")
elif player == "scissors" and computer == "paper":
    print(f"You win! You chose {player} and the computer chose {computer}")