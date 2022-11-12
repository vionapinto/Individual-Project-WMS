"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from data import warehouse1, warehouse2
from art import *
import time
import os


# YOUR CODE STARTS HERE
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
    print('\n\n',user_name,', Please choose an option : \n 1. List items by warehouse \n 2. Search an item and place an order \n 3. Quit \n\n' )
    menu = input('Please enter 1, 2 or 3 : ')

    while not menu.isnumeric():
        menu = input('Wrong type!! Please enter 1,2 or 3. ')
    
    menu = int(menu)

    print('')

    time.sleep(0.3)
    print('  ~')

    time.sleep(0.4)
    print(' ~~~')

    time.sleep(0.5)
    print('~~~~~')

    print('')


    # If they pick 1
    if menu ==1:
        print('Items in WAREHOUSE 1: ')
        print('--------------------')
        for i in warehouse1:
            print('~',i)
        print('')
        print('Items in WAREHOUSE 2: ')
        print('--------------------')
        for i in warehouse2:
            print('~',i)

    # Else, if they pick 2
    elif menu ==2:
        items_in_warehouse1= 0
        items_in_warehouse2= 0

        item=str.capitalize(input('Choose an item you like: '))  
        if item in warehouse1 or item in warehouse2:
            print('---')
            print('You selected :', item, '\nItem found!')
            for i in warehouse1:
                    if i.upper() == item.upper():
                        items_in_warehouse1 += 1
            for i in warehouse2:
                    if i.upper() == item.upper():
                        items_in_warehouse2 += 1

            print('Total of', items_in_warehouse1+items_in_warehouse2,' items were found in our warehouses.')
            print ('We have ',items_in_warehouse1,' items available in Warehouse1')
            print ('We have ',items_in_warehouse2,' items available in Warehouse2')


            if items_in_warehouse1 > items_in_warehouse2:
                print('')
                print('Warehouse1 has a larger stock')
            elif items_in_warehouse1 < items_in_warehouse2:
                print('')
                print('Warehouse2 has a larger stock')
            else:
                print('')
                print('Both our warehouses have an equal stock.')

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
                    print('--Order placed for--\nItem:',item,'\nTotal number ordered: ',number_of_items)

                elif number_of_items > items_in_warehouse1 + items_in_warehouse2:
                    print ('Sorry, we have only ',items_in_warehouse1+items_in_warehouse2,' items available.\nYou may order the maximum available instead.')
                    
                    max_order = input('Would you like to order the maximum available? y / n --  ')
                    if max_order == 'y':
                        print('-----')
                        print('Order placed for:\nItem:',item,'\nTotal number ordered: ',items_in_warehouse1+items_in_warehouse2)
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

    # Else, if they pick 3
    elif menu ==3:
        print('Thank you for your visit,',user_name,'. See you again!')
        app_running = False
    
    else:
        print(menu,' is not a valid operation')
        

#print('Thank you for your visit, ',user_name)

    # Thank the user for the visit