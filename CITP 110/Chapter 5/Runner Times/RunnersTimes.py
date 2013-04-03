#=====================================================================
# Program:      Runners Example
# Programmer:   Gary Heisler
# Date:         February 4, 2009
#               July 1, 2011 - Revised for Python 3
# Abstract:     This program processes a group of runners.
#               Each runner may run a different number of laps.
#               After each runner's lap times have
#               been entered, the program displays their average,
#               longest, and shortest lap times.
#=====================================================================

def main():
    # create a variable to control the loop
    keep_going = 'y'

    # create a counter for runners
    number_of_runners = 0

    # process each runner's lap times
    while keep_going == 'y' or keep_going == 'Y':

        # use a function to process each runner
        process_runner()

        number_of_runners += 1

        # are there more runners?
        keep_going = input('Are there more runners? (enter y for yes): ')

    # display the total number of runners
    print()
    print('There were', number_of_runners, 'runners today.')

# process each runer's lap times
def process_runner():
    # get the runner's name
    print()
    name = input("What is the runner's name? ")

    # input the first lap time
    print('Enter', name + "'s time for the first lap: ", end = ''),
    first_lap_time = float(input())
    
    # validate the lap time is > 0
    while first_lap_time <= 0:
        print("ERROR: the lap time must be > 0.")
        first_lap_time = float(input("Please enter a correct lap time: "))

    # intialize total, shortest, and longest lap times to first lap time
    total_time = first_lap_time
    shortest_lap_time = first_lap_time
    longest_lap_time = first_lap_time
    
    # get the number of laps for this runner
    print('How many laps did', name, 'run? ', end = '')
    number_of_laps = int(input())

    for number in range(2, number_of_laps + 1):
        # get the lap time
        print('Enter', name + "'s time for lap #" + str(number) + ': ', end = ''), 
        lap_time = float(input())

        # validate the lap time is > 0
        while lap_time <= 0:
            print("ERROR: the lap time must be > 0.")
            lap_time = float(input("Please enter a correct lap time: "))

        # accumulate the scores
        total_time += lap_time

        # check for longest lap time
        if lap_time > longest_lap_time:
            longest_lap_time = lap_time

        # check for shortest lap time
        elif lap_time < shortest_lap_time:
            shortest_lap_time = lap_time

    # compute average lap time
    average_lap_time = float(total_time) / number_of_laps

    # display the average, longest, and shortest lap times
    print()
    print(name + "'s average lap time was: \t", format(average_lap_time, "6.2f"))
    print(name + "'s longest lap time was: \t", format(longest_lap_time, "6.2f"))
    print(name + "'s shortest lap time was: \t", format(shortest_lap_time, "6.2f"))
    print()

# call the main function
main()