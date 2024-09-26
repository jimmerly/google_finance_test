from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class GoogleFinancePage(BasePage):
    URL = "https://www.google.com/finance"

    def open(self):
        self.driver.get(self.URL)

    def verify_title(self):
        assert "Google Finance" in self.driver.title

    def get_interested_stock_symbols(self):
        # Locator for the "You may be interested in" section
        stocks = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'ul.sbnBtf li div.COaKTb')))
        return [stock.text for stock in stocks]
