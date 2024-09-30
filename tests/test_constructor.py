import pytest
import allure
from data import User, Handle, Texts

@pytest.mark.usefixtures("setup")
class TestConstructor:

    @allure.title('Переход в раздел "Конструктор"')
    def test_transfer_to_constructor_page(self, constructor_page, login_page, personal_account_page):
        constructor_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        personal_account_page.go_to_personal_account()
        constructor_page.open_constructor_page()

        assert constructor_page.get_text_on_constractor_page() == Texts.CONSTRUCTOR_HEADING

    @allure.title('Переход в раздел "Лента заказов"')
    def test_transfer_to_order_list(self, constructor_page):
        constructor_page.open_url(Handle.login_handle)
        constructor_page.open_order_list()

        assert constructor_page.get_text_on_order_page() == Texts.ORDER_PAGE_HEADING

    @allure.title('Всплывающее окно с деталями об ингредиенте при клике на него')
    def test_pop_up_with_details(self, constructor_page):
        constructor_page.open_url()
        constructor_page.open_ingredient_details()

        assert constructor_page.get_text_on_details_cart_heading() == Texts.DETAILS_CART_HEADING

    @allure.title('Всплывающее окно с деталями об ингредиенте закрывается по крестику')
    def test_close_pop_up_with_details(self, constructor_page):
        constructor_page.open_url()
        constructor_page.open_ingredient_details()
        constructor_page.close_ingredient_details()

        assert constructor_page.get_text_on_constractor_page() == Texts.CONSTRUCTOR_HEADING

    @allure.title('Счетчик ингредиента увеличивается если добавить его в заказ')
    def test_add_ingredient_to_order(self, constructor_page):
        constructor_page.open_url()
        constructor_page.add_ingredient_to_order()
        counter = constructor_page.get_ingredient_counter()

        assert counter == Texts.COUNT_INGREDIENT

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_submit_order_logged_in_user(self, login_page, constructor_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()

        assert constructor_page.get_text_on_submit_window() == Texts.SUBMIT_WINDOW_HEADING
