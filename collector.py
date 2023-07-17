from model.book import BookModel
from scraper import CnpScraper


class CnpBooksCollector:
    CYCLES = [("Base", range(0, 9)), ("Secondaire", range(0, 4))]
    LEVELS = ['Première année', 'Deuxième année', 'Troisième année', 'Quatrième année', 'Cinquième année', 'Sixième année', 'Septième année', 'Huitième année', 'Neuvième année']
    SUBJECTS = ['اللغة العربية', 'الرياضيات', 'الإيقاظ العلمي', 'علوم الحياة والأرض', 'جغرافيا', 'تاريخ', 'تربية(تشكيلية - تقنية - موسيقية)', 'الألعاب والتسلية', 'فلسفة', 'المواد الاجتماعية وتربية إسلامية وتربية مدنية', 'تربية بدنية', 'Français', 'Mathématique', 'Physique', 'Chimie', 'Sciences naturelles', 'Technologie/Mécanique/Électricité', 'Economie gestion', 'Informatique', 'Anglais', 'Allemand', 'Italien', 'Espagnol']
    SUBJECTS_DB = ["ar", "math", "svt", "svt", "geo", "his", "mu_des_tech_me_el", "jeu", "phylo", "social", "sport", "fr", "math",
                   "phy", "chi", "svt", "mu_des_tech_me_el", "ec_ge", "inf", "en", "de", "it", "es"]

    def __init__(self):
        self.scraper = CnpScraper()

    def collect(self, callback):
        for cycle_index, (cycle, level_range) in enumerate(CnpBooksCollector.CYCLES):
            for level_index in level_range:
                level = CnpBooksCollector.LEVELS[level_index]
                for subject, subject_code in zip(CnpBooksCollector.SUBJECTS, CnpBooksCollector.SUBJECTS_DB):
                    books = self.collect_specific(cycle, level, subject,
                                                  cycle_index, level_index, subject_code)
                    print(f"##{cycle} {level} {subject}")
                    for book in books:
                        print(book)
                        callback(book)

    def collect_specific(self, cycle, level, subject,
                         cycle_index, level_index, subject_code):
        for book_id, book_name, book_part, book_link in self.scraper.get_books(cycle, level, subject):
            book = BookModel(cycle_index, level_index, subject_code, book_part, book_link)
            yield book

    def destroy(self):
        self.scraper.close()