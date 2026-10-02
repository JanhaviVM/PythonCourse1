import sys
import random
from enum import Enum
# value = input('please enter a value: \n')

# print(value)


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

print("")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 It's a tie!")
else:
    print("🐍 Python wins!")

print("")
