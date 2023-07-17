import sqlite3

from model.book import BookModel


class BookDatabaseHelper:
    def __init__(self):
        self.db = sqlite3.connect("books.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cycle INTEGER,
                level INTEGER,
                subject TEXT,
                part INT,
                link TEXT
            )""")

    def add_book(self, book: BookModel):
        self.cursor.execute("INSERT INTO books(level, cycle, subject, link, part) VALUES (?,?,?,?,?)",
                            (book.level, book.cycle, book.subject, book.link, book.part))

    def save(self):
        self.db.commit()

    def close(self):
        self.db.close()
