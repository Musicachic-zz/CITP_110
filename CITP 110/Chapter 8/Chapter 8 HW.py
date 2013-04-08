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
    again = 'y'
    Names = input_names()
    print("Unsorted Names are as follows:")
    print("______________________________")
    print_name(Names)
    print()
    print()
    Names = sort_names(Names)
    print("Sorted Names are as follows:")
    print("______________________________")
    print_name(Names)
    print()
    print()
    output_names(Names)
    print("File newnames.txt has been created.")
    while again == 'Y' or again == 'y':
        search_names(Names)
        again = input("Would you like to search for another name? Enter y: ")
    else:
        print("Ending the program")

def input_names():
# Open a file for reading.
    infile = open('names.txt', 'r')

    # Read the contents of the file into a list.
    names = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    index = 0
    while index < len(names):
        names[index] = names[index].rstrip('\n')
        index += 1

        # Print the contents of the list.
    return(names)

def print_name(Names):
    for name in Names:
        print(name)

def sort_names(Names):
    Names.sort()
    return Names

def output_names(Names):
    outfile = open("newnames.txt", "w")
    for name in Names:
        outfile.writelines(name + "\n")
    outfile.close()

def search_names(Names):

    search = input("Enter a name:")
    if search in Names:
        print(search, "was found in the list.")
        print("It is located at position", Names.index(search)+1)
    else:
        print(search, "was not found in the list.")

# Call the main function.
main()

