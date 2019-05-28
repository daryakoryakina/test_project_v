from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    COUNTRY_FIELD = (By.XPATH, "(//span[@class = 'selecter-selected' and contains (text(), 'Russian Federation')])")
    CANADA_BUTTON =
    LANGUAGE_FIELD = (By.XPATH, "(//span[@class = 'selecter-selected' and contains (text(), 'All languages' )])")
    FRENCH_BUTTON = (By.XPATH, "(//*[@for = 'ch-10'])")
    APPLY_BUTTON = (By.XPATH, "(//a[@class = 'selecter-fieldset-submit'])")
    VACANCY_CART =
    COUNT_VACANCY_CART =

    def verify_page(self):
        self.on_this_page(self.COUNTRY_FIELD, self.LANGUAGE_FIELD)

    def country(self):
        self.click_on(self.COUNTRY_FIELD)

    def country_choice(self):
        pass

    def language_field_open(self):
        self.click_on(self.LANGUAGE_FIELD)

    def language_choice(self):
        self.click_on(self.FRENCH_BUTTON)

    def apply_button(self):
        self.click_on()


