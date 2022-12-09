
from data import stock
#from art import *
import time
import os
import datetime
import collections

# tprint('Viona.Inc')
print('---------------------------------')
print('WMS - Warehouse Management System')
print('---------------------------------')


# Get the user name
user_name = input('Please enter your name : ')
user_name = user_name.capitalize()


# Greet the user
print('Hello', user_name, ', Welcome to our Warehouse!')
print('')

time.sleep(0.2)
print('  .')

time.sleep(0.3)
print(' ...')

time.sleep(0.4)
print('.....')

app_running = True
while app_running == True:

    # Show the menu and ask to pick a choice
    print('\n\n', user_name, ', Please choose an option : \n 1. List items by warehouse \n 2. Search an item and place an order \n 3. Browse by category \n 4. Quit \n\n')
    menu_str = input('Please enter 1, 2, 3 or 4 : ')

    while not menu_str.isnumeric():
        menu_str = input('Wrong type!! Please enter 1,2,3 or 4: ')

    menu = int(menu_str)

    print('')
    time.sleep(0.3)
    print('  ~')
    time.sleep(0.4)
    print(' ~~~')
    time.sleep(0.5)
    print('~~~~~')

    print('')

    def menu_1():
        if menu == 1:
            print ("--Warehouse 1--")
            print('-----------------------')
            total_items1 = []
            for i in stock:
                if i["warehouse"] == 1:
                    total_items1.append(i)
                    print (f"{total_items1.index(i) + 1}) {i['state']} {i['category']}")                
            print ("\n--Warehouse 2--")
            print('------------------------')
            total_items2 = []
            for i in stock:
                if i["warehouse"] == 2:
                    total_items2.append(i)
                    print (f"{total_items2.index(i) + 1}) {i['state']} {i['category']}")
        print (f"\nTotal items in warehouse 1 - {len(total_items1)}\nTotal items in warehouse 2- {len(total_items2)}")

############################### -----------------------MENU 2 BEGINS HERE!!!--------------#######################################
    def menu_2():
        os.system("clear")
        item_name = input("Please state the item you are searching for: ")
        warehouse1 = []
        warehouse2 = []
        for i in range(len(stock)):
            if stock[i]["state"].upper() in item_name.upper() and stock[i]["category"].upper() in item_name.upper() and stock[i]["warehouse"] == 1:
                warehouse1.append(stock[i])
            elif stock[i]["state"].upper() in item_name.upper() and stock[i]["category"].upper() in item_name.upper() and stock[i]["warehouse"] == 2:
                warehouse2.append(stock[i])

        if len(warehouse1) > 0 and len(warehouse2) > 0:
            print(item_name.capitalize(), "is available in both warehouses!")

            if len(warehouse1) < len(warehouse2):
                print("Warehouse 2 has a larger stock.")
            elif len(warehouse1) > len(warehouse2):
                print("Warehouse 1 has a larger stock")
            else:
                print("Both warehouses have equal stock")

            print('')
            number = len(warehouse1) + len(warehouse2)
            print('A total of', number, "pieces are available")
            print(len(warehouse1), "-- Warehouse 1")
            print(len(warehouse2), "-- Warehouse 2")

        elif len(warehouse1) > 0 and len(warehouse2) == 0:
            print("There are ", len(warehouse1), "pieces available")
            print(item_name, "is available only in Warehouse 1")
        elif len(warehouse2) > 0 and len(warehouse1) == 0:
            print("There are ", len(warehouse2), "pieces available")
            print(item_name, "is available only in Warehouse 2")
        else:
            print("Not in Stock")
        print('')
        print("Location:")
        for i in warehouse1:
            delta = datetime.datetime.now() - datetime.datetime.strptime(i["date_of_stock"], "%Y-%m-%d %H:%M:%S")
            print('Warehouse 1 --> (in stock for ', delta.days, 'days)')
        for i in warehouse2:
            delta = datetime.datetime.now() - datetime.datetime.strptime(i["date_of_stock"], "%Y-%m-%d %H:%M:%S")
            print('Warehouse 2 --> (in stock for ', delta.days, 'days)')

        order = input('Do you want to place an order?\nType y / n --  ')

        time.sleep(0.2)
        print('  *')
        time.sleep(0.3)
        print(' ***')
        time.sleep(0.4)
        print('*****')

        if order == 'y':

            number_of_items = int(input('Please enter the total number of items you want to order: '))

            if number_of_items <= number:
                print('--Order placed for--\nItem:', item_name.capitalize(),'\nTotal number ordered: ', number_of_items)

            elif number_of_items > number:
                print('Sorry, we have only ', number,
                      ' items available.\nYou may order the maximum available instead.')

                max_order = input(
                    'Would you like to order the maximum available? y / n --  ')
                if max_order == 'y':
                    print('-----')
                    print('Order placed for:\nItem:', item_name,
                          '\nTotal number ordered: ', number)
                elif max_order == 'n':
                    print('Please check out our warehouses for other items that you might like.')
                else:
                    print('Incorrect entry, please type y / n : ')

            elif order == 'n':
                print('Thank you for your visit, ',user_name, '. See you again!')
            else:
                print('Incorrect entry! Please type y / n : ')

        elif order == 'n':
            pass

        else:
            print('')
            print('ERROR : No such item found!')

    
    def menu_3():
        os.system("clear")
        categories = {1:"Keyboard",2:"Smartphone",3:"Mouse",4:"Laptop",5:"Headphones",6:"Monitor",7:"Router",8:"Tablet"}
        temp = []
        for i in stock:
            counter1 = 0
            for b in categories:
                counter1 += 1
                if i["category"] in categories[counter1]:
                    temp.append(counter1)           
        counter = 1
        for i in categories:
            print(f"{i}. {categories[i]} ({temp.count(counter)})")
            counter += 1
        menu_category = int(input("\nPress 9 to quit:\n-OR-\nType the number of the category (1 - 9) to browse"))
        if menu_category in range(1,9):
            for i in stock:
                if categories[int(menu_category)] == i["category"]:
                    print(i["state"], i["category"],", Warehouse", i["warehouse"])
        elif menu_category == "9":
            pass     
        
    # If they pick 1
    if menu == 1:
        menu_1()

    # Else, if they pick 2
    elif menu == 2:
        menu_2()

    # If they pick 3
    elif menu == 3:
        menu_3()

    # Else, if they pick 4
    elif menu == 4:
        print('Thank you for your visit,', user_name, '. See you again!')
        app_running = False

    else:
        print(menu, ' is not a valid operation')


#################### the category keeps repeating!! ###############
# def filter_data(key, value):
#             result = []
#             for item in stock:
#                 if item[key] == value:
#                     result.append(item)
#             return result

#         warehouse1 = filter_data('warehouse', 1)
#         for item in warehouse1:
#             print(f"{item['category']} ({len(filter_data('category', item['category']))})")

#         warehouse2 = filter_data('warehouse', 2)
#         for item in warehouse2:
#             print(f"{item['category']} ({len(filter_data('category', item['category']))})")



################## how do we merge a dict and list?? #################


# def menu_3():
    #     pass
    #     dict_of_categories = {1: 'Keyboard', 2:'Smartphone', 3: 'Mouse', 4:'Laptop', 5:'Headphones', 6:'Monitor', 7:'Router' , 8: 'Tablet'}

    #     category_list = [item['category'] for item in stock]
    #     category_counter = collections.Counter(category_list)
    #     print(category_list)
    #     print(list(category_counter.items()))
    #     for item in stock:
    #         pass