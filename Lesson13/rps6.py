import sys
import random
from enum import Enum


def rps():

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "Enter...\n1 for Rock,\n2 or Paper, or\n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter a 1, 2 or 3")
            return play_rps()

        print("")
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"You chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.")
        print("")

        def decide_winner(player, compter):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 It's a tie!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer win Count: {str(player_wins)}")
        print(f"\nPython win Count: {str(python_wins)}")

        print("\nPlay again")
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
            sys.exit("Bye! 👋")
            # or can use break

    return play_rps()


play = rps()

play()
