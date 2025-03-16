class Library:
    def __init__(self):
        self.books = {}

    def find_book(self, book):
        if book in self.books:
            return True
        return False

    def add_book(self, book):
        if self.find_book(book):
            self.books[book] += 1
        else:
            self.books[book] = 1

    def remove_book(self, book):

        if self.find_book(book):
            self.books[book] -= 1

            if self.books[book] == 0:
                del self.books[book]
        else:
            print("Book not found")

# Легаси код для тестов Я еще не смотрел время уже  поздно пошел спать !
import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.assertTrue(self.library.find_book("Book B"))

    def test_remove_book(self):
        self.library.add_book("Book A")
        self.library.add_book("Book A")
        self.library.remove_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))
        self.library.remove_book("Book B")

    def test_find_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))

if __name__ == '__main__':
    unittest.main()
