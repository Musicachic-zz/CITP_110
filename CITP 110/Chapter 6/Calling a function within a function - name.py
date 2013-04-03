# This program uses the return value of a function.

def main():
    first_name, last_name = get_name()
    print("Your full name is:", first_name, last_name)
    
def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

# Call the main function.
main()