from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from Strona_selenium_testy.Page_objects.contact_fields import Contact_fields
import time
from Strona_selenium_testy.Objects.Xpaths import Path


class Test2():
    def contact_us_submit(self):
        driver = webdriver.Firefox()
        website = Web(driver)
        website.open_web()

        cfm = Contact_fields(driver)
        cfm.contact_fields_method("Moje imie", "mojmail@test.pl", "666", "Polska", "Moja firma", "To jest moja wiadomość" * 10)
        time.sleep(3)
        driver.find_element_by_xpath(Path.submit_button).click()
        time.sleep(1)

        print("Test2 - passed")

        c = Web(driver)
        c.close_web()


open = Test2()
open.contact_us_submit()
