# This program calculates sales commissions.
COMM_RATE = .05
def main():
    # Create a variable to control the loop.
    keep_going = 'y'

    # Calculate a series of commissions.
    while keep_going == 'y':
        show_commission()
        
        # See if the user wants to do another one.
        keep_going = input('Enter y to calculate another: ')

def show_commission():
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    # Calculate the commission.
    commission = sales * COMM_RATE

    # Display the commission.
    print('The commission is $', format(commission, ',.2f'), sep='')

# Call the main function.
main()

