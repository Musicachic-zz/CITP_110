import person

def main():

    peep = person.Customer('Teresa Potts','1206 Mary Ave Grand Ledge, MI 60126','517-123-4564','4562')

    print("Name:", peep.get_name())
    print("Address:", peep.get_address())
    print("Phone Number:", peep.get_phone_num())
    print("Customer ID:", peep.get_cust_id())

main()

