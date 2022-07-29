from .base_page import BasePage
from .main_page import MainPage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self): 
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Item in basket is presented, but should not be"
        
        
    def should_be_empty_basket_message(self):    
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message that busket is empty is not presented"