import sys
import random
from enum import Enum
# value = input('please enter a value: \n')

# print(value)
game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS(2))  # RPS.PAPER
    # # prints RPS.PAPER in terminal on run
    # print(RPS.ROCK)  # RPS.ROCK
    # print(RPS['ROCK'])  # RPS.ROCK
    # print(RPS.ROCK.value)  # 1
    # sys.exit()

    print("")
    playerchoice = input(
        "Enter...\n1 for Rock,\n2 or Paper, or\n3 for Scissors\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter a 1, 2 or 3")
        return play_rps()

    print("")
    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    def decide_winner(player, compter):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 It's a tie!"
        else:
            return "🐍 Python wins!"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1

    print("\nGame Count: " + str(game_count))

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


play_rps()
