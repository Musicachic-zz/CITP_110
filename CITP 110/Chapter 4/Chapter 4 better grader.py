# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Constants for the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

def main():
    # Get a test score from the user.
    score = int(input('Enter your test score: '))

    # Determine the grade.
    if score >= A_SCORE:
        print('Your grade is an A.')
    elif score >= B_SCORE:
        print('Your grade is a B.')
    elif score >= C_SCORE:
        print('Your grade is a C.')
    elif score >= D_SCORE:
        print('Your grade is a D.')
    else:
        print('Your grade is a F.')

# Call the main function.
main()
