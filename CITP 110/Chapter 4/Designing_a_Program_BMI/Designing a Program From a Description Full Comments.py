#-------------------------------------------------------------------------------
#Program:       Designing a Program From a Desciption - BMI
#Programmer:    Gary Heisler
#Date:          9/1/2010
#               7/1/2011 - Revised for Python 3
#Abstract:      This program calculates the body mass index (BMI) for a user
#               and determines if the BMI indicates the user is underweight, 
#               overweight, or of optimal weight. 
#-------------------------------------------------------------------------------

#Define the main function
def main():
    #display the purpose of this program
    print('This program calculates your BMI using your weight and height')
    
    #input the user's weight in pounds and height in inches
    weight = float(input('What is your weight (in pounds)? '))
    height = float(input('What is your height (in inches)? '))
    
    #call the function to compute the user's body mass index (BMI)
    calculate_BMI(weight, height)
    
#Define the calculate_BMI function
def calculate_BMI(weight, height):
    
    #calculate the BMI using the formula and display the result
    BMI = weight * 703 / height ** 2
    print('Your BMI is ', format(BMI, '.2f'))
    
    #check to see if user is underweight (BMI < 18.5) and display message
    if BMI < 18.5:
        print('You are underweight')
    #check to see if user is overweight (BMI > 25) and display message
    elif BMI > 25:
        print('You are overweight')
    #otherwise, the user's weight is optimal and display message
    else:
        print('Your weight is optimal')
        
#call the main function
main()