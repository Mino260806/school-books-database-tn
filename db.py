import sqlite3

from model.book import BookModel


class BookDatabaseHelper:
    def __init__(self):
        self.db = sqlite3.connect("books.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                cycle INTEGER,
                level INTEGER,
                subject TEXT,
                part INT,
                link TEXT
            )""")

    def add_book(self, book: BookModel):
        self.cursor.execute("INSERT INTO books(book_id, level, cycle, subject, part, link) VALUES (?,?,?,?,?,?)",
                            (book.id, book.level, book.cycle, book.subject, book.part, book.link))

    def save(self):
        self.db.commit()

    def close(self):
        self.db.close()
