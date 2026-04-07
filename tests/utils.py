from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    """Чекає, поки елемент стане видимим на сторінці."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator),
        message=f"Елемент {locator} не знайдено за {timeout} секунд"
    )

def wait_for_clickable(driver, locator, timeout=10):
    """Чекає, поки на елемент можна буде клікнути."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator),
        message=f"Елемент {locator} не став клікабельним"
    )
