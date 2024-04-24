FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items."""
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items to a list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello!")
    print(get_todos())