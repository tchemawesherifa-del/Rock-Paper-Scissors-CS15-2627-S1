import random

def get_cpu_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        player_choice = input("rock, paper, or scissors: ").lower()

        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice

        print("that isn't a choice, try again")


def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        return "tie"

    if player_choice == "rock" and cpu_choice == "scissors":
        return "player"

    if player_choice == "paper" and cpu_choice == "rock":
        return "player"

    if player_choice == "scissors" and cpu_choice == "paper":
        return "player"

    return "cpu"


def play_round():
    player_choice = get_player_choice()
    cpu_choice = get_cpu_choice()

    print("you picked:", player_choice)
    print("cpu picked:", cpu_choice)

    winner = check_winner(cpu_choice, player_choice)

    if winner == "player":
        print("you won this round!")
    elif winner == "cpu":
        print("cpu won this round!")
    else:
        print("it's a tie!")

    return winner


player_wins = 0
cpu_wins = 0
ties = 0

while player_wins < 3 and cpu_wins < 3:
    print("\nnew round!")

    winner = play_round()

    if winner == "player":
        player_wins += 1
    elif winner == "cpu":
        cpu_wins += 1
    else:
        ties += 1

    print("score:")
    print("you:", player_wins)
    print("cpu:", cpu_wins)
    print("ties:", ties)

if player_wins == 3:
    print("\nyou won the tournament!")
else:
    print("\ncpu won the tournament!")