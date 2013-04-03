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

#player_accumulator = 0
#computer_accumulator = 0
#tie_accumulator = 0

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
        #print(player_total, '-', computer_total, '-', tie_total)
        
# Define the play_game function.
def play_game():
    players_choice = get_players_choice()
    if players_choice == 1:
        print("You have chosen rock.")
    elif players_choice == 2:
        print("You have chosen paper.")
    else:
        print("You have chosen scissors.")
        
    computers_choice = get_computers_choice()
    
    if computers_choice == 1:
        print("Your competition has chosen rock.")
    elif computers_choice == 2:
        print("Your competition has chosen paper.")
    else:
        print("Your competition has chosen scissors.")
    winner = determine_the_winner(computers_choice, players_choice)
    return winner

def get_computers_choice():
    choice = random.randint(1,3)
    return choice

def get_players_choice():
    choice = input("Enter value 1-Rock, 2-Paper, or 3-Scissors. ")

    while choice not in ["1", "2", "3"]:
        print("Error: Please input value of 1, 2, or 3. ")
        choice = input("Enter value 1, 2, or 3. ")
    return choice

def determine_the_winner(computers_choice, players_choice):
    if computers_choice == players_choice:
        print("Result is a tie!") 
        #tie_total = tie_accumulator + 1
    elif computers_choice == 1 and players_choice == 3 or computers_choice == 2 and players_choice == 1 or computers_choice == 3 and players_choice == 2:
        print("Your competition wins!")
        #computer_total = computer_accumulator + 1
    else:
        print("You win!")
        #player_total = player_accumulator + 1


main()