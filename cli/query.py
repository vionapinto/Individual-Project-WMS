from loader import Loader
from classes import User

personnel = Loader(model="personnel")
stock = Loader(model="stock")

import collections
import datetime
from itertools import zip_longest


STATE = {
    'USER': None,
}
history = []

def list_items_by_warehouse():
    """Print a list of items by warehouse."""
    for warehouse in stock:
        print(f"Items in warehouse {warehouse.id}:")
        for item in warehouse.stock:
            print(f"- {item}")
    total = 0
    print()
    for warehouse in stock:
        total_warehouse = warehouse.occupancy()
        total = total + total_warehouse
        print(f"Total items in warehouse {warehouse.id}:", total_warehouse)

    return f"Listed {total} items"


def print_stock_datetime(today, wh_num, dt_items):
    for item in dt_items:
        stock_time = (today - datetime.datetime.strptime(item.date_of_stock, '%Y-%m-%d %H:%M:%S')).days
        print(f"Warehouse {wh_num} (in stock for {stock_time} days)")



def flatten_personnel(personnel, flatten_list=[]):
    for person in personnel:
        flatten_list.append(person)
        if person.head_of:
            flatten_personnel(person.head_of, flatten_list)
    return flatten_list

personnel_list = flatten_personnel(personnel)


def get_person_entity():
    name = input('Please enter your name: ')
    for employee in personnel_list:
        if employee.is_named(name):
            return employee
    return User(user_name=name)
        
            


def credentials(func):
    def inner(item_name, total_item):
        while True:
            if STATE['USER'].is_authenticated:
                return func(item_name, total_item)
            else:
                password = input('What is your employee password?')
                STATE['USER'].authenticate(password)
                if STATE['USER'].is_authenticated:
                    return func(item_name, total_item)
                else:
                    print('wrong password')
                    if input('Do you want to try again? (y/n)') == 'y':
                        STATE['USER'] = get_person_entity()
                    else:
                        return 'Authentication failed'
    return inner

@credentials
def place_order(item_name, total_amount):
    print()
    amount = int(input("How many would you like to order? "))
    print()
    if amount > total_amount:
        print("*" * 50)
        print("There are not this many available.",
              "The maximum amount that can be ordered is", total_amount)
        print("*" * 50)
        accept_available = input("Would you like to order the maximum available?(y/n) ")
        if accept_available.lower in ["y", "yes"]:
            amount = total_amount
    if amount <= total_amount:
        STATE['USER'].order(item_name, amount)
        print(f"Order placed for {amount} {item_name}")
    return f'placed order for {amount} {item_name}'


def search_and_order_item():
    item_name = input("What would you like to order? ")
    results = {}
    for wh in stock:
        results.update(wh.search(item_name))
    total_item = sum(len(item) for item in results.values())
    if total_item == 0:
        print('Not in warehouses.')
    else: 
        today = datetime.datetime.now()
        print(f"Amount available: {total_item}")
        for wh_num, dt_items in results.items():
            print_stock_datetime(today, wh_num, dt_items)
        order = input('Would you like to place an order?(y/n)')
        if order == 'y':
            history.append(place_order(item_name, total_item))
    return f"Searched for {item_name}"

def print_cat_by_id(my_cat_dict, my_dict_counter):
    print('')
    for id, category in my_cat_dict.items():
        print(f"{id}: {category} {my_dict_counter[category]}")
    print('')

def get_cat_id(my_cat_dict):
    category_id = int(input('Choose a category by id:'))

    print('')
    category_by_id = my_cat_dict[category_id]
    print(f"List of {category_by_id} available: ")
    return category_id

def get_items_by_category(wh, category):
    return [f"{item.state} {item.category} Warehouse{wh.id}" 
                for item in wh.stock
                       if item.category == category]

def browse_by_category():
    category_ct = collections.Counter()

    for wh in stock:
        categories = [item.category for item in wh.stock]
        category_ct.update(categories)

    cat_d = {id:category for id, category in  enumerate(category_ct, start=1)}
    category_id = print_cat_by_id(cat_d, category_ct)
    cat_id = get_cat_id(cat_d)
    wh_items = {}
    for wh in stock:
        unique_items = set(get_items_by_category(wh, cat_d[cat_id]))
        wh_items[wh.id] = unique_items

    for items in zip_longest(*wh_items.values(), fillvalue=False):
        for item in items:
            if item:
                print(f"- {item}")
        print('')
    return f"Browsed the category {cat_d[cat_id]}"

def selection():
    print('1: List all items')
    print('2: Search and place order')
    print('3: Browse by category')
    print('4: Quit')
    return int(input("Choose one option: "))

def start_cli(operation):
    global history
    if operation == 1:
        print('')
        history.append(list_items_by_warehouse())
        start_cli(selection())
    elif operation == 2:
        print('')
        history.append(search_and_order_item())
        start_cli(selection())
    elif operation == 3:
        print('')
        history.append(browse_by_category())
        start_cli(selection())
    elif operation == 4:
        print('')
        print('Thank you for visiting us!')
        for num, action in enumerate(history, start=1):
            print(f"{num}. {action}")
        history = []
        return  
    else:
        print('')
        print('Wrong operation number')
        start_cli(selection())


if "__main__" == __name__:
    STATE['USER'] = get_person_entity()

    start_cli(selection())



