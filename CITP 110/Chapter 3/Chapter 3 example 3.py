PAY_RATE = 25.65

def main():
    display_message()
    hours = int(input("Enter the hours "))
    # pay_rate = float(input("Enter the pay rate "))
    gross_pay = hours * PAY_RATE
    display_results(gross_pay, hours)

def display_message():
    print("This program will help you calculate your gross pay")
    print("using your input of hours and pay rate")
    print()

def display_results(gross_pay, hours):
    print("Hours:", hours)
    print("Your gross pay: $", format(gross_pay, ".2f"))




main ()
