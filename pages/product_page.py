from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_busket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def check_adding_page(self): #функция, включающая в себя несколько проверок
        self.should_be_success_message()
        self.should_be_cost_window()
        self.compare_names()
        self.compare_prices()
        
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message window is not presented"
        
    def should_be_cost_window(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_WINDOW), "Price window is not presented"
         
    def compare_names(self):
        book_name_in_window = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_in_window, "Book name is not in message window" 
        
    def compare_prices(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_WINDOW).text
        assert price == price_in_alert, "Book price is not in message window" 
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
           
    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is exist, but should disappear"
 