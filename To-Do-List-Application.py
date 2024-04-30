tasks = {}

def addTask(task): # Function to add task to to-do list. Every task starts as 'false' or 'incomplete'
    tasks[task] = False

def viewTasks(): # Function to view all tasks on to-do list
    if (len(tasks) == 0):
        print("You have no tasks on your to-do list") # If there are no tasks, notify user
    else:
        for i, task in enumerate(tasks): # Loop to print all tasks
            if (tasks[task]): 
                print("{}. {}: Complete".format(i+1, task)) # Print 'Complete' for tasks marked as complete
            else:
                print("{}. {}: Incomplete".format(i+1, task)) # Print 'Incomplete' for all other tasks

def markTaskAsComplete(task): # Function to mark tasks as complete
    try:
        tasks[task] = True # Setting a task to 'true', marks it as complete
    except KeyError: 
        print("There is no such task on the to-do list") # If the task is not detected, notify user

def deleteTask(task): # Function to delete a task
    try:
        tasks.pop(task) # Remove the task from the list
    except KeyError: 
        print("There is no such task on the to-do list") # If the task is not detected, notify user

if __name__ == "__main__": # Main method for the command line interface, and calling above functions
    # Print selection options for user
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    while True: # Loop until terminated by user
        try:
            user_num_input = int(input("Input a number from the list above: ")) # get number input from user
        except ValueError: 
            print("Please select a valid number") # If an invalid input is supplied by user (anything not an integer), notify user
        else:
            if (user_num_input < 1 or user_num_input > 5): 
                print("Please input a number from 1-5") # If an invalid integar is inputted, notify user

            elif (user_num_input == 1): 
                user_input = input("What task would you like to add: ") # Get input from user
                addTask(user_input) # Add inputted task to list

            elif (user_num_input == 2):
                viewTasks() # Show user the full to-do list

            elif (user_num_input == 3):
                user_input = input("What task would you like to mark as complete: ") # Get input from user
                markTaskAsComplete(user_input) # Mark off completed task
                
            elif (user_num_input == 4):
                user_input = input("What task would you like to delete: ") # Get input from user
                deleteTask(user_input) # Delete inputted task from list

            elif (user_num_input == 5): 
                break # Exit loop