from behave import given, when, then
from selenium import webdriver

password = "rapisz1992"

@given('user is on Poczta Onet website')

def step_start_page(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://poczta.onet.pl/")

@when('user fills in the Sign In form and submits it')
def step_set_login_in(context):
    context.driver.find_element_by_id('f_login').send_keys('niwin@vp.pl')
    context.driver.find_element_by_id('f_password').send_keys(password)
    context.driver.find_element_by_xpath("//button[2]/span[contains(text(), 'Przejdź do serwisu')]").click()
    context.driver.find_element_by_css_selector('input.loginButton').click()

@then('user can see email list')
def step_valid_login(context):
  context.driver.save_screenshot("screenshot-login.png")
  assert context.driver.find_element_by_id('mailList-list-items')