class CustomStack:
    def __init__(self):
        self.text = ""  # Initial empty text
        self.command_stack = []  # Stack to keep track of commands for undo

    def insert(self, value):
        # Save the current state before executing the command
        self.command_stack.append(self.text)
        # Insert the string value at the current cursor position
        self.text += value

    def delete(self, value):
        # Save the current state before executing the command
        self.command_stack.append(self.text)
        # Delete the last value characters from the text starting from the current cursor position
        self.text = self.text[:-value]

    def get(self, value):
        # Retrieves the character at index value from the text and displays it
        if 0 <= value < len(self.text):
            print(self.text[value])

    def undo(self):
        # Reverts the last executed command on the text
        if self.command_stack:
            self.text = self.command_stack.pop()

# Function to process a sequence of commands
def process_commands(commands):
    text_editor = CustomStack()

    for command in commands:
        operation, *args = command.split()
        if operation == '1':
            text_editor.insert(args[0])
        elif operation == '2':
            text_editor.delete(int(args[0]))
        elif operation == '3':
            text_editor.get(int(args[0]))
        elif operation == '4':
            text_editor.undo()

# Test the function with the given input
input_commands = "1 abc,3 3,2 2,3 1"
commands = input_commands.split(',')
process_commands(commands)
