#=====================================================================
# Program:      Homework Assignment #8
# Programmer:   Teresa Potts
# Date:         April 15, 2013
# Abstract:     This program uses a pet class to help a user create a
#               list of pets. It asks for the pet's name, type, and
#               age. It then prints out the pets entered to the user.
#=====================================================================

import Pet

def main():
    again = "Y"
    # Get a list of Pet objects.
    pets = make_list()

    # Display the data in the list.
    print('Here is the data you entered:')
    print()
    pet_list(pets)

# The make_list function gets data from the user
# for five pets. The function returns a list
# of pet objects containing the data.

def make_list():
    # Create an empty list.
    pet_list = []

    # Add five pet objects to the list.
    print('Enter data for five pets.')
    for count in range(1, 6):
        # Get the pet's data.
        name = input("Enter the pet's name: ")
        while name == '':
            print("Error: Please enter the pet's name.")
            name = input("Enter the pet's name: ")
        animal_type = input('Enter the type of animal: ')
        while animal_type == '':
            print("Error: Please enter the animal type.")
            animal_type = input('Enter the type of animal: ')
        age = input("Enter the pet's age: ")
        while age == '' or age.isalpha():
            print("Error: Please enter the age.")
            age = input("Enter the pet's age: ")
        float(age)

        # Create a new Pet object in memory and
        # assign it to the pet variable.
        pets = Pet.Pet(name, animal_type, age)

        # Add the object to the list.
        pet_list.append(pets)

    # Return the list.
    return pet_list

# The display_list function accepts a list containing
# Pet objects as an argument and displays the
# data stored in each object.

def pet_list(pet_list):
    for item in pet_list:
        print(item.get_name())
        print(item.get_animal_type())
        print(item.get_age())
        print()

# Call the main function.
main()


