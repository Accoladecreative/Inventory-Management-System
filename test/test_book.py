import sys
import os

# Add the path to the model directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from model.Book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        # Arrange
        title = "The Great Gatsby"
        author = "F. Scott Fitzgerald"
        quantity = 50

        # Act
        book = Book(title, author, quantity)

        # Assert
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.quantity, quantity)

    def test_book_str_representation(self):
        # Arrange
        title = "To Kill a Mockingbird"
        author = "Harper Lee"
        quantity = 30
        book = Book(title, author, quantity)

        # Act
        str_representation = str(book)

        # Assert
        expected_output = f"{title} by {author} - Quantity: {quantity}"
        self.assertEqual(str_representation, expected_output)

if __name__ == '__main__':
    unittest.main()
