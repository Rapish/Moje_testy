from selenium import webdriver
from Strona_selenium_testy.Page_objects.open_website import Web
from Strona_selenium_testy.Objects.Xpaths import Path
import time



class Test7():
    def alert_box(self):
        driver = webdriver.Firefox()
        w = Web(driver)
        w.open_web()

        driver.find_element_by_xpath(Path.alertbox).click()
        time.sleep(2)
        try:
            alert_info = "Please share this website with your friends and in your organization."
            alert = driver.switch_to_alert()

            if alert_info == alert.text:
                print("Tekst alertu jest prawidłowy")
            else:
                print("Tekst alertu jest nieprawidłowy")
                alert.dismiss()
            alert.accept()
            print("Alert zamkniety")
        except:
            print("Nie udało się zamknąc alertu")


        c = Web(driver)
        c.close_web()

start = Test7()
start.alert_box()