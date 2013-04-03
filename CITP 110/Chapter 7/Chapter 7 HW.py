#=====l================================================================
# Program:      Homework Assignment #7
# Programmer:   Teresa Potts
# Date:         Mar 20, 2013
# Abstract:     This program calculates the amount due for sales of 
#               CD-RWs and DVD-RWs (using the code "C" or "c" for CD-RWs
#               and "D" or "d" for DVD-RWs) based on the amount bought per
#               person. It also calculates a total amount of product sold.
#=====================================================================

# Define some global constants.
CD_RW_PRICE = 16.50
DVD_RW_PRICE = 21.75

# Define the main function.
def main():
    
    # Initialize counters and payment total.
    cd_rw_counter = 0
    dvd_rw_counter = 0
    payment_due_counter = 0
    
    print("Name \t\t\tCode\t\tSpindles\tPayment Due")
    print
    
    try:
        # Open the data file.
        infile = open("disks.txt", "r")
        
        name = infile.readline()
        
        # Continue reading the file to the end.
        while name != "":
            
            # Strip the new line character and print the buyer's name.
            name = name.rstrip("\n")
            print(name, end="\t\t")
            
            # Read the code, strip the new line, and print it.
            code = infile.readline()
            code = code.rstrip("\n")
            print(code, end="\t\t")
            
            # Read the number of spindles, strip the new line, and print it.
            spindles = infile.readline()
            spindles = int(spindles)
            print(format(spindles, "3.0f"), end="\t\t")
            
            # Check the code type and compute the payment amount due
            # and increment the appropriate counter.
            if code =="C" or code=="c":
                payment_due = spindles * CD_RW_PRICE
                cd_rw_counter += 1
            elif code == "D" or code =="d":
                payment_due = spindles * DVD_RW_PRICE
                dvd_rw_counter += 1
            else:
                payment_due = 0
            
            # Accumulate the payment amount due per person.
            payment_due_counter += payment_due
            
            # Print the appropriate detail line. 
            if payment_due == 0:
                print("Invalid Code")
            else:
                print("$", format(payment_due, "8,.2f"))
            
            # Get the name of next the customer.  
            name = infile.readline()
        
        # Close the input file.    
        infile.close()

        # Print the counters and payment total amount.
        print()
        print("Total number of CDs sold: ", cd_rw_counter)
        print("Total number of DVDs sold: ", dvd_rw_counter)
        print("Total payment due: ", end="")
        print("$", format(payment_due_counter, ",.2f"))
    
    # Display an error if the file cannot be opened or found.
    except IOError:
        print("An error occurred trying to open or read disks. ")
        
# Call the main function.
main()        
