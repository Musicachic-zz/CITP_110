# This program uses a loop to display a
# table of numbers and their squares.

def main():
    # Get the ending limit.
    end = int(input('How high should I go? '))
    
    # Print the table headings.
    print()
    print('Number\tSquare')
    print('--------------')

    # Print the numbers and their squares.
    for number in range(1, end + 1):
        square = number**2
        print(number, '\t', square)

# Call the main function.
main()

