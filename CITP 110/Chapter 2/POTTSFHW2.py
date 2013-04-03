#==================================================================
# Program:      Convert
# Programmer:   Teresa Potts
# Date:         01/23/2013
# Abstract:     This program converts the number of gallons entered
#               to its equivalent in quarts and liters which are
#               displayed as output.
#==================================================================

# get input from the user
gallons = int(input('How many gallons?  '))

# do the conversions
quarts = gallons * 4
liters = gallons * 3.785

# display the output to the user
print('The number of quarts in', gallons, 'gallons is', quarts)
print ('The number of liters in', gallons, 'gallons is', liters)
print("Thanks for playing")
