from faker import Faker
import random


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Shelf:
    def __init__(self):
        self.books = []
        self.categories = set()

    def add_book(self, book):
        self.books.append(book)
        self.categories.add(book.category)

    def organize_by_title(self):
        self.books.sort(key=lambda book: book.title)

    def __str__(self):
        shelf_name = "&".join(sorted(self.categories)) + " Books" 
        books = '\n  '.join(str(book) for book in self.books)
        return f'Shelf with {shelf_name}:\n  {books}'


class Room:
    def __init__(self):
        self.shelves = []

    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    def organize_books(self, books):
        shelves_by_category = {}
        for book in books:
            if book.category not in shelves_by_category:
                if not any(book.category in shelf.categories for shelf in self.shelves):
                    new_shelf = Shelf()
                    self.add_shelf(new_shelf)
                    shelves_by_category[book.category] = new_shelf
                else:
                    for shelf in self.shelves:
                        if book.category in shelf.categories:
                            shelves_by_category[book.category] = shelf
            shelves_by_category[book.category].add_book(book)

    def sort_shelves(self):
        for shelf in self.shelves:
            shelf.organize_by_title()

    def __str__(self):
        room_str = '\n'.join(str(shelf) for shelf in self.shelves)
        return f'Room:\n{room_str}'


fake = Faker()

categories = ['Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Non-Fiction', 'Historical Fiction', 'Romance']


def create_fake_books(number_of_books):
    books = set()
    for _ in range(number_of_books):
        title = fake.catch_phrase() 
        author = fake.name()
        category = random.choice(categories)
        books.add(Book(title, author, category))
    return books


books = create_fake_books(10)

room = Room()
room.organize_books(books)
room.sort_shelves()
print(room)
