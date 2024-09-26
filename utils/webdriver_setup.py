from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    # options.add_argument('--headless')  # Uncomment to run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    # Specify the path to chromedriver if not in PATH
    # service = Service('/path/to/chromedriver')  # Update the path if necessary

    # If chromedriver is in PATH, you can omit the 'service' parameter
    driver = webdriver.Chrome(options=options)
    return driver
