class CountLines:
    def __init__(self, file_path):
        """
        Initialize the CountLines class with the file path.

        Parameters:
        file_path (str): The path to the file.
        """
        self.file_path = file_path

    def count_lines(self):
        """
        Count the number of lines in the file.

        Returns:
        int: The number of lines in the file. Returns -1 if the file is not found.
        """
        try:
            with open(self.file_path, 'r') as file:
                line_count = 0
                for line in file:
                    line_count += 1
                return line_count
        except FileNotFoundError:
            return -1  # Return -1 to indicate file not found

# Main program
file_path = input('Please enter the complete file path: ')
data = CountLines(file_path)
line_count = data.count_lines()

if line_count == -1:
    print("File not found. Please recheck the file path.")
else:
    print(f'The number of lines in the file is: {line_count}')