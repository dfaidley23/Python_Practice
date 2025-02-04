""" is multiline comments/strings """
#import functions from the functions file in the a directory
# from functions import get_todos, write_todos can be used if you have only a few functions
from modules import functions
import time


date = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", date)


while True:
    userAction = input("Type Add, Show, Edit, Complete, or Exit: ")

    # strip removes blank spaces
    userAction = userAction.strip()

    #match case is almost like an if/else with comparrason operators.
    if userAction.startswith("add"):
        todo = userAction[4:]
        #opens the txt file and reads the contents. It then saves these to a variable
        todos = functions.get_todos()

        todos.append(todo + "\n")
        #file object and opens an object/file then write that data to the file
        functions.write_todos(todos)

    elif userAction.startswith("show"):
        todos = functions.get_todos()

        #list comprehension with a built in for loop to modify and remove the extra line break in the print out
        # new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            #title method capitalizes the first letter of each word
            item  = item.title()
            clean_item = item.strip("\n")
            row = f"{index + 1}.{clean_item}"
            print(row)

    #this case shows how to edit in Python as well as how to correct the array indexing for users to modify a list
    elif userAction.startswith("edit"):
        try:
            number = int(userAction[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Please enter a new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif userAction.startswith("complete"):
        try:
            number = int(userAction[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The ToDo {todo_to_remove} has been completed."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif userAction.startswith("exit"):
        break

    # _ is used by most programmers as a catch all variable
    else:
        print("Please enter a suggested choice.")

print("Bye.")