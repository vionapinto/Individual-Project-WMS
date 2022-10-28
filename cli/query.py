"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from re import S
from data import warehouse1, warehouse2
import time


# YOUR CODE STARTS HERE
print('')
print('WMS - Warehouse Management System')
print('-')


# Get the user name
user_name = input('Please enter your name : ')


# Greet the user
print('Hello',user_name,', Welcome to our Warehouse!')
print('')

time.sleep(0.2)
print('loading..')

time.sleep(0.3)
print('loading..')

time.sleep(0.4)
print('loading..')

app_running = True
while app_running == True:

    # Show the menu and ask to pick a choice
    print('\n\n',user_name,', Please choose an option : \n 1. List items by warehouse \n 2. Search an item and place an order \n 3. Quit \n\n' )
    menu = int(input('Please enter 1, 2 or 3 : '))

    print('')

    time.sleep(0.2)
    print('loading..')

    time.sleep(0.3)
    print('loading..')

    time.sleep(0.4)
    print('loading..')

    print('')


    # If they pick 1
    if menu ==1:
        print('Items in WAREHOUSE 1: ')
        for i in warehouse1:
            print(i)
        print('Items in WAREHOUSE 2: ')
        for i in warehouse2:
            print(i)

    # Else, if they pick 2
    elif menu ==2:
        items_in_warehouse1= 0
        items_in_warehouse2= 0

        item=str.capitalize(input('Choose an item you like: '))  #
        if item in warehouse1 or item in warehouse2:
            print('You selected :', item, '\n Item found!')
            for i in warehouse1:
                    if i.upper() == item.upper():
                        items_in_warehouse1 += 1
            for i in warehouse2:
                    if i.upper() == item.upper():
                        items_in_warehouse1 += 1

            print('Total of', items_in_warehouse1+items_in_warehouse2,' items were found in our warehouses.')
            print ('We have ',items_in_warehouse1,' items available in Warehouse1')
            print ('We have ',items_in_warehouse2,' items available in Warehouse2')


            if items_in_warehouse1 > items_in_warehouse2:
                print('Warehouse1 has a larger stock')
            elif items_in_warehouse1 < items_in_warehouse2:
                print('Warehouse2 has a larger stock')
            else:
                print('Both our warehouses have an equal stock.')

            number_of_items = int(input('Please enter the total number of items you want to order: '))
            print('User input: ',number_of_items)
            print(number_of_items <= items_in_warehouse1 + items_in_warehouse2)
            


            if number_of_items > items_in_warehouse1 + items_in_warehouse2:
                print('Sorry, we have only', items_in_warehouse1+items_in_warehouse2,'items available.\nDo you want to order the maximum number of items available?')

                
                if number_of_items <= items_in_warehouse1 + items_in_warehouse2:
                buying_decision = input('Please type y to checkout or n to exit : ')

                if buying_decision == 'y':
                    print('Purchase successful!')
                    
                elif buying_decision == 'n':
                    print('Sorry, Do you want to buy something else?')
                elif buying_decision != 'y' or buying_decision != 'n':
                    print('ERROR!! Please type: y or n')
                else:
                    print('Sorry, item not found.')
                    
                
            

    # Else, if they pick 3
    elif menu ==3:
        print('Thank you for your visit,',user_name,'. See you again!')
        app_running = False

    # Else

    # Thank the user for the visit

    """ if buying_decision == 'y':
        print('Purchase successful!')
    elif buying_decision == 'n':
        print('Sorry, please visit us again')
    elif buying_decision != 'y' or buying_decision != 'n':
                print('ERROR!! Please type: y or n') """