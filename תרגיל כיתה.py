import time
q = 100000
start = time.time()
for _ in range(q):pass
print("O(n):", round(time.time() - start, 5), "seconds")
start = time.time()
for _ in range(q):
 for _ in range(q):pass
print("O(n²):", round(time.time() - start, 5), "seconds")
from models.book import Book
from models.user import User
from typing import List, Optional

class Library:
    def __init__(self, books: List[Book]=None, users: List[User]=None):
        self.books = books or []
        self.users = users or []

    def add_book(self, book: Book):
        if self.find_book_by_isbn(book.isbn):
            raise ValueError("Book with the same ISBN already exists.")
        self.books.append(book)

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def list_available_books(self):
        return [b for b in self.books if b.is_available]

    def search_books(self, query: str):
        q = query.lower()
        return [b for b in self.books if q in b.title.lower() or q in b.author.lower()]

    def add_user(self, user: User):
        if self.find_user_by_id(user.id):
            raise ValueError("User with the same ID already exists.")
        self.users.append(user)

    def find_user_by_id(self, user_id: str) -> Optional[User]:
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    def borrow_book(self, user_id: str, book_isbn: str) -> str:
        user = self.find_user_by_id(user_id)
        if not user:
            return "User not found."
        book = self.find_book_by_isbn(book_isbn)
        if not book:
            return "Book not found."
        if not book.is_available:
            return "Book already borrowed."
        book.is_available = False
        user.borrowed_books.append(book.isbn)
        return f"{user.name} borrowed '{book.title}'."

    def return_book(self, user_id: str, book_isbn: str) -> str:
        user = self.find_user_by_id(user_id)
        if not user:
            return "User not found."
        book = self.find_book_by_isbn(book_isbn)
        if not book:
            return "Book not found."
        if book_isbn not in user.borrowed_books:
            return "This user did not borrow that book."
        user.borrowed_books.remove(book_isbn)
        book.is_available = True
        return f"{user.name} returned '{book.title}'."