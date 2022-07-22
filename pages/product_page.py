from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage): 
    def add_to_busket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def check_adding_page(self):
        self.should_be_message_window()
        self.should_be_cost_window()
        self.compare_names()
        self.compare_prices()
        
    def should_be_message_window(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WINDOW), "Message window is not presented"
        
    def should_be_cost_window(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_WINDOW), "Price window is not presented"
         
    def compare_names(self):
        book_name_in_window = self.browser.find_element(*ProductPageLocators.MESSAGE_WINDOW).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_in_window, "Book name is not in message window" 
        
    def compare_prices(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_WINDOW).text
        assert price == price_in_alert, "Book price is not in message window" 