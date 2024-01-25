from model.Book import Book


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_book(self, title, author, quantity):
        book = Book(title, author, quantity)
        self.inventory.append(book)
        print(f"Book added: {book}")

    def update_quantity(self, title, new_quantity):
        for book in self.inventory:
            if book.title == title:
                book.quantity = new_quantity
                print(f"Quantity updated for {book}: {new_quantity}")
                return
        print(f"Book not found: {title}")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for book in self.inventory:
                print(book)

    def process_order(self, title, quantity):
        for book in self.inventory:
            if book.title == title:
                if book.quantity >= quantity:
                    book.quantity -= quantity
                    print(f"Order processed: {quantity} copies of {book} shipped.")
                    return
                else:
                    print(f"Insufficient stock for {book}: Available quantity is {book.quantity}.")
                    return
        print(f"Book not found: {title}")