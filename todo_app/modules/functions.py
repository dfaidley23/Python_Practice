""" is multiline comments/strings """
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todosLocal = file_local.readlines()
    return todosLocal

#passing through an unknown arg(user input) and a default arg like filepath
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
