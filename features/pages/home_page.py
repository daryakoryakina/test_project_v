import time

from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):

    COUNTRY_FIELD = (By.ID, "country-element")
    LANGUAGE_FIELD = (By.ID, "language")
    FRENCH_BUTTON = (By.XPATH, "(//*[@for = 'ch-7'])")
    APPLY_BUTTON = (By.XPATH, "(//a[@class = 'selecter-fieldset-submit'])")
    VACANCY_CART = (By.XPATH, "//*[@class = 'vacancies-blocks-container']//h4")
    COUNT_VACANCY_CART = (By.XPATH, "//div[@class = 'col-xs-12 pl0-md-down pr0-md-down']")
    CLEAR_FILTER = (By.ID, "clear-filters-button")

    def verify_page(self):
        self.on_this_page(self.COUNTRY_FIELD, self.LANGUAGE_FIELD)

    def select_country(self):
        self.click_on(self.COUNTRY_FIELD)
        # select = Select(self.COUNTRY_FIELD)

    def country_choice(self, country):
        country_button = (By.XPATH, "//*[@class = 'selecter-item' and contains (text(), '"+country+"')]")
        self.click_on(country_button)

    def ret_f(self, country):
        selected_button = (By.XPATH, "//*[@class = 'selecter-selected' and contains (text(), '"+country+"')]")
        return self.get_element(selected_button).text

    def language_field_open(self):
        self.click_on(self.LANGUAGE_FIELD)
        time.sleep(2)

    def language_choice(self, param):
        language_button = (By.XPATH, "//*[@for = '"+param+"']")
        self.click_on(language_button)

    def apply_button(self):
        self.click_on(self.APPLY_BUTTON)

    def language_in_field(self, language):
        language_field = (By.XPATH, "//*[@class = 'selecter-selected' and contains (text(), '"+language+"')]")
        return self.get_element(language_field).text

    def count_active_vacancy_cart_country(self, country):
        vacancy_carts_country = self.driver.find_elements(By.XPATH, "//*[@itemprop = 'addressRegion' and contains(text(),'"+country+"')]")
        return len(vacancy_carts_country)

    def count_active_vacancy_cart_language(self, language):
        vacancy_carts_language = self.driver.find_elements(By.XPATH, "//*[@class = 'languages m0' and contains (text(), '"+language+"')]")
        return len(vacancy_carts_language)

    def active_vacancy_block_h3(self):
        return self.get_element(self.COUNT_VACANCY_CART).text

    def clear_filter(self):
        self.click_on(self.CLEAR_FILTER)


