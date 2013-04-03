# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

# Global constants
START = 60
END = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

def main():
    # Print the table headings.
    print('KPH\tMPH')
    print('--------------')

    # Print the speeds.
    for kph in range(START, END, INCREMENT):
        mph = kph * CONVERSION_FACTOR
        print(kph, '\t', format(mph, '.1f'))

# Call the main function.
main()
