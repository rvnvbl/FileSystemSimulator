class Node:
    """A node to represent a file or directory."""
    def __init__(self, node_name, node_type):
        self.node_name = node_name  # Name of the file or directory
        self.node_type = node_type  # 'file' or 'directory'
        self.children = []  # List to store child nodes (for directories)
        self.next = None  # Pointer to the next node (used for linked list)


class FileSystem:
    """A simple file system simulator."""
    def __init__(self):
        self.current_directory = Node('root', 'directory')  # Root directory
        self.root = self.current_directory  # Root of the file system

    def ls(self):
        """List all files and directories in the current directory."""
        print(f"Contents of '{self.current_directory.node_name}':")
        if not self.current_directory.children:
            print("  (No files or directories)")
        else:
            for child in self.current_directory.children:
                print(f"  {child.node_name} ({child.node_type})")

    def mkdir(self, node_name):
        """Create a new directory in the current directory."""
        new_directory = Node(node_name, 'directory')
        self.current_directory.children.append(new_directory)
        print(f"Directory '{node_name}' created.")

    def touch(self, node_name):
        """Create a new file in the current directory."""
        new_file = Node(node_name, 'file')
        self.current_directory.children.append(new_file)
        print(f"File '{node_name}' created.")

    def cd(self, node_name):
        """Change the current directory to the specified directory."""
        if node_name == "..":
            if self.current_directory.node_name != 'root':
                self.current_directory = self.root  # Change to root for simplicity
                print("Changed directory to root.")
            else:
                print("Already at root directory.")
        else:
            for child in self.current_directory.children:
                if child.node_type == 'directory' and child.node_name == node_name:
                    self.current_directory = child
                    print(f"Changed directory to '{node_name}'.")
                    return
            print(f"Directory '{node_name}' not found.")

    def print_structure(self, node=None, indent=0):
        """Helper function to print the structure of the file system recursively."""
        if node is None:
            node = self.root
        print('  ' * indent + f"{node.node_name} ({node.node_type})")
        if node.node_type == 'directory':
            for child in node.children:
                self.print_structure(child, indent + 1)

    def prompt(self):
        """Allow the user to input commands and execute them."""
        while True:
            user_input = input(f"{self.current_directory.node_name} > ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the FileSystem Simulator.")
                break

            command_parts = user_input.split()
            command = command_parts[0].lower()

            if command == 'ls':
                self.ls()
            elif command == 'mkdir' and len(command_parts) > 1:
                self.mkdir(command_parts[1])
            elif command == 'touch' and len(command_parts) > 1:
                self.touch(command_parts[1])
            elif command == 'cd' and len(command_parts) > 1:
                self.cd(command_parts[1])
            else:
                print("Invalid command or missing argument.")

# Testing the file system with interactive prompt
if __name__ == "__main__":
    fs = FileSystem()
    fs.prompt()  # Start the command prompt
