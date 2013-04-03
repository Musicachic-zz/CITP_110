PAY_RATE = 40
def main():
    # Get the number of hours worked.
    hours = int(input('Enter the hours worked this week: '))

    # Calculate the gross pay.
    gross_pay = hours * PAY_RATE

    # Display the gross pay.
    print('Gross pay: $', format(gross_pay, ',.2f'))

# Call the main function.
main()
