"""
Concerned with storing and retrieving rooms from a list.
"""

hotels = []


def add_room(name_room, number_item):
    room = {}
    budget = 0
    for i in range(number_item):
        item_name = input("Enter name of the item: ").title()
        item_price = int(input("Enter the price of the product: "))
        budget += item_price

        room[item_name] = item_price

    hotels.append({'room': name_room, 'items': room, 'budget': budget})
    return room


def get_all_rooms():
    return hotels


def budget_room(customer_budget):
    cost = []
    for room in hotels:
        room_name = room['room']
        budget_per_room = room['budget']
        cost.append({'room': room_name, 'cost': budget_per_room})

    for r in cost:
        if customer_budget >= r['cost']:
            print(f'{r["room"]} costs ${r["cost"]} per day.')
        else:
            print("Sorry for the inconvenience. There are no rooms available in your budget."
                  "\nThanks for your visit.")
            break

