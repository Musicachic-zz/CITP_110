#=====================================================================
# Program:      Homework Assignment #5B
# Programmer:   Teresa Potts
# Date:         Feb 20, 2013
# Abstract:     This program calculates an average sales amount,
#               highest sales amount, and lowest sales amount
#               for sales people at a used car dealership. The calculation
#               is based on the following input: their first sale amount,
#               subsequent sales amounts, and their number of sales.
#=====================================================================

def main():
    # Create a variable to control the loop
    keep_going = 'y'

    # Create a counter for salespeople
    number_of_salespeople = 0

    # Process each saleperson's first sales amount
    while keep_going == 'y' or keep_going == 'Y':

        # Use a function to process each salesperson
        process_salesperson()

        number_of_salespeople += 1

        # Ask if there are more salespeople?
        keep_going = input('Are there more salespeople? (enter y for yes): ')

    # Display the total number of salespeople
    print()
    if number_of_salespeople <= 1:
        print('There is', number_of_salespeople, 'salesperson today.')
    
    else:
        print('There are', number_of_salespeople, 'salespeople today.')

# Process each salesperson's sale amounts
def process_salesperson():
    # Get the salesperson's name
    print()
    name = input("What is the salesperson's name? ")

    # Input the first sales amount
    print('Enter', name + "'s amount for the first sale: ", end = ''),
    first_sales_amount = float(input())

    # Validate the sales amount is > 0
    while first_sales_amount <= 0 or first_sales_amount >= 25000:
        print("ERROR: The sales amount must be greater than $0, but less than $25,000.")
        first_sales_amount = float(input("Please enter a correct sales amount: "))

    # Initialize total, lowest, and highest sales amounts to first sales amount
    total_amount = first_sales_amount
    lowest_sales_amount = first_sales_amount
    highest_sales_amount = first_sales_amount

    # Get the number of sales for this salesperson
    print('How many sales did', name, 'make? ', end = '')
    number_of_sales = int(input())

    for number in range(2, number_of_sales + 1):
        # Get the next sales amount
        print('Enter', name + "'s amount for sale #" + str(number) + ': ', end = ''),
        sales_amount = float(input())

        # Validate the sales amount is > 0
        while sales_amount <= 0 or sales_amount >= 25000:
            print("ERROR: The sales amount must be greater than $0, but less than $25,000.")
            sales_amount = float(input("Please enter a correct sales amount: "))

        # Accumulate the sales
        total_amount += sales_amount

        # Check for highest sales amount
        if sales_amount > highest_sales_amount:
            highest_sales_amount = sales_amount

        # Check for lowest sales amount
        elif sales_amount < lowest_sales_amount:
            lowest_sales_amount = sales_amount

    # Compute the average sales amount
    average_sales_amount = float(total_amount) / number_of_sales

    # Display the average, highest, and lowest sales amounts
    print()
    print(name + "'s average sales amount was $: ", format(average_sales_amount, "6.2f"), sep='')
    print(name + "'s highest sales amount was $: ", format(highest_sales_amount, "6.2f"), sep='')
    print(name + "'s lowest sales amount was $: ", format(lowest_sales_amount, "6.2f"), sep='')
    print()

# Call the main function
main()