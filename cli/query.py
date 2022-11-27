
from data import stock
from art import *
import time
import os
import datetime

tprint('Viona.Inc')
print('---------------------------------')
print('WMS - Warehouse Management System')
print('---------------------------------')


# Get the user name
user_name = input('Please enter your name : ')
user_name = user_name.capitalize()


# Greet the user
print('Hello',user_name,', Welcome to our Warehouse!')
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
    print('\n\n',user_name,', Please choose an option : \n 1. List items by warehouse \n 2. Search an item and place an order \n 3. Browse by category \n 4. Quit \n\n' )
    menu_str = input('Please enter 1, 2 or 3 : ')

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
            """ print('--Warehouse 1--')
            total_items1 = []
            for i in stock:
                if i['warehouse'] == 1:
                    total_items1.append(i)
                    print(f"{total_items1.index(i)+1}){i['state']} {i['category']}")
            print('Total items in Warehouse 1 are: ', len(total_items1))
            print('')
            print('--Warehouse 2--')
            total_items2 = []
            for i in stock:
                if i['warehouse'] == 2:
                    total_items2.append(i)
                    print(f"{total_items2.index(i)+1}){i['state']} {i['category']}")
            print('Total items in Warehouse 1 are: ', len(total_items2))
 """
        def filter_data(key,value):
            result = []
            for item in stock:
                if item[key] == value:
                    result.append(item)
            return result

        warehouse1 = filter_data('warehouse',1)
        for item in warehouse1:
            #print(filter_data('category',item['category']))
            print('---')
            print(' ')
            print('Item:----',item['category'])       
            print('total items in warehouse 1', len(filter_data('category',item['category'])))   ## no of items

        warehouse2 = filter_data('warehouse',2)
        for item in warehouse2:
            print('---')
            print(' ')
            print('Item:----',item['category'])       
            print('total items in warehouse 2', len(filter_data('category',item['category'])))   ## no of items

############################### -----------------------MENU 2 BEGINS HERE!!!--------------#######################################
    def menu_2():
        os.system("clear")
        #items_in_warehouse1= 0
        #items_in_warehouse2= 0
        def filter_data(key,value):
            result = []
            for item in stock:
                if item[key] == value:
                    result.append(item)
            return result
        warehouse1 = filter_data('warehouse',1)
        warehouse2 = filter_data('warehouse',2)

        item_name = str.capitalize(input('Choose an item you like: '))
        #if item in warehouse1 or item in warehouse2:
        for item in stock:
            for item in warehouse1:
                if item['state'] in item_name and item['category'] in item_name:
                    items_in_warehouse1 = len(filter_data('category',item['category']))
                    print ('We have ',items_in_warehouse1,' items available in Warehouse 1')
                    print('LOCATION:')
                    delta = datetime.datetime.now() - datetime.datetime.strptime(item["date_of_stock"],"%Y-%m-%d %H:%M:%S")
                    print('Warehouse 1 (in stock for',delta,'days)')
            for item in warehouse2:       
                if item['state'] in item_name and item['category'] in item_name:
                    items_in_warehouse2 = len(filter_data('category',item['category']))
                    print ('We have ',items_in_warehouse2,' items available in Warehouse 2')
                    delta = datetime.datetime.now() - datetime.datetime.strptime(item["date_of_stock"],"%Y-%m-%d %H:%M:%S")
                    print('Warehouse 1 (in stock for',delta,'days)')
            # else:
            #     print('Not in stock')
 
        print('---')
        print('You selected :', item_name)
        #print('Total of', items_in_warehouse1+items_in_warehouse2,' items were found in our warehouses.')
        
        


        # if items_in_warehouse1 > items_in_warehouse2:
        #     print('')
        #     print('Warehouse1 has a larger stock')
        # elif items_in_warehouse1 < items_in_warehouse2:
        #     print('')
        #     print('Warehouse2 has a larger stock')
        # else:
        #     print('')
        #     print('Both our warehouses have an equal stock.')

        
        order = input ('Do you want to place an order?\nType y / n --  ')
            
        time.sleep(0.2)
        print('  *')

        time.sleep(0.3)
        print(' ***')

        time.sleep(0.4)
        print('*****')



        if order == 'y':
            number_of_items = int(input('Please enter the total number of items you want to order: '))
            #print('User input: ',number_of_items)
            
            if number_of_items <= items_in_warehouse1+items_in_warehouse2:
                print('--Order placed for--\nItem:',item_name,'\nTotal number ordered: ',number_of_items)

            elif number_of_items > items_in_warehouse1 + items_in_warehouse2:
                print ('Sorry, we have only ',items_in_warehouse1+items_in_warehouse2,' items available.\nYou may order the maximum available instead.')
                
                max_order = input('Would you like to order the maximum available? y / n --  ')
                if max_order == 'y':
                    print('-----')
                    print('Order placed for:\nItem:',item_name,'\nTotal number ordered: ',items_in_warehouse1+items_in_warehouse2)
                elif max_order == 'n':
                    print('Please check out our warehouses for other items that you might like.')
                else:
                    print('Incorrect entry, please type y / n : ')

            elif order == 'n':
                print('Thank you for your visit, ', user_name,'. See you again!')
            else:
                print('Incorrect entry! Please type y / n : ')

        
        else:
            print('')
            print('ERROR : No such item found!')
    
    def menu_3():
        pass




    # If they pick 1
    if menu ==1:
        menu_1()

    # Else, if they pick 2
    elif menu ==2:
        menu_2()

    # If they pick 3
    elif menu == 3:
        menu_3()

    # Else, if they pick 4
    elif menu ==4:
        print('Thank you for your visit,',user_name,'. See you again!')
        app_running = False
    
    else:
        print(menu,' is not a valid operation')
        

#print('Thank you for your visit, ',user_name)

    # Thank the user for the visit



# the different sections in 'stock'--data.py

# state, category, warehouse, date of stock

""" def filter_data(key,value):
    result = []
    for item in stock:
        if item[key] == value:
            result.append(item)
    return result

warehouse1 = filter_data('warehouse',1)
print(warehouse1)

warehouse2 = filter_data('warehouse',2)
print(warehouse2) """