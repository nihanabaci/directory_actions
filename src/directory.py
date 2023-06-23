class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

        # sorts the directories in alphabetical order
        self.children = sorted(self.children, key=lambda dir: dir.name)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def remove_child(self, child):
        self.children.remove(child)

    def list_children(self, indent=""):
        print(indent + self.name)
        for child in self.children:
            child.list_children(indent + "  ")