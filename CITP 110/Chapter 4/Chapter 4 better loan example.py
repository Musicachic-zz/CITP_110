def main():
    salary = float(input("Enter your annual salary: "))
    
    years_on_job = int(input("Enter the number of years employed: "))
    
    #Determine whether the customer qualifies.
    if salary >= 30000 and years_on_job >= 2:
        print("You qualify for the loan.")
            
    else:
        print("You do not qualify.")
                      
# Call the main function.
main()