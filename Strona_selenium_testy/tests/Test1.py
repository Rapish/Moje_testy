from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from hamcrest import *


class Test1():
    def check_website(self):
        driver = webdriver.Firefox()
        website = Web(driver)
        website.open_web()

        get_title = driver.title
        my_title = "Selenium Framework | Practiceform"

        if get_title == my_title:
            print("Wszedłeś na stronę")
            assert_that(get_title, equal_to(my_title))
            screens_url = "C:\\Users\\Grzesiek\\PycharmProjects\\Testowe\\Strona_selenium_testy\\Screens\\Test1_screen.png"
            driver.get_screenshot_as_file(screens_url)
        else:
            ("Coś poszło nie tak")

        print("Test1 - passed!!!!")

        driver.close()


start = Test1()
start.check_website()
