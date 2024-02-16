import os

class Library:
    def __init__(self):
        # Initialize the file name
        self.file_name = 'books.txt'
        # Open the file in append mode for reading and appending
        self.file = open(self.file_name, 'a+')


    def __del__(self):
         # Close the file when the object is destroyed
        self.file.close()

    def list_books(self):
        # Move the file pointer to the beginning
        self.file.seek(0)
        # Read all lines from the file
        lines = self.file.readlines()
        # If the file is empty, print a message
        if not lines:
            print("No books found.")
            return
        # Iterate through each line and print book information
        for line in lines:
            book_info = line.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        while True:
            try:
                # Prompt user for book title
                book_title = input("Enter book title: ").strip()
                if not book_title:
                    print("Title cannot be empty. Please try again.")
                    continue
                break
            except Exception as e:
                print("Invalid input. Please try again.")

        while True:
            try:
                # Prompt user for book author
                book_author = input("Enter book author: ").strip()
                if not book_author:
                    print("Author cannot be empty. Please try again.")
                    continue
                break
            except Exception as e:
                print("Invalid input. Please try again.")

        while True:
            try:
                # Prompt user for book release year
                book_release_year = int(input("Enter book release year: "))
                if book_release_year < 0:
                    print("Release year must be a positive number. Please try again.")
                    continue
                break
            except Exception as e:
                print("Invalid input. Please try again.")

        while True:
            try:
                # Prompt user for number of pages
                book_pages = int(input("Enter number of pages: "))
                if book_pages < 0:
                    print("Number of pages must be a positive number. Please try again.")
                    continue
                break
            except Exception as e:
                print("Invalid input. Please try again.")

        # Move the file pointer to the end for appending
        self.file.seek(0, os.SEEK_END)
        # Write the new book information to the file
        book_info = f"{book_title},{book_author},{book_release_year},{book_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
         # Prompt user for book title to remove
        book_title = input("Enter book title to remove: ").strip()
        if not book_title:
            print("Title cannot be empty. Please try again.")
            return
        # Move the file pointer to the beginning
        self.file.seek(0)
        # Read all lines from the file
        lines = self.file.readlines()
        # Reset the file pointer to the beginning
        self.file.seek(0)
        # Clear the file contents
        self.file.truncate()
        # Initialize a flag to track if the book is found
        found = False
        # Iterate through each line and check if the book title matches
        for line in lines:
            book_info = line.strip().split(',')
            if book_info[0] == book_title:
                found = True
            else:
                # Write the line back to the file if the book is not the one to be removed
                self.file.write(line)
        if found:
            print("Book removed successfully.")
        else:
            print("Book not found.")

# Make an object of the Library class
lib = Library()

while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    # Prompt user for menu item
    menu_item = input("Enter menu item: ").strip().lower()
    if menu_item == '1':
        lib.list_books()
    elif menu_item == '2':
        lib.add_book()
    elif menu_item == '3':
        lib.remove_book()
    elif menu_item in ['q', 'Q']:
        break
    else:
        print("Invalid menu item. Please try again.")

# Potential Issues
# - Limited error handling: The error handling is basic and might not cover all possible error scenarios.
# - Lack of input validation: There's no validation for the input data (e.g., release year, number of pages). It's assumed that the user always provides valid input.
# - File handling efficiency: The file is read entirely into memory for operations like removing a book. For larger files, this approach might not be efficient.
# - Potential race conditions: If multiple instances of the program are running concurrently, there might be race conditions when accessing the same file.
