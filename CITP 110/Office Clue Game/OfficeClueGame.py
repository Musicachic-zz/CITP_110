#=====================================================================
# Program:      Office Clue Game
# Programmer:   Teresa Potts
# Date:         June 27, 2013
#=====================================================================

import random

def main():
    print("This is a office clue game.")
    People = find_people()
    print_people(People)
    Weapons = find_weapons()
    print_weapons(Weapons)
    Room = find_room()
    print_room(Room)
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

def number_people(People):
    people_size = len(People)
    return people_size

def number_weapons(Weapons):
    weapons_size = len(Weapons)
    return weapons_size

def number_room(Room):
    room_size = len(Room)
    return room_size

def get_computers_choice_person(Num_People):
    x = Num_People
    computer_choice = random.randint(0,x-1)
    return computer_choice

def get_computers_choice_weapons(Num_Weapons):
    x = Num_Weapons
    computer_choice = random.randint(0,x-1)
    return computer_choice

def get_computers_choice_room(Num_Room):
    x = Num_Room
    computer_choice = random.randint(0,x-1)
    return computer_choice

def players_choice_people(People,Num_People):
    x = int(Num_People)

    choice = int(input("Enter a person you think got pwned "))
    if choice < 0 or choice >= x:
        print("Error: Please input a integer between 0 and", Num_People-1)
        return players_choice_people(People,Num_People)
    else:
        print(People[choice])
        return choice


def players_choice_weapon(Weapons,Num_Weapons):
    x = int(Num_Weapons)
    choice = int(input("Enter a weapon you think was used to pwn someone "))

    if choice < 0 or choice >= x:
        print("Error: Please input a integer between 0 and", Num_Weapons-1)
        return players_choice_weapon(Weapons,Num_Weapons)
    else:
        print(Weapons[choice])
        return choice

def player_choice_room(Room,Num_Room):
    x = int(Num_Room)
    choice = int(input("Enter a room you think someone got pwned in "))

    if choice < 0 or choice >=x:
        print("Error: Please input a integer between 0 and", Num_Room-1)
        return player_choice_room(Room,Num_Room)
    else:
        print(Room[choice])
        return choice

def determine_the_meanie(People,Num_People,Computer_Person_Choice):
    while True:

        Players_Choice_Person = players_choice_people(People,Num_People)
        print(Computer_Person_Choice)
        if Computer_Person_Choice == Players_Choice_Person:
            print(People[Players_Choice_Person], "totally did it. Now what did they do it with?")
            return People[Players_Choice_Person]
        else:
            print(People[Players_Choice_Person], "didn't do it. Keep guessing.")

def determine_the_weapon(People, Num_People, Computer_Person_Choice, Weapons,Num_Weapons,Computer_Weapon_Choice, Meanie):
    while True:

        Players_Choice_Weapon = players_choice_weapon(Weapons,Num_Weapons)
        if Computer_Weapon_Choice == Players_Choice_Weapon:
            print(Weapons[Players_Choice_Weapon], "was totally used to bop", Meanie)
            return Weapons[Players_Choice_Weapon]
        else:
            print(Weapons[Players_Choice_Weapon], "wasn't used to do bop", Meanie, "on the head. Keep guessing.")

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