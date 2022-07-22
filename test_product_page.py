from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer_number', [0,1,2,3,4,5,6,7,8,9])

def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_busket()          # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.check_adding_page()