# This program uses the return value of a function.

def main():
    first_age = int(input('Enter your age: '))
    second_age = int(input("Enter your best friend's age: "))

    # Get the sum of both ages.
    total = sum(first_age, second_age)

    # Display the total age.
    print('Together you are', total, 'years old.')

# The sum function accepts two numeric arguments and
# returns the sum of those arguments.
def sum(first_age, second_age):
    total = first_age + second_age
    return total

# Call the main function.
main()
