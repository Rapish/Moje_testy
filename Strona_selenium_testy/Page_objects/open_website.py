from selenium import webdriver
from Strona_selenium_testy.Objects.Xpaths import Path

class Web():
    def __init__(self, driver):
        self.driver = driver

    def open_web(self):
        self.driver.maximize_window()
        self.driver.get(Path.main_website)

    def close_web(self):
        self.driver.close()
