from selenium import webdriver
from Strona_selenium_testy.Objects.Xpaths import Path
from Strona_selenium_testy.Page_objects.open_website import Web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time





class Test6():
    def new_browser_tab(self):
        driver = webdriver.Firefox()
        w = Web(driver)
        w.open_web()

        main_window = driver.current_window_handle
        driver.find_element_by_xpath(Path.new_browser_tab_button).click()
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='main-nav']//span[contains(text(),'HOME')]")))
        try:
            rs = driver.execute_script("return document.readyState;")
            print(rs)
            if rs == "complete":
                print("Strona została zładowana")
        except Exception as e:
            print("Cos poszło nie tak")
            print(e)

        after_click_window = driver.window_handles

        for window in after_click_window:
            if window not in main_window:
                driver.switch_to.window(window)
                time.sleep(3)
                driver.execute_script("window.scrollBy(0, 2500);")
                element = driver.find_element_by_xpath("//span[contains(text(),'Feedback we received from Students')]")
                print(element.text)
                driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "background:yellow; color: Red;")



start = Test6()
start.new_browser_tab()




# element = driver.find_element_by_xpath("//span[contains(text(),'Feedback we received from Students')]")
# driver.execute_script("arguments[0].scrollIntoView(True);", element)
# print(element.text)

# wait = WebDriverWait(driver, 30)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='main-nav']//span[contains(text(),'HOME')]")))
# if wait is not None:
#     print("Okno zostało załadowane")
# else:
#     print("Okno nie zostało załadowane")
# "background:yellow; color: Red; border : 4px dotted solid yellow;"