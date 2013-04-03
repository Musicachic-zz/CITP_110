# This program simulates the rolling of dice.
import random

def main():
    # Create a variable to control the loop.
    again = 'y'

    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice... Their values are...')
        print(random.randint(1, 6))
        print(random.randint(1, 6))

        # Do another roll of the dice?
        again = input('Roll them again? (y = yes): ')

# Call the main function.
main()
