# This program calculates retail prices.

# MARK_UP is used as a global constant for
# the markup up percentage.
MARK_UP = 2.5

# The main function
def main():
    # Variable to control the loop.
    another = 'y'

    # Process one or more items.
    while another == 'y' or another == 'Y':
        # Display an item's retail price.
        show_retail()

        # Do this again?
        another = input('Do you have another item? ' + \
                        '(Enter y for yes): ')
        
# The show_retail function gets an item's wholesale
# cost and displays the item's retail price.
def show_retail():
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's " + \
                            "wholesale cost: "))

    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct ' + \
                                'wholesale cost:'))

    # Calculate the retail price.
    retail = wholesale * MARK_UP

    # Display the retail price.
    print('Retail price: $', format(retail, ',.2f'))

# Call the main function.
main()
