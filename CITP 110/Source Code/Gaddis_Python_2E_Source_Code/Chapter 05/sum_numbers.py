# This program calculates the sum of a series
# of numbers entered by the user.

def main():
    # Initialize an accumulator variable.
    total = 0.0
    
    max = int(input("How many numbers will you add?: "))

    # Get the numbers and accumulate them.
    for counter in range(max):
        number = int(input('Enter a number: '))
        total = total + number

    # Display the total of the numbers.
    print('The total is', total)

# Call the main function.
main()

