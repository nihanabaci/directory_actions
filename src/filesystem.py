from src.directory import Directory


class FileSystem:
    def __init__(self):
        self.root = Directory("")

    def create_directory(self, path):
        names = path.split("/")
        current_dir = self.root
        for name in names:
            existing_dir = current_dir.find_child(name)
            if existing_dir:
                current_dir = existing_dir
            else:
                new_dir = Directory(name)
                current_dir.add_child(new_dir)
                current_dir = new_dir

    def move_directory(self, source_path, destination_path):
        source_names = source_path.split("/")
        destination_names = destination_path.split("/")
        source_dir = self._traverse_path(source_names)
        if source_dir:
            destination_dir = self._traverse_path(destination_names)
            if destination_dir:
                source_parent = self._traverse_path(source_names[:-1])
                source_parent.remove_child(source_dir)
                destination_dir.add_child(source_dir)

    def delete_directory(self, path):
        names = path.split("/")
        directory = self._traverse_path(names)
        if directory:
            parent = self._traverse_path(names[:-1])
            parent.remove_child(directory)
        else:
            print(f"Cannot delete {path} - {names[-2]} does not exist")

    def list_directory(self):
        if self.root.name != "":
            print(self.root.name)
        for child in self.root.children:
            child.list_children()

    def _traverse_path(self, names):
        current_dir = self.root
        for name in names:
            current_dir = current_dir.find_child(name)
            if not current_dir:
                return None
        return current_dir