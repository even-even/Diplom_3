import pytest
import allure
from data import User, Handle, Texts

@pytest.mark.usefixtures("setup")
class TestOrdersFeed:

    @allure.title('По клику на заказ всплывает окно с деталями о нем')
    def test_open_order_details(self, login_page, orders_feed_page):
        login_page.open_url(Handle.order_list_handle)
        orders_feed_page.open_order_details()
        composition = orders_feed_page.get_text_on_order_information()

        assert composition == Texts.ORDER_DETAILS

    @allure.title('Заказ из "Истории заказов" отображается в "Лента заказов"')
    def test_same_order_on_history_and_list(self, login_page, constructor_page, orders_feed_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url(Handle.order_list_handle)
        order_list = orders_feed_page.get_order_list()
        orders_feed_page.go_to_history()
        order_number = orders_feed_page.get_order_number()

        assert order_number in order_list

    @allure.title('При создании наказа счетчик "Выполнено за сегодня" увеличивается')
    def test_order_today_counters_update(self, login_page, constructor_page, orders_feed_page):
        orders_feed_page.open_url(Handle.order_list_handle)
        today_count_before_order = orders_feed_page.get_todays_count()
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url(Handle.order_list_handle)
        today_count_before_after_order = orders_feed_page.get_todays_count()

        assert today_count_before_order < today_count_before_after_order

    @allure.title('Номер оформленного заказа находится "В работе"')
    def test_order_number_in_work(self, login_page, constructor_page, orders_feed_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url(Handle.order_list_handle)
        order_number = orders_feed_page.get_order_number()
        in_progress = orders_feed_page.get_number_order_in_progress()

        assert order_number in in_progress
