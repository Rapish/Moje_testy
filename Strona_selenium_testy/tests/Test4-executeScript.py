from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Strona_selenium_testy.Objects.Xpaths import Path


class Test4():
    def new_browser_window(self):
        driver = webdriver.Firefox()
        website = Web(driver)
        website.open_web()

        parent_window = driver.current_window_handle

        driver.find_element_by_xpath(Path.new_browser_window).click()


        afterclick_window = driver.window_handles
        for window in afterclick_window:
            if window not in parent_window:
                driver.switch_to.window(window)
                driver.maximize_window()
                wait = WebDriverWait(driver, 50, ignored_exceptions=NoSuchElementException).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'HOME')]")))
                wait.click()


                element1 = driver.find_element_by_xpath(Path.Selenium_Python_Basic_Tutorial)
                driver.execute_script("arguments[0].click();", element1)
                time.sleep(3)
                check1 = "//strong[contains(text(),'What is Python?')]"
                assert driver.find_element_by_xpath(check1)
                time.sleep(1)

                element2 = driver.find_element_by_xpath(Path.Selenium_Python_Intermediate)
                driver.execute_script("arguments[0].click();", element2)
                time.sleep(3)
                check2 = "//strong[contains(text(),'Test Data')]"
                assert driver.find_element_by_xpath(check2)
                time.sleep(1)

                element3 = driver.find_element_by_xpath(Path.Selenium_Python_Frameworks)
                driver.execute_script("arguments[0].click();", element3)
                time.sleep(3)
                check3 = "//strong[contains(text(),'What are Frameworks?')]"
                driver.find_element_by_xpath(check3)
                time.sleep(1)


                close = Web(driver)
                close.close_web()
start = Test4()
start.new_browser_window()