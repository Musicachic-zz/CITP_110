#=====================================================================
# Program:      Homework Assignment #10
# Programmer:   Teresa Potts
# Date:         April 24,2013
# Abstract:
#=====================================================================

import person

def main():

    peep = person.Person('Emily Darin','1206 Mary Ave Okemos, MI 48917','517-123-4564')

    print("Name:", peep.get_name())
    print("Address:", peep.get_address())
    print("Phone Number:", peep.get_phone_num(),'\n')

    peep = person.Customer('Teresa Potts','1206 Mary Ave Grand Ledge, MI 60126','517-123-4564', 1221)

    print("Name:", peep.get_name())
    print("Address:", peep.get_address())
    print("Phone Number:", peep.get_phone_num())
    print("Customer ID:", peep.get_cust_id(),'\n')

    peep = person.Vendor('Tim Belcher', '1500 Abbot Rd Ste 100 East Lansing, MI 48823', '517-456-4564', 4231)

    print("Name:", peep.get_name())
    print("Address:", peep.get_address())
    print("Phone Number:", peep.get_phone_num())
    print("Vendor ID:", peep.get_vendor_id())

main()

