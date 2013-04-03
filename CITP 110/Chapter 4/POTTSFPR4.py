#===================================================================================================
# Program:      Homework Assignment #4B
# Programmer:   Teresa Potts
# Date:         02/13/2013
# Abstract:     This program is a basic banking program. It will allow users to do a withdrawal or
#               deposit after it gets input on what the users previous balance was and determines if
#               there is enough funds in the account to do so. It also will handle a use case where
#               the user puts in a value other than doing a withdrawal or deposit and provide an
#               error message.
#===================================================================================================


# The main function will perform the main logic of the program.
def main():
    
    # These statements gets inputs from the user that we will display and use in calculations.
    name = input("What is your name? ")
    account_id = input("What is your account ID? ")
    transaction_code = input("What is your transaction code? Note: Enter W or w for withdrawal and D or d for deposit. ")
    previous_balance = float(input("What is your previous balance? "))
    transaction_amount = float(input("What is your desired transaction amount? "))
    
    # This if condition allows for a user to do a withdrawl. It calls the process_withdrawal function.
    if transaction_code == "W" or transaction_code == "w":
        process_withdrawal(name, account_id, transaction_code, transaction_amount, previous_balance)
    
    # This elif condition allows for a user to do a deposit. It calls the process_deposit function.
    elif transaction_code == "D" or transaction_code == "d":
        process_deposit(name, account_id, previous_balance, transaction_code, transaction_amount)
     
    # This else condition takes the user here if they do not meet the previous if or elif condition.
    # It calls the process_invalid_transaction function.
    else:
        process_invalid_transaction(name, account_id, previous_balance)
    
# This function takes the user through the process of processing a withdrawal.    
def process_withdrawal(name, account_id, transaction_code, transaction_amount, previous_balance):
    
    # This if condition will handle if the person does not have enough funds in their account to do
    # a withdrawal.
    if transaction_amount > previous_balance:
        print("Withdrawal exceeds previous balance. ")
        new_balance = previous_balance
        print_balance(name, account_id, new_balance)
    
    # This else condition will allow a person to do a withdrawal since they did not meet the prior 
    # if condition in this function.
    else:
        new_balance = previous_balance - transaction_amount
        print_balance(name, account_id, new_balance)
    
# This function takes the user through the proces of procesing a deposit.         
def process_deposit(name, account_id, transaction_code, previous_balance, transaction_amount):
    new_balance = previous_balance + transaction_amount
    print_balance(name, account_id, new_balance)

# This function takes the user to a error message if they type invalid input for doing a withdrawal
# or a deposit.
def process_invalid_transaction(name, account_id, previous_balance):
    print("Invalid transaction type")
    new_balance = previous_balance
    print_balance(name, account_id, new_balance)
        
# This function will show the user a message using their input of their name and account id. It will
# then calculate their new balance based on the transaction type they were trying to do. If the
# transaction can be processed it will display be a new balance. If the transaction cannot be processed
# it will display the previous balance to the user.
def print_balance(name, account_id, new_balance):
    print("Hello", name)
    print("Your account ID is", account_id)
    print("Your new balance is $",
          format(new_balance, ',.2f'), \
          sep='')

# Call the main function.         
main ()
