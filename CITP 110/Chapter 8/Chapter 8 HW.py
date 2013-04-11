#=====================================================================
# Program:      Homework Assignment #8
# Programmer:   Teresa Potts
# Date:         April 8, 2013
# Abstract:     This program creates a list containing names. The list of names 
#               will be printed, sorted, and printed again with the new sort order.
#               Then it is written to a new outfile file and then searched. 
#=====================================================================

# Define the main function.
def main():
    # Create a variable to control the loop.
    again = 'y'
    # Assign Names to use the output for the input_names function.
    Names = input_names()
    # Print a header for the unsorted names.
    print("Unsorted Names are as follows:")
    print("______________________________")
    # Call the print_name function.
    print_name(Names)
    print()
    print()
    # Assign Names to use the output for the sort_names function.
    Names = sort_names(Names)
    # Print a header for the sorted names.
    print("Sorted Names are as follows:")
    print("______________________________")
    # Call the print_name function.
    print_name(Names)
    print()
    print()
    # Call the output_names function.
    output_names(Names)
    # Show the user that the new file has been created.
    print("File newnames.txt has been created.")
    # Use a while loop to control whether or not to oo another search.
    while again.upper() == 'Y':
        # Call the search_names function.
        search_names(Names)
        # Get input from the user whether to do another search.
        again = input("Would you like to search for another name? Enter Y for Yes: ")
    # If the user does not want to continue show the user the program is ending.
    else:
        print("Ending the program")

# Define the input_names function.
def input_names():
    # Open a file for reading.
    infile = open('names.txt', 'r')

    # Read the contents of the file into a list.
    names = infile.readlines()

    # Close the file.
    infile.close()

    # Start at the first name in the file.
    index = 0
    # Create a while loop to iterate through the names in the file.
    while index < len(names):
        # Strip the \n from each element.
        names[index] = names[index].rstrip('\n')
        # Read each name in the file.
        index += 1

    # Return the contents of the list.
    return(names)

# Define the print_name function.
def print_name(Names):
    # Create a for loop for printing the Name output as defined in the main.
    for name in Names:
        print(name)

# Define the sort_names function.
def sort_names(Names):
    # Use the built in sort function.
    Names.sort()
    return Names

# Define the output_names function.
def output_names(Names):
    # Open a new file for writing.
    outfile = open("newnames.txt", "w")
    # Create a for loop for reading each name and adding a line break after each one.
    for name in Names:
        outfile.writelines(name + "\n")
        # Close the file.
    outfile.close()

# Define the search_names function.
def search_names(Names):
    # Assign the input from the user to be named search.
    search = input("Enter a name:")
    # Conditional statement if the input from the user is found in the file.
    if search in Names:
        # Display to the user that the name was found.
        print(search, "was found in the list.")
        # Display the location of the name in the index.
        print("It is located at position", Names.index(search) + 1)
    # If the name is not found, display it is not found on the list.
    else:
        print(search, "was not found in the list.")

# Call the main function.
main()