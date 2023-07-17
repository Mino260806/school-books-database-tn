from collector import CnpBooksCollector
from db import BookDatabaseHelper

if __name__ == '__main__':
    db = BookDatabaseHelper()
    collector = CnpBooksCollector()
    collector.collect(
        lambda book: db.add_book(book)
    )
    db.save()
    collector.destroy()
