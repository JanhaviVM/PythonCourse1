import sys
import random
from enum import Enum


def rps(name='PlayerOne'):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter...\n1 for Rock,\n2 or Paper, or\n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter a 1, 2 or 3")
            return play_rps()

        print("")
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"{name}, chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.")
        print("")

        def decide_winner(player, compter):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 It's a tie!"
            else:
                python_wins += 1
                return f"🐍 Python wins! Sorry, {name}... 😢"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s win Count: {player_wins}")
        print(f"\nPython win Count: {python_wins}")

        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes\nQ for Quit\n\n")
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break

        if playagain.lower() == 'y':
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉 ")
            print("Thank you for playing!\n")
            sys.exit(f" {name}! 👋")
            # or can use break

    return play_rps()


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    # only one arguement can be created at a time with the add_arguement function.
    # inside parser.add_arguement, we define the command line arguement that python will look for and accept when executed
    # --n or --name are the arguement flags, both refer to the same arguement being created.
    # metavar is what the display name is, incase you get a message that refers back to this arguement.
    # dest is the name for us to use across the code when referring to the arguement coming from args
    # required says when using the file, this argument needs to be provided.
    # help is shown incase you get a message that refers back to this arguement.
    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname",
        required=True, help="The name of the person playing the game"
    )

    # 'args' stores the values passed from the command line when running a script
    # then it processes them based on your definitons
    # then stores them inside variable names
    args = parser.parse_args()

    rock_papers_scissors = rps(args.firstname)
    rock_papers_scissors()
