""" Class should be modified """


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


""" Class modified """


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.title} by {self.author}"
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return None
