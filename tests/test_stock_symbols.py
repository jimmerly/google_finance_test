import unittest
from utils.webdriver_setup import setup_driver
from pages.google_finance_page import GoogleFinancePage

class TestStockSymbols(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = setup_driver()
        cls.page = GoogleFinancePage(cls.driver)
        cls.page.open()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_verify_page_title(self):
        self.page.verify_title()

    def test_compare_stock_symbols(self):
        ui_symbols = self.page.get_interested_stock_symbols()
        test_data = ["NFLX", "MSFT", "TSLA"]

        ui_set = set(ui_symbols)
        test_data_set = set(test_data)

        symbols_in_ui_not_in_test = ui_set - test_data_set
        symbols_in_test_not_in_ui = test_data_set - ui_set

        print("Symbols in UI but not in test data:", symbols_in_ui_not_in_test)
        print("Symbols in test data but not in UI:", symbols_in_test_not_in_ui)

        # You can add assertions if needed
        # For example:
        # self.assertTrue(len(symbols_in_ui_not_in_test) > 0)

if __name__ == '__main__':
    unittest.main()
