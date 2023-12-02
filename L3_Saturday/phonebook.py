# list of dictionaries where each dicitionary - detail of contact
from pprint import pprint

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "97002233",
            "mobile": "0400123456"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Melbourne",
        "phone": {
            "home": "95001122",
            "mobile": "0400234567"
        }
    }
]

pprint(phonebook)

name = input("Enter name: ")
address = input("Enter Address: ")
home = input("Enter home phone: ")
mobile = input("Enter mobile: ")

# variant one - append to dict on the fly
phonebook.append(
    {
    "name": name,
    "address": address,
    "phone": {
        "home": home,
        "mobile": mobile,
    }
}
)

# variant two - create a new dict, and append to previous

# # create a dict
# contact_to_add = {
#     "name": name,
#     "address": address,
#     "phone": {
#         "home": home,
#         "mobile": mobile,
#     }
# }

# # append to the phonebook list

# phonebook.append(contact_to_add)

pprint(phonebook)

# find a number in the phonebook

number_to_find = input("enter a number to find: ")

def find_number(number):
    for phone_entry in phonebook:
        for phone_number_key in phone_entry["phone"]:
            print(phone_entry["phone"])
            [phone_number_key]
            if (number == phone_entry["phone"][phone_number_key]):
                print("number found")
                return
            
find_number(number_to_find)