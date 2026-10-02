# main module
#
# import both modules
# ask user to input 1,2 or letter x
# display arcade menu
# inside it display two options 1, and 2
# if user selects 1, execute rps.py
# if user selects 2, execute guess_number.py
#
# if user quits, display arcade menu again
# if user exits, do sys.exit()

import argparse
import rps
import guess_number
import sys


def play_arcade(name):
    print(f"\n{name}, welcome to the Arcade! 🤖\n")
    while True:
        gamechoice = input(
            f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to Exit the Arcade\n\n")
        if gamechoice.lower() not in ["1", "2", "x"]:
            continue
        elif gamechoice.lower() == "1":
            play_rps = rps.rps(args.name)
            play_rps()
            print(f"\n{name}, welcome back to the Arcade Menu! 🤖\n")
        elif gamechoice.lower() == "2":
            play_guess_number = guess_number.guess_number_game(args.name)
            play_guess_number()
            print(f"\n{name}, welcome back to the Arcade Menu! 🤖\n")
        else:
            print(f"Thank you for playing {name},\nSee you next time!👋\n")
            sys.exit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Arcade Game Menu"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="Name of the Player"
    )

    args = parser.parse_args()

    my_arcade = play_arcade(args.name)

    my_arcade()
