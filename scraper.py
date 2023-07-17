from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver


class CnpScraper:
    def __init__(self):
        webdriver_service = Service()

        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        driver.get("https://cnp.com.tn/CNP1/web/french/biblio/man-eleves.jsp")

        self.driver = driver

    def get_books(self, cycle, level, subject):
        self._access_book_page(cycle, level, subject)
        result = list(self._fetch_book_ids_names())

        self.driver.back()
        return result

    def close(self):
        self.driver.quit()

    def _access_book_page(self, cycle, level, subject):
        cycle_select = Select(self.driver.find_element(By.NAME, "CYCLE"))
        level_select = Select(self.driver.find_element(By.NAME, "CLASSE"))
        subject_select = Select(self.driver.find_element(By.NAME, "MATIERE"))
        type_select = Select(self.driver.find_element(By.NAME, "type"))
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="javascript:chercher_eleve();"]')

        cycle_select.select_by_visible_text(cycle)
        level_select.select_by_visible_text(level)
        subject_select.select_by_visible_text(subject)

        search_button.click()

    def _fetch_book_ids_names(self):
        for book_tr in self.driver.find_elements(By.CLASS_NAME, "tr_content"):
            cols = book_tr.find_elements(By.TAG_NAME, "td")
            book_link = cols[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            book_part = int(cols[0].find_element(By.TAG_NAME, "a").text.split()[1]) - 1
            if book_part == 0:
                book_name = cols[1].text
                book_id = int(cols[2].text)
            yield book_id, book_name, book_part, book_link
