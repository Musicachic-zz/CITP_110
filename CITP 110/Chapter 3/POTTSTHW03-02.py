#===================================================================================================
# Program:      Homework Assignment #3B
# Programmer:   Teresa Potts
# Date:         01/29/2013
# Abstract:     This program will calcalate the amount telephone solicitors
#               are paid each week. It uses global constants for the hourly pay rate, commission
#               rate, and tax withholding rate. It takes the user's input of their sales amount and
#               hours worked to calculate the following: hourly pay amount, commission amount,
#               gross pay, tax withholding amount, and net pay.
#===================================================================================================


# Here are my global constants in this program.
HOURLY_PAY_RATE = 7.50
COMMISSION_RATE = 0.05
WITHHOLDING_RATE = 0.25

# The main function will perform the main logic of the program.
def main():
    display_message()
    name = input("What is your first name? ")
    sales_amount = float(input("What is your amount of total sales this week? "))
    hours_worked = float(input("What are your number of hours worked this week? "))
    print() 
    # I added space for a extra line here because I felt like it looked nicer 
    # for the user.
    hourly_pay_amt = hours_worked * HOURLY_PAY_RATE
    commission_amt = sales_amount * COMMISSION_RATE
    gross_pay_amt = hourly_pay_amt + commission_amt
    withholding_amt = gross_pay_amt * WITHHOLDING_RATE
    net_pay_amt = gross_pay_amt - withholding_amt
    display_results(hourly_pay_amt,commission_amt, gross_pay_amt, 
                    withholding_amt, net_pay_amt, name)

# This function will display a message to the user to explain what the program 
# will calculate for them.
def display_message():
    print("This program calculates the salesperson's pay.")
    print("Five values are displayed:")
    print("Hourly Pay, Commission, Gross Pay, Withholding, and Net Pay")
    print()
        
# This function will show the user the output of the results of the calculations
# from above. It will show them their hourly pay amount, commission amount, 
# gross pay amount, tax withholding amount, and net pay amount. I added their
# name that they input at the beginning of the main for more of a personal touch
# for the user.
def display_results(hourly_pay_amt,commission_amt, gross_pay_amt, 
                    withholding_amt, net_pay_amt, name):
    print(name,", your hourly pay is $", \
          format(hourly_pay_amt,',.2f'),\
          sep='')
    print(name, ", your commission amount is $", \
          format(commission_amt, ',.2f'),\
          sep='')
    print(name,", your gross pay amount is $", \
          format(gross_pay_amt, ',.2f'), \
          sep='')
    print(name, ", your withholding amount is $", \
          format(withholding_amt, ',.2f'), \
          sep='')
    print(name, ", your net pay amount is $", 
          format(net_pay_amt, ',.2f'), \
          sep='')
    
# Call the main function.    
main()