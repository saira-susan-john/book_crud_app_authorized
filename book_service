from repositories.book_repository import BookRepository
from models.book import Book

class BookService:
    def __init__(self, db_config):
        self.book_repository = BookRepository(**db_config)


    def add_book(self, book: Book):
        self.book_repository.add_book(book)

    def get_book_by_id(self, book_id: int):
        return self.book_repository.get_book_by_id(book_id)

    def update_book(self, book: Book):
        existing = self.get_book_by_id(book.id)
        if not existing:
            return False
        return self.book_repository.update_book(book)

    def delete_book(self, book_id: int):
        existing = self.get_book_by_id(book_id)
        if not existing:
            return False
        return self.book_repository.delete_book(book_id)

    def list_all_books(self):
        return self.book_repository.list_all_books()
