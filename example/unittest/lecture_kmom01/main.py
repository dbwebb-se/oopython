"""
Handle phonebook
"""
from src.phonebook import Phonebook

def main():
    """Run a phonebook"""
    pb = Phonebook()
    while input("To exit press q: ") != "q":
        todo = int(input(
            "1. Add\n2. Has contacts?\n3. Get a contact\n: "
        ))
        if todo == 1:
            name, number = input("Enter name,number: ").split(",")
            try:
                pb.add_contact(name, number)
            except ValueError:
                print("Use valid number!")
        elif todo == 2:
            empty = "no" if pb.has_contacts() else "yes"
            print(f"is phonebook empty? {empty}")
        elif todo == 3:
            print(pb.get_contact(input("Who to find?")))

if __name__ == "__main__":
    main()
