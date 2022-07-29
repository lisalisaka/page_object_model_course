from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn.btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    PRICE_WINDOW = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_page .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_page h1")
    
class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")