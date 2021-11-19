import random

_dict = {
    -1: "rock",
    0: "paper",
    1: "scissors"
}

def generate():
    num = random.randint(-1, 1)
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