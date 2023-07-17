from dataclasses import dataclass


@dataclass
class BookModel:
    id: int
    cycle: int
    level: int
    subject: str
    part: int
    link: str

# class BookFactory:
#     @staticmethod
#     def from_book_id(id, name) -> BookModel:
#         link = f"https://cnp.com.tn/arabic/PDF/{id}P00.pdf"
#         return BookModel(link, name)
