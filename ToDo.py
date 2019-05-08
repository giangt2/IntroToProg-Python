#-----------------------------------#
#Title:Assignment 6
#Date: May 4, 2019
#Goal: Using the data from Assignment 5 and place the code you created for working with your ToDo.txt file into Functions and a Class.
#-----------------------------------#

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# Define variables
objFileName = "ToDo.txt"
strData = ""
dicRow = {}
lstTable = []


class Todo(object):
    '''This class contains methods to manage a To-Do list'''
    @staticmethod # Define the method


    def start():
        todo_file = open("Todo.txt")  # Open file "Todo.txt"
        test = todo_file.readlines()  # This make it a loop so that the data will continued
        for line in test:  # This make it a loop so that the data will continued
            strData = line.split(",")
            dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()


    def current_list(): # Show the current Data
        print("******* The current ToDo list are: *******")

    def menu_options(): # Provide the options
        print ("""
        Menu of Options: Enter the number on the left.
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)

    def table(): # Create a function for new table
        print("*************************************")
        for lst in lstTable:
            print(lst["Task"] + ": " + lst["Priority"])

    def new_entry(): # Create a new task
        new_errand = input("Enter the new Task: ")
        new_priority = input("What is the priority: ")
        dicNewRow = {"Task": new_errand, "Priority": new_priority}
        print("Current Data in table:")
        lstTable.append(dicNewRow)

    def remove_data(): # Removing data
        del_index = input("Enter the number of the errand to be removed: ")
        del lstTable[int(del_index)]
        print(lstTable)
        print("Task is removed!")

    def save_data(): # Write the data to file
        objFile = open(objFileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        print("Data is saved!")
        objFile.close()


# -------------Processing------------- #
while (True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        Todo.table()

    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        Todo.new_entry()

    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
       Todo.remove_data()

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        Todo.save_data()

    elif (strChoice == '5'):
        print("Exit program!")
        break #and Exit the program