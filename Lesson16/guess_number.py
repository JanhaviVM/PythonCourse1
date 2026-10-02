# planning the steps to write code
#
#
# # input accepting player name
# input accepting number
# CLI print asking user to enter either 1,2, and 3
# accept user input, check if valid, if valid accept input, else throw error
# generate a random number from 1, 2, and 3.
# set game count for that specific user name
# compare the user input number to randomly generated number
# if both numbers match, user/player wins. Store player win count
# take game count, player win count. get % of times player has won
# print game count, % of wins, for that specific user
# ask user if want to play again or quit


import argparse
import sys


def guess_number_game(name="PlayerOne"):

    game_count = 0
    player_wins = 0
    win_percentage = 0

    def play_guess_number_game():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        from random import choice

        while True:
            playernumber = input(
                f"\n{name} guess what number I'm thinking of... 1, 2, or 3.\n")
            if playernumber not in ['1', '2', '3']:
                continue
            else:
                break

        pythonnumber = choice("123")

        print(f"\n{name}, you chose {playernumber}")
        print(f"I was thinking about the number {pythonnumber}\n")

        def decide_winner(playernumber, pythonnumber):

            if playernumber == pythonnumber:
                nonlocal player_wins
                nonlocal win_percentage

                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time... 😢"

        game_result = decide_winner(playernumber, pythonnumber)
        print(game_result)

        game_count += 1

        print(f"Game Count: {game_count}")
        print(f"{name} wins: {player_wins}\n")
        print(f"Your winning percentage: {player_wins / game_count:.2%}")

        print(f"Play Again, {name}?")
        while True:
            playagain = input("Y for Yes or\nQ to Quit\n")
            if playagain.lower() not in ['y', 'q']:
                continue
            if playagain.lower() == 'y':
                return play_guess_number_game()
            else:
                print(f"\n🎉🎉🎉🎉 ")
                print(f"Thank you for playing!\n")
                if __name__ == "__main__":
                    sys.exit(f"Bye, {name}! 👋\n")
                else:
                    return

    return play_guess_number_game


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Game of guessing Number"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the person playing the game"
    )

    args = parser.parse_args()

    my_guess_number_game = guess_number_game(args.name)

    my_guess_number_game()
