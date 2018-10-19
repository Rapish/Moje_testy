from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from Strona_selenium_testy.Page_objects.contact_fields import Contact_fields
import time
from Strona_selenium_testy.Objects.Xpaths import Path


class Test3():
    def contact_us_clear(self):
        driver = webdriver.Firefox()
        website = Web(driver)
        website.open_web()

        cfm = Contact_fields(driver)
        cfm.contact_fields_method("Moje imie", "mojmail@test.pl", "666", "Polska", "Moja firma",
                                  "To jest moja wiadomość" * 30)

        time.sleep(3)

        driver.find_element_by_xpath(Path.clear_button).click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='dt-btn dt-btn-m dt-btn-submit']").click()
        driver.get_screenshot_as_file(
            "C:\\Users\\Grzesiek\\PycharmProjects\\Testowe\\Strona_selenium_testy\\Screens\\Test3.png")

        print("Test3 - passed")

        c = Web(driver)
        c.close_web()


open = Test3()
open.contact_us_clear()
