import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        """Preconditions: Відкриття браузера та перехід на сторінку подій"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc1_verify_events_list_display(self):
        """TC-1: Перевірка відображення списку подій"""
        # Чекаємо завантаження карток подій (клас .list-item)
        event_cards = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-item")),
            "Список подій не завантажився"
        )
        self.assertGreater(len(event_cards), 0, "На сторінці немає жодної події")

    def test_tc3_search_functionality(self):
        """TC-3: Пошук події за назвою 'Eco Workshop'"""
        search_query = "Eco Workshop"
        
        # Знаходимо інпут пошуку
        search_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))
        )
        search_field.send_keys(search_query)
        search_field.send_keys(Keys.ENTER)
        
        # Перевіряємо, що заголовок першої знайденої картки містить запит
        first_card_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".list-item-title"))
        )
        self.assertIn(search_query.lower(), first_card_title.text.lower())

    def test_tc5_negative_search(self):
        """TC-5 (Negative): Пошук неіснуючої події 'zxcvbnm123'"""
        invalid_query = "zxcvbnm123"
        
        search_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))
        )
        search_field.send_keys(invalid_query)
        search_field.send_keys(Keys.ENTER)
        
        # Очікуємо, що список подій стане порожнім (елементи зникнуть)
        # Використовуємо find_elements (множина), він поверне порожній список без помилки
        events = self.driver.find_elements(By.CSS_SELECTOR, ".list-item")
        self.assertEqual(len(events), 0, "Список не порожній для неіснуючого запиту")

    def tearDown(self):
        """Postconditions: Закриття браузера"""
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
