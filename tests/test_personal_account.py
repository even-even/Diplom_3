import pytest
import allure
from data import User, Handle, Texts

@pytest.mark.usefixtures("setup")
class TestPersonalAccount:

    @allure.title('Переход в раздел "Личный кабинет"')
    def test_navigation_to_account(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        personal_account_page.go_to_personal_account()

        assert personal_account_page.get_text_from_profile_button() == Texts.PROFILE

    @allure.title('Переход в раздел "История заказов"')
    def test_navigation_to_order_history(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()

        assert personal_account_page.get_text_from_history_order() == Texts.ORDER_STATUS_TEXT_IN_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.EMAIL, User.PASSWORD)
        personal_account_page.go_to_personal_account()
        personal_account_page.logout()

        assert personal_account_page.get_text_after_logout() == Texts.ENTER