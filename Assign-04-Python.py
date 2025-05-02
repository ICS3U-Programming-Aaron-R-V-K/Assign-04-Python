# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 30, 2025
# Rolling dice game until doubles are rolled
# After rolling doubles, asks the user if they want to play again


import random
import time


def main():
    # Welcome message
    print("Welcome to the double dice game!")
    print("Roll the dice until you get doubles!\n")

    # Initialize the counter for games and rolls
    total_games = 0
    total_rolls = 0

    # Declare this variable to false, to end the whole program
    terminate_program = False

    # Outer loop for resetting the rolls after each game
    while True:
        # Reset the rolls to 0 after each game
        rolls = 0

        # Inner loop for rolling the dice until doubles
        while True:
            # Before rolling the dice, there is a small animation of shaking the dice
            for shake in range(3):
                print(" Shaking the dice...")
                # It will print that three times, but it will wait 0.3 sec after it prints it for three times
                time.sleep(0.3)

            # Generate the random numbers from 1 to 6
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)

            # Add one roll after shaking the dice
            rolls += 1
            # Display the current roll and the random numbers it generated for the dice
            print(f"Roll {rolls}: {die1} and {die2}")

            # Compare both dice, and if they are doubles, it will exit this loop, if it is not equal, it will loop the program until it gets doubles
            if die1 == die2:
                print(f"Doubles rolled after {rolls} attempts!\n")
                # break to exit the loop
                break

        # After finishing one game add one to the total games and add the number of rolls it took to the total rolls
        total_games += 1
        total_rolls += rolls

        # Ask the user if they want to play again
        while True:
            # Ask the user if they want to do it again and use .lower to accept input in lower or upper case
            again = input("Roll again? (yes/y to continue, no/n to stop): ").lower()
            if again == "yes" or again == "y":
                break  # Break this small input loop, start new game
            # elif, if the user says no it will display the game summary

            elif again == "no" or again == "n":
                # Exit the big game loop
                print("\nThank you for playing!")

                # Calculate final stats
                chance_of_doubles = (total_games / total_rolls) * 100
                average_rolls_per_game = total_rolls / total_games

                # Display the final stats
                print("\n GAME SUMMARY ")
                print(f"Total games played: {total_games}")
                print(f"Total rolls made: {total_rolls}")
                print(f"Chance of rolling doubles per roll: {chance_of_doubles:.2f}%")
                print(f"Average rolls per game: {average_rolls_per_game:.2f}")

                # After ending the program set the variable to True
                terminate_program = True
                # Break so you exit the loop from asking if they want to keep playing
                break

            # else statement if Invalid input from the user
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        # If statement to exit the whole program
        if terminate_program == True:
            break


if __name__ == "__main__":
    main()
