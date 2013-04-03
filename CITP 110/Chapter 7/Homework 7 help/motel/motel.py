#==================================================================
# Program:      motel
# Programmer:   Gary Heisler
# Date:         April 20, 2008
#               July 1, 2011 - Revised for Python 3
# Abstract:     This program calculates the amount due for motel room
#               rentals based upon the type of room (D or d = double,
#               Q or q = queen, and K or k = king) and the number  
#               of nights the guest is staying.
#==================================================================

DOUBLE_ROOM_RATE = 80
QUEEN_ROOM_RATE = 89
KING_ROOM_RATE = 105

def main():

    # initialize counters and total tuition
    double_room_counter = 0
    queen_room_counter = 0
    king_room_counter = 0
    total_room_rent = 0

    print("Guest Name \tType\tNights\tAmount Due")
    print

    try:
        # open the data file
        infile = open('motel.txt', 'r')

        # read the first value from the file
        guest_name = infile.readline()

        # continue reading from file until the end
        while guest_name != '':

            # strip the new line character and print the guest's name
            guest_name = guest_name.rstrip('\n')
            print(guest_name, end='\t')

            # read the room type, strip the new line, and print it
            room_type = infile.readline()
            room_type = room_type.rstrip('\n')
            print(room_type, end='\t')

            # read the number of nights, strip the new line, and print it
            nights = infile.readline()
            nights = int(nights)
            print(format(nights, '3.0f'), end='\t')

            # check the room type and compute the rental amount due 
            # increment the appropriate counter
            if room_type == "D" or room_type == "d":
                payment_due = nights * DOUBLE_ROOM_RATE
                double_room_counter += 1
            elif room_type == "Q" or room_type == "q":
                payment_due = nights * QUEEN_ROOM_RATE
                queen_room_counter += 1
            elif room_type == "K" or room_type == "k":
                payment_due = nights * KING_ROOM_RATE
                king_room_counter += 1
            else:
                payment_due = 0

            # accumulate the total room rent
            total_room_rent += payment_due
            
            # print the appropriate detail line
            if payment_due == 0:
                print('invalid code')
            else:
                print('$', format(payment_due, '8,.2f'))

            # get the next guest's name
            guest_name = infile.readline()

        # close the input file
        infile.close()

        # print the counters and payment total amount
        print
        print('total number of double rooms sold: ', double_room_counter)
        print('total number of queen rooms sold: ', queen_room_counter)
        print('total number of king rooms sold: ', king_room_counter)
        print
        print('total room rental: ', end='')
        print('$', format(total_room_rent, ',.2f'))

    except IOError:
        print('an error occured trying to open or read motel.txt')

# execute the main function
main()
