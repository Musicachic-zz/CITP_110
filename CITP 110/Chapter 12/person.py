#=====================================================================
# Program:      Homework Assignment #10
# Programmer:   Teresa Potts
# Date:         April 24,2013
# Abstract:     This program uses a pet class to help a user create a
#               list of pets. It asks for the pet's name, type, and
#               age. It then prints out the pets entered to the user.
#=====================================================================

class Person:

    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num

class Customer(Person):

    def __init__(self, name, address, phone_num, cust_id):
        Customer.__init__(self, name, address, phone_num)

        self.__cust_id = cust_id

class Vendor(Person):

    def __init__(self, name, address, phone_num, vendor_id):
        Vendor.__init__(self, name, address, phone_num, vendor_id)

        self.__vendor_id = vendor_id