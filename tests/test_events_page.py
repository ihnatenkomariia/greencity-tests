import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .utils import wait_for_element, wait_for_clickable  # Імпорт утиліт

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def test_tc1_verify_list(self):
        # Замість довгого WebDriverWait пишемо одну коротку функцію:
        locator = (By.CSS_SELECTOR, ".list-item")
        events = wait_for_element(self.driver, locator)
        
        self.assertTrue(events.is_displayed())

    def test_tc3_search(self):
        search_locator = (By.CSS_SELECTOR, "input[placeholder='Search']")
        # Використовуємо утиліту для очікування клікабельності
        search_field = wait_for_clickable(self.driver, search_locator)
        search_field.send_keys("Eco Workshop")
        # ... далі код тесту

    def tearDown(self):
        self.driver.quit()
