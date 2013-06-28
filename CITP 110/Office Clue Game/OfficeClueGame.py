#=====================================================================
# Program:      Office Clue Game
# Programmer:   Teresa Potts
# Date:         June 27, 2013
#=====================================================================

import random

def main():
    print("This is a office clue game.")
    People = find_people()
    #print_people(People)
    #print("")
    Weapons = find_weapons()
    #print_weapons(Weapons)
    #print("")
    Room = find_room()
    #print_room(Room)
    #print("")
    print_all(People, Weapons, Room)
    Num_People = number_people(People)
    Computer_Person_Choice = get_computers_choice_person(Num_People)
    Num_Weapons = number_weapons(Weapons)
    Computer_Weapon_Choice = get_computers_choice_weapons(Num_Weapons)
    Num_Room = number_room(Room)
    Computer_Room_Choice = get_computers_choice_room(Num_Room)
    Meanie = determine_the_meanie(People,Num_People,Computer_Person_Choice)

    Weapon_used = determine_the_weapon(People, Num_People, Computer_Person_Choice, Weapons,Num_Weapons,Computer_Weapon_Choice, Meanie)
    determine_the_room(People, Num_People, Computer_Person_Choice, Weapons,Num_Weapons, Computer_Weapon_Choice, Room,Num_Room,Computer_Room_Choice, Meanie,Weapon_used)

def find_people():
    # Open files for reading.
    infile = open("People.txt", "r")

    # Read the contents of the file into a list.
    people = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    index = 0
    while index < len(people):
        people[index] = people[index].rstrip("\n")
        index += 1

    # Return the contents of the list.
    return(people)

def print_people(People):
    for people in People:
        print(people)

def find_weapons():
    # Open files for reading.
    infile = open("Weapons.txt", "r")

    # Read the contents of the file into a list.
    weapons = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    index = 0
    while index < len(weapons):
        weapons[index] = weapons[index].rstrip("\n")
        index += 1

    # Print the contents of the list.
    return weapons

def print_weapons(Weapons):
    for weapons in Weapons:
        print(weapons)

def find_room():
    # Open files for reading.
    infile = open("Room.txt", "r")
    # Read the contents of the file into a list.
    room = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    index = 0
    while index < len(room):
        room[index] = room[index].rstrip("\n")
        index += 1

    # Print the contents of the list.
    return room

def print_room(Room):
    for room in Room:
        print(room)

def print_all(People, Weapons, Room):
    Number_People = number_people(People)
    Number_Weapons = number_weapons(Weapons)
    Number_Rooms = number_room(Room)

    Max_Number = Number_People
    if Max_Number < Number_Weapons:
        Max_Number = Number_Weapons
    if Max_Number < Number_Rooms:
        Max_Number = Number_Rooms
    print(Max_Number)
    header = ""
    header += "PEOPLE".ljust(40)
    header += "WEAPONS".ljust(40)
    header += "ROOMS".ljust(40)
    print(header)

    for index in range(0, Max_Number):
        line = ""
        if Number_People>=index:
            line += People[index].ljust(40)
        else:
            line += "".ljust(40)
        if Number_Weapons>=index:
            line += Weapons[index].ljust(40)
        else:
            line += "".ljust(40)
        if Number_Rooms>=index:
            line += Room[index].ljust(40)
        else:
            line += "".ljust(40)
        print(line)

def number_people(People):
    people_size = len(People)-1
    return people_size

def number_weapons(Weapons):
    weapons_size = len(Weapons)-1
    return weapons_size

def number_room(Room):
    room_size = len(Room)-1
    return room_size

def get_computers_choice_person(Num_People):
    x = Num_People
    computer_choice = random.randint(0,x)
    return computer_choice

def get_computers_choice_weapons(Num_Weapons):
    x = Num_Weapons
    computer_choice = random.randint(0,x)
    return computer_choice

def get_computers_choice_room(Num_Room):
    x = Num_Room
    computer_choice = random.randint(0,x)
    return computer_choice

def players_choice_people(People,Num_People):
    x = int(Num_People)

    choice = input("Enter a person you think got pwned ")
    try:
        choice = abs(int(choice))
        if choice <= x:
            return choice
        else:
            raise ValueError
    except:
        print("Error: Please input a integer between 0 and", Num_People)
        return players_choice_people(People,Num_People)


def players_choice_weapon(Weapons,Num_Weapons):
    x = int(Num_Weapons)
    choice = int(input("Enter a weapon you think was used to pwn someone "))
    if choice < 0 or choice > x or choice == "":
        print("Error: Please input a integer between 0 and", Num_Weapons)
        return players_choice_weapon(Weapons,Num_Weapons)
    else:
        #print(Weapons[choice])
        return choice

def player_choice_room(Room,Num_Room):
    x = int(Num_Room)
    choice = int(input("Enter a room you think someone got pwned in "))

    if choice < 0 or choice >x:
        print("Error: Please input a integer between 0 and", Num_Room)
        return player_choice_room(Room,Num_Room)
    else:
        #print(Room[choice])
        return choice

def determine_the_meanie(People,Num_People,Computer_Person_Choice):
    while True:

        Players_Choice_Person = players_choice_people(People,Num_People)
        persons_name = People[Players_Choice_Person].lstrip("0123456789. ")
        if Computer_Person_Choice == Players_Choice_Person:
            print(persons_name, "totally got pwned. Now with what?")
            return persons_name
        else:
            print(persons_name, "didn't get pwned. Keep guessing.")

def determine_the_weapon(People, Num_People, Computer_Person_Choice, Weapons,Num_Weapons,Computer_Weapon_Choice, Meanie):
    while True:

        Players_Choice_Weapon = players_choice_weapon(Weapons,Num_Weapons)
        weapon_name = Weapons[Players_Choice_Weapon].lstrip("0123456789. ")
        if Computer_Weapon_Choice == Players_Choice_Weapon:
            print(weapon_name, "was totally used to bop", Meanie)
            return weapon_name
        else:
            print(weapon_name, "wasn't used to do bop", Meanie, "on the head. Keep guessing.")

def determine_the_room(People, Num_People, Computer_Person_Choice, Weapons,Num_Weapons, Computer_Weapon_Choice, Room,Num_Room,Computer_Room_Choice, Meanie,Weapon_used):

    while True:

        Players_Choice_Room = player_choice_room(Room,Num_Room)
        if Computer_Room_Choice == Players_Choice_Room:
            print("Yes!", Meanie, "got bopped by", Weapon_used, "in the", Room[Players_Choice_Room])
            break
        else:
            print(Room[Players_Choice_Room], "was not the room of the crime. Keep guessing.")

# Call the main function.
main()