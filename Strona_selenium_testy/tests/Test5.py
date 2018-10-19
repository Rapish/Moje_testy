from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from Strona_selenium_testy.Objects.Xpaths import Path
import time
from hamcrest import *

class Test5():
    def new_message_window(self):
        driver = webdriver.Firefox()
        w = Web(driver)
        w.open_web()


        main_window = driver.current_window_handle
        driver.find_element_by_xpath(Path.new_message_window).click()
        time.sleep(2)

        afterclick_window = driver.window_handles
        for window in afterclick_window:
            if window not in main_window:
                driver.switch_to.window(window)
                try:
                    check = assert_that(main_window, is_not(window))
                    if check == None:
                        print("Okno zostało otwarte")
                except Exception as exc:
                    print("Błąd!" + str(exc))
                    print(exc)
                driver.close()
                driver.switch_to.window(main_window)

        c = Web(driver)
        c.close_web()


start = Test5()
start.new_message_window()

