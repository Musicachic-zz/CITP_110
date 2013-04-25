#=====================================================================
# Program:      Homework Assignment #10
# Programmer:   Teresa Potts
# Date:         April 24,2013
# Abstract:
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
        Person.__init__(self, name, address, phone_num)

        self.__cust_id = cust_id

    def set_cust_id(self, cust_id):
        self.__cust_id = cust_id

    def get_cust_id(self):
        return self.__cust_id

class Vendor(Person):

    def __init__(self, name, address, phone_num, vendor_id):
        Person.__init__(self, name, address, phone_num)

        self.__vendor_id = vendor_id
    def set_vendor_id(self, vendor_id):
        self.__vendor_id = vendor_id

    def get_vendor_id(self):
        return self.__vendor_id