'''
Title: To do list
Assignment 5
April 28, 2019
Create a text file called Todo.txt using the following data:
Clean House,low
Pay Bills,high
2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary. (The data will be stored like a row in a table.)
Tip: You can use a for loop to read a single line of text from the file and then place the data into a new dictionary object.
3.	After you get the data in a Python dictionary, Add the new dictionary “row” into a Python list object (now the data will be managed as a table).
4.	Display the contents of the List to the user.
5.	Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
6.	Save the data from the table into the Todo.txt file when the program exits.
'''

# Declaring my variables
strData = ""
dicRow = {}
lstTable = []
textfile = ("Todo.txt", "r")

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"
todo_file = open("Todo.txt") # Open file "Todo.txt"
test = todo_file.readlines() # This make it a loop so that the data will continued
for line in test: # This make it a loop so that the data will continued
    contents = line.split(",")
    dicRow[contents[0].strip()] = contents[1].strip()
    lstTable.append(dicRow)
todo_file.close()

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        new_errand = input("Enter the new Task: ")
        new_priority = input("What is the priority: ")
        dicNewRow = {"Task": new_errand, "Priority": new_priority}
        print("Current Data in table:")
        for dicRow in lstTable:
            print(dicNewRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        del_index = input("Enter the number of the errand to be removed: ")
        lstTable.pop(int(del_index))
        print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        saveData = input("Do you want to save the dat? (y/n")
        if (saveData.lower() == "y"):
            new_errand0= input("Enter the new Task: ")
            new_priority0 = input("What is the priority: ")
            newDicRow0 = {new_errand0,new_priority0}
            todo_file = open("Todo.txt", "w")
            todo_file.write(newDicRow0)
            print("Data was saved!")
            objFile.close()
        else:
            print("Data was not saved!")
        continue
    elif (strChoice == '5'):
        break  # and Exit the program



