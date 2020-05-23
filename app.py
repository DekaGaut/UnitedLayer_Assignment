from UnitedLayer_Assignment.utils import database

"""
A hotel has N number of rooms. Create a list of rooms in the hotel such that

Each room in your rooms list needs to contain at least 5 items (ie, TV, couch, table, Air Conditioner etc)
and the relative dollar value of each item.

It should provide us with an interactive command prompt based shell with the following menu.

1. Add a hotel
2. Add a room to the hotel with any of the 5 items.
3. Print out each room along with the individual items and values. This needs to be properly formatted,
eg: no printing an object as /is
4. Accept a budget from the user(in $) and list only those rooms which will cost less than or equal to his budget.
"""


USER_CHOICE = """
Enter:
- 'r' to add a room to the hotel
- 'l' to list all rooms along with the individual items and values 
- 'p' to enter the budget (in $) to check for the available rooms 
- 'q' to quit

Your choice: """

name_hotel = input("Enter the name of the hotel: ").title()


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'r':
            prompt_add_room()
        elif user_input == 'l':
            list_rooms()
        elif user_input == 'p':
            prompt_enter_budget()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_hotel():
    name_hotel = input("Enter the name of the hotel: ").title()

    database.add_hotel(name_hotel)


def prompt_add_room():
    name_room = input("Enter the name of the room: ").title()
    number_items = int(input("Enter the number of items required: "))

    database.add_room(name_room, number_items)


def list_rooms():
    rooms = database.get_all_rooms()
    for room in rooms:
        print(f"{room['room']} costs ${room['budget']} per day."
              f"\nThe list of items along with the values (in $) are: {room['items']}.")


def prompt_enter_budget():
    customer_budget = int(input("Enter your budget (in $) : "))

    database.budget_room(customer_budget)


menu()
print(f"{name_hotel} looks forward to serving you in the future. Thank you for your visit.")
