#=====================================================================
# Program:      Homework Assignment #5B
# Programmer:   Teresa Potts
# Date:         Mar 14, 2013
# Abstract:     This program simulates a rock, paper, scissors game. 
#               You play against a computer using the random import in
#               the Python library.
#=====================================================================

# Import the random library from Python.
import random

# Create global variables to use for the accumulator. Start the values out as zero.
PLAYER_ACCUMULATOR = 0
COMPUTER_ACCUMULATOR = 0
TIE_ACCUMULATOR = 0

# The main function to run the program.
def main():
    # Describe what the program is designed to do to the user.
    print("This is a old fashioned rock, paper, scissors game. It is you versus the computer.\nUse 1 for rock. Use 2 for paper. Use 3 for scissors. \nGood Luck!")
    # Create a variable to control the loop. 
    again = 'y'
    # Play the game everytime the user wants to keep playing.
    while again == 'Y' or again =='y':
        # Call the play_game function.
        play_game()
        # Ask the user if they want to play the game again.
        again = input("Would you like to play again? (Enter Y for Yes): ")
    print("Thanks for playing.")
        
# Define the play_game function.
def play_game():

    # Get the players selection and show them what their choice is: rock, paper, or scissors.    
    players_choice = get_players_choice()
    if players_choice == 1:
        print("You have chosen rock.")
    elif players_choice == 2:
        print("You have chosen paper.")
    else:
        print("You have chosen scissors.")
    
    # Get the computers selection and show the user what the computer selected: rock, paper, or scissors.    
    computers_choice = get_computers_choice()
    if computers_choice == 1:
        print("Your competition has chosen rock.")
    elif computers_choice == 2:
        print("Your competition has chosen paper.")
    else:
        print("Your competition has chosen scissors.")
    
    # Call the function to determine the winner.
    winner = determine_the_winner(computers_choice, players_choice)
    # Return the output from the determine_the_winner function.
    return winner

# Define the get_computer_choice function.
def get_computers_choice():
    # Get a random integer between 1-3 for the computer's choice.
    computers_choice = random.randint(1,3)
    # Return the output from the computer_choice function.
    return computers_choice

# Define the get_players_choice function.
def get_players_choice():
    # Get the input from the user.
    players_choice = input("Enter value 1-Rock, 2-Paper, or 3-Scissors. ")

    # Display a error message if the user picks anything other than 1, 2, or 3.
    while players_choice not in ["1", "2", "3"]:
        print("Error: Please input value of 1, 2, or 3. ")
        players_choice = input("Enter value 1, 2, or 3. ")
        # Return the player's choice as an integer since it was looking for a string value.
    return int(players_choice)

# Define the determine_the winner function.
def determine_the_winner(computers_choice, players_choice):
    # If, elif, and else statements do comparisons on the values selected to determine who wins.
    if computers_choice == players_choice:
        # Show the user the outcome.
        print("Result is a tie!")
        # Use a global variable to start your accumulator.
        global TIE_ACCUMULATOR
        # Use an accumulator to keep track of ties. Add +1 if this condition is met.
        TIE_ACCUMULATOR += 1
    elif (computers_choice == 1 and players_choice == 3) or (computers_choice == 2 and players_choice == 1) or (computers_choice == 3 and players_choice == 2):
        # Show the user the outcome.
        print("Your competition wins!")
        # Use a global variable to start your accumulator.
        global COMPUTER_ACCUMULATOR
        # Use an accumulator to keep track of losses. Add +1 if this condition is met.
        COMPUTER_ACCUMULATOR += 1
    else:
        # Show the user the outcome.
        print("You win!")
        # Use a global variable to start your accumulator.
        global PLAYER_ACCUMULATOR
        # Use an accumulator to keep track of wins. Add +1 if this condition is met.
        PLAYER_ACCUMULATOR += 1
    
    # Print the users win-loss-tie record.
    print("Your W-L-T record is %d-%d-%d" % (PLAYER_ACCUMULATOR, COMPUTER_ACCUMULATOR, TIE_ACCUMULATOR))

# Call the main function.
main()