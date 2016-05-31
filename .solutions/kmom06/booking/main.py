#!/usr/bin/env python3

"""
Main file for testing
"""

from handler import Handler
handler = Handler() # pylint: disable=C0103
# handler.create_calendar()

def menu():
    """
    Display a menu
    """
    print("\n#####  Menu  #####\n")
    print("1) List calendar")
    print("-----------------------")
    print("2) Create team")
    print("3) List all teams")
    print("-----------------------")
    print("4) Create match")
    print("5) List booked matches")
    print("q) Quit.")

def main():
    """
    Main method
    """
    while True:
        menu()
        choice = input(">>> ")

        if choice == "1":
            handler.list_calendar()

        elif choice == "2":
            handler.create_team()

        elif choice == "3":
            handler.list_teams()

        elif choice == "4":
            handler.create_match()

        elif choice == "5":
            handler.list_matches()

        elif choice == "q":
            print("Exiting calendar...")
            break

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
