from src.filesystem import FileSystem


def process_commands(commands):
    fs = FileSystem()
    for command in commands:
        print(command)
        action, *args = command.split()
        if action == "CREATE":
            fs.create_directory(args[0])
        elif action == "MOVE":
            fs.move_directory(args[0], args[1])
        elif action == "DELETE":
            fs.delete_directory(args[0])
        elif action == "LIST":
            fs.list_directory()


commands = [
    "CREATE fruits",
    "CREATE vegetables",
    "CREATE grains",
    "CREATE fruits/apples",
    "CREATE fruits/apples/fuji",
    "LIST",
    "CREATE grains/squash",
    "MOVE grains/squash vegetables",
    "CREATE foods",
    "MOVE grains foods",
    "MOVE fruits foods",
    "MOVE vegetables foods",
    "LIST",
    "DELETE fruits/apples",
    "DELETE foods/fruits/apples",
    "LIST",
]

process_commands(commands)