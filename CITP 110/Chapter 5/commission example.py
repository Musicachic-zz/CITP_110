# This program calculates sales commissions.
COMM_RATE = .05

def main():
    # Create a variable to control the loop.
    keep_going = 'y'

    # Calculate a series of commissions.
    while keep_going == 'y':
        sales = float(input('Enter the amount of sales: '))
        commission = sales * COMM_RATE

        print('The commission is $', format(commission, ',.2f'), sep='')
        
        keep_going = input('Enter y to calculate another rate: ')
        


# Call the main function.
main()
