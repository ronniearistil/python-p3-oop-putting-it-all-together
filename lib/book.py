#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # Use the setter with validation

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_count with validation
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method to display book information
    def display(self):
        print(f"{self.title}, {self.page_count} pages")

    # New method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

if __name__ == "__main__":
    book = Book("The World According to Garp", 69)
    book.turn_page()  # Output: Flipping the page...wow, you read fast!


