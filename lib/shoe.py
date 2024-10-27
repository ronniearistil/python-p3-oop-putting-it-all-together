#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # Use the setter with validation
        self.condition = "New"  # Initialize the shoe's condition

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size with validation
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    # Method to repair the shoe
    def cobble(self):
        self.condition = "New"  # Update condition to 'New'
        print("Your shoe is as good as new!")  # Correct message

if __name__ == "__main__":
    shoe = Shoe("Adidas", 9)
    print(shoe.size)  # Output: 9
    shoe.size = "not an integer"  # Output: size must be an integer
    shoe.cobble()  # Output: Your shoe is as good as new!
    print(shoe.condition)  # Output: New


