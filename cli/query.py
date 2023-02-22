# import re
# #from data import personnel, stock
# #from art import *
# import time
# import os
# import datetime
# import collections
# from loader import Loader


# # tprint('Viona.Inc')
# print('---------------------------------')
# print('WMS - Warehouse Management System')
# print('---------------------------------')


# personnel = Loader(model="personnel")
# stock = Loader(model="stock")

# user_information={}

# def get_user_V2(personnel,flatten_list=[]): #This is a recursive function, it takes two arguments. One is the list personnel and the other is an empty list
#     for person in personnel: # We are iterating through every dictionary in personnel
        
        
#         flatten_list.append(person) # We are appending every dictionary to the empty flatten list
#         #print(person)
#         if "head_of" in person: # if the key "head_of" is in person run the function again
#             get_user_V2(person["head_of"], flatten_list)# the function runs again but it goes through the values of person[head_of] instead of only person
#             del person["head_of"]# the head of is deleted for better readability
    
#     return flatten_list



# flat_list = get_user_V2(personnel)
# #print (flat_list)


# def security_check():  

#     print("Please authenticate yourself")  
#     user_name = input("Please insert user name: ").capitalize()
#     user_password=input("Please type your password: ").lower()
    

#     for dictionary in flat_list:
        
#         if user_name == dictionary["user_name"]:
#             if user_password==dictionary["password"]:
#                 user_information.update({"user_name":user_name})
#                 user_information.update({"password": dictionary["password"]})
#                 print(user_information)
#         elif user_name!= dictionary["user_name"]:
#            pass      
#         else:
#             print("Wrong credentials")

# # to ask once again if we want to order something else
# def final_decision():
#     opt = input('Do you want to add something else into your cart? Enter y or n:  ')
#     if opt == 'y':
#         search_and_order_item()
#     elif opt == 'n':
#         print('You are not choosing any other item.Thank you.')
#     else:
#         print('please choose y or n')
#         final_decision()



# # Get the user name
# user_name = input('Please enter your name : ')
# user_name = user_name.capitalize()


# # Greet the user
# print('Hello', user_name, ', Welcome to our Warehouse!')
# print('')

# time.sleep(0.2)
# print('  .')

# time.sleep(0.3)
# print(' ...')

# time.sleep(0.4)
# print('.....')

# app_running = True
# while app_running == True:

#     # Show the menu and ask to pick a choice
#     print('\n\n', user_name, ', Please choose an option : \n 1. List items by warehouse \n 2. Search an item and place an order \n 3. Browse by category \n 4. Quit \n\n')
#     menu_str = input('Please enter 1, 2, 3 or 4 : ')

#     while not menu_str.isnumeric():
#         menu_str = input('Wrong type!! Please enter 1,2,3 or 4: ')

#     menu = int(menu_str)


#     print('')

#     def max_warehouse():        # counting total number of warehouses
#         return max([item['warehouse'] for item in stock])
#     number_of_warehouses = max_warehouse()

# ## menu 1 begins here
#     def list_items_by_warehouse():
#         if menu == 1:  
#             for j in range(1, number_of_warehouses+1):        # since there are 4 warehouses!
#                 print ("---Warehouse",j,"---")
#                 print('-----------------------')
#                 total_items = []
#                 for i in stock:
#                     if i["warehouse"] == j:
#                         total_items.append(i)
#                         print (f"{total_items.index(i) + 1}) {i['state']} {i['category']}")                
#             print (f"\nTotal items in warehouse {j} --> {len(total_items)}")
            

# ############################### -----------------------MENU 2 BEGINS HERE!!!--------------#######################################
    
#     def search_and_order_item():
#         os.system("clear")
#         item_name = input("Please state the item you are searching for: ")
#         list_of_warehouse_items = []    # list of lists. each list inside is a warehouse
#         #total_items_ordered = 0
#         for j in range(1, number_of_warehouses+1):
#             warehouse_temp_list = []
#             for i in range(len(stock)):
#                 if stock[i]["state"].upper() in item_name.upper() and stock[i]["category"].upper() in item_name.upper() and stock[i]["warehouse"] == j:
#                     warehouse_temp_list.append(stock[i])
#             list_of_warehouse_items.append(warehouse_temp_list)

#             total_items_available = sum([len(warehouse_list) for warehouse_list in list_of_warehouse_items])
            
#             print(f"Total number of items in warehouse {j} is {len(warehouse_temp_list)}")
#         print(f"Total items available: {total_items_available}")

# ## the code has been pasted below 
        
#         print('')
#         print("Location:")
#         for list in list_of_warehouse_items:
#             for i in list:
#                 delta = datetime.datetime.now() - datetime.datetime.strptime(i["date_of_stock"], "%Y-%m-%d %H:%M:%S")
#                 print('Warehouse',i['warehouse'],' --> (in stock for ', delta.days, 'days)')


#         order = input('Do you want to place an order?\nType y / n --  ')

#         time.sleep(0.2)
#         print('  *')
#         time.sleep(0.3)
#         print(' ***')
#         time.sleep(0.4)
#         print('*****')

#         if order == 'y':
#             while True:
#                 security_check()
#                 if "user_name" in user_information and "password" in user_information: 
#                     number_of_items = input('Please enter the total number of items you want to order: ')
#                     if number_of_items.isnumeric():
#                         number_of_items_integer = int(number_of_items)
#                         if number_of_items_integer <= total_items_available:
#                             print('--Order placed for--\nItem:', item_name.capitalize(),'\nTotal number ordered: ', number_of_items_integer)
#                             final_decision()
#                             break
#                         elif number_of_items_integer > total_items_available:
#                             print('Sorry, we have only ', total_items_available,
#                                 ' items available.\nYou may order the maximum available instead.')

#                             max_order = input(
#                                 'Would you like to order the maximum available? y / n --  ')
#                             if max_order == 'y':
#                                 print('-----')
#                                 print('Order placed for:\nItem:', item_name,
#                                     '\nTotal number ordered: ', total_items_available)
#                             elif max_order == 'n':
#                                 print('There may be other items in our warehouses that you might like.')
#                                 final_decision()
#                                 break
#                             else:
#                                 print('Incorrect entry, please type y / n : ')

#                         elif order == 'n':
#                             print('Thank you for your visit, ',user_name, '. See you again!')
#                         else:
#                             print('Incorrect entry! Please type y / n : ')
#                     else:
#                         print('!!!')
#                         print("Please enter an integer")
#                         print('!!!')
#                 else:
#                     print('!!!!!!!')
#                     print('ERROR: User not recognized!')
#                     print('!!!!!!!')
                    

#         elif order == 'n':
#             pass

#         else:
#             print('')
#             print('ERROR : Incorrect entry! Please type y / n : ')
# ##################### -- ----------------MENU 3 starts here!!!-----------------------------------------------------------   
    
#     def browse_by_category():
#         os.system("clear")
#         categories = {1:"Keyboard",2:"Smartphone",3:"Mouse",4:"Laptop",5:"Headphones",6:"Monitor",7:"Router",8:"Tablet"}
#         temp = []
#         for i in stock:
#             counter1 = 0
#             for b in categories:
#                 counter1 += 1
#                 if i["category"] in categories[counter1]:
#                     temp.append(counter1)           
#         counter = 1
#         for i in categories:
#             print(f"{i}. {categories[i]} ({temp.count(counter)})")
#             counter += 1
#         menu_category = int(input("\nPress 9 to quit:\n-OR-\nType the number of the category (1 - 9) to browse: --> "))
#         if menu_category in range(1,9):
#             for i in stock:
#                 if categories[int(menu_category)] == i["category"]:
#                     print(i["state"], i["category"],", Warehouse", i["warehouse"])
#         elif menu_category == "9":
#             pass     
        
#     # If they pick 1
#     if menu == 1:
#         list_items_by_warehouse()

#     # Else, if they pick 2
#     elif menu == 2:
#         search_and_order_item()

#     # If they pick 3
#     elif menu == 3:
#         browse_by_category()

#     # Else, if they pick 4
#     elif menu == 4:
#         print('Thank you for your visit,', user_name, '. See you again!')
#         app_running = False

#     else:
#         print('*' * 50)
#         print(menu, ' is not a valid operation')
#         print('*' * 50)





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


## this is the code that i said was copied below

# if len(warehouse1) > 0 and len(warehouse2) > 0:
        #     print(item_name.capitalize(), "is available in both warehouses!")

        #     if len(warehouse1) < len(warehouse2):
        #         print("Warehouse 2 has a larger stock.")
        #     elif len(warehouse1) > len(warehouse2):
        #         print("Warehouse 1 has a larger stock")
        #     else:
        #         print("Both warehouses have equal stock")

        #     print('')
        #     number = len(warehouse1) + len(warehouse2)
        #     print('A total of', number, "pieces are available")
        #     print(len(warehouse1), "-- Warehouse 1")
        #     print(len(warehouse2), "-- Warehouse 2")

        # elif len(warehouse1) > 0 and len(warehouse2) == 0:
        #     print("There are ", len(warehouse1), "pieces available")
        #     print(item_name, "is available only in Warehouse 1")
        # elif len(warehouse2) > 0 and len(warehouse1) == 0:
        #     print("There are ", len(warehouse2), "pieces available")
        #     print(item_name, "is available only in Warehouse 2")
        # else:
        #     print("Not in Stock")