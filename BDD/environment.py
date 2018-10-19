from selenium import webdriver

def before(context, feature):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(3)


def after(context, feature):
    context.driver.close()