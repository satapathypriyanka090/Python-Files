# Simple To-do Python app Project
from typing import ItemsView


user_input='random'
# create a list for storing items
data= list()
#we are going to create 4 options
# 1. Add an item
# 2. Mark as Done
# 3. View ItemsView
# 4. Exit 

# Lets Create menu items using function

def showMenu():
    print("Choose one of the Following : \n")
    print("[!] 1. Add an item")
    print("[!] 2. Mark as Done")
    print("[!] 3. View all Items")
    print("[!] 4. Exit:")
    

def welcome_page():
    print(" |--------|   --------")
    print("     ||       |      |")
    print("     ||       |      |")
    print("     ||       |      |")
    print("     ||       --------")
    # print("                      ")
welcome_page()
while user_input != '4':

    showMenu()
    user_input = input("\nEnter your choice: ..\n")

    if user_input == '1':
        item = input("\nWhat is to be done ?")
        data.append(item)

        print('\nAdded item:', item)

    elif user_input== '2':
        item= input("\n What is to be marked as Done ")
        # id item is present in data list then remove it from list
        # else item is not list then print item does not exist
        if item in data:
            data.remove(item)
            print("\nRemove item:", item)
        else:
            print("\nItem does not exist in the to-do List")

    elif user_input== '3':
        print("\nList of To-do Items: \n")
        for items in data:
            print(items)
        print()
    elif user_input == '4':
        print("\n Thanks for using To-Do Application!!.. \n hope you loved it \n GoodBye :)")

# So Finally Done: