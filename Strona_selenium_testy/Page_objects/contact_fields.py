from selenium import webdriver
from Strona_selenium_testy.Objects.Xpaths import Path


class Contact_fields():

    def __init__(self, driver):
        self.driver = driver


    def get_imie(self):
        return self.driver.find_element_by_xpath(Path.imie)

    def get_email(self):
        return self.driver.find_element_by_xpath(Path.email)

    def get_telephone(self):
        return self.driver.find_element_by_xpath(Path.telephone)

    def get_country(self):
        return self.driver.find_element_by_xpath(Path.country)

    def get_company(self):
        return self.driver.find_element_by_xpath(Path.company)

    def get_message(self):
        return self.driver.find_element_by_xpath(Path.message)


    def keys_imie(self, imie):
        self.get_imie().send_keys(imie)

    def keys_email(self, email):
        self.get_email().send_keys(email)

    def keys_telephone(self, telephone):
        self.get_telephone().send_keys(telephone)

    def keys_country(self, country):
        self.get_country().send_keys(country)

    def keys_company(self, company):
        self.get_company().send_keys(company)

    def keys_message(self, message):
        self.get_message().send_keys(message)


    def contact_fields_method(self, imie, email, telephone, country, company, message):
        self.keys_imie(imie)
        self.keys_email(email)
        self.keys_telephone(telephone)
        self.keys_country(country)
        self.keys_company(company)
        self.keys_message(message)