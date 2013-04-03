
TAX_FACTOR = 0.0065

# The main function.
def main():
    # Get the first lot number.
    print('Enter the property lot number or enter 0 to end.')
    lot = int(input('Lot number: '))

    while lot != 0:
        show_tax()

        print('Enter the next lot number or enter 0 to end.')
        lot = int(input('Lot number: '))

def show_tax():
    value = float(input('Enter the property value: '))
    tax = value * TAX_FACTOR

    print('Property tax: $', format(tax, ',.2f'), sep='')

# Call the main function.
main()


