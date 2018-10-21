from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from hamcrest import *
from Strona_selenium_testy.Page_objects.contact_fields import Contact_fields
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By


class Test1():
    def check_website(self):
        driver = webdriver.Firefox()
        website = Web(driver)
        website.open_web()

        get_title = driver.title
        my_title = "Selenium Framework | Practiceform"

        try:
            cf = Contact_fields(driver)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, cf.get_imie())))
            print("Strona została prawidłowo załadowana")
            try:
                assert_that(get_title, equal_to(my_title))
                screens_url = "C:\\Users\\Grzesiek\\PycharmProjects\\Testowe\\Strona_selenium_testy\\Screens\\Test1_screen.png"
                driver.get_screenshot_as_file(screens_url)
                print("Tytuł strony jest prawidłowy")
            except AssertionError:
                print(AssertionError)
        except:
            print("Nie udało się załadować strony!")






        driver.close()


start = Test1()
start.check_website()
