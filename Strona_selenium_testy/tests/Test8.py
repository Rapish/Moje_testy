from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from metody_ze_szkolenia import SeleniumDriver


class Test8():
    def my_test(self):
        driver = webdriver.Firefox()
        w = Web(driver)
        w.open_web()

        # x = driver.find_element_by_xpath("//form[@action='https://feedburner.google.com/fb/a/mailverify']//input[@name='email']")

        gbt = SeleniumDriver(driver)
        gbt.getElement("//form[@action='https://feedburner.google.com/fb/a/mailverify']//input[@name='email']", "XPATH")

        c = Web(driver)
        #c.close_web()


start = Test8()
start.my_test()
