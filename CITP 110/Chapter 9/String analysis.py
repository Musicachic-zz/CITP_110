# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')

    # Test the string.
    if user_string.isdigit():
        print('The string contains only digits.')
    elif user_string.isalnum():
        print("The string contains alpha and numeric.")
    else:
        print("Nothing special here.")

main()
