import allure
import pytest

from data import User, Handle, Texts


@pytest.mark.usefixtures("setup")
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transfer_to_recovery_password_page(self, login_page, password_recovery_page):
        login_page.open_url(Handle.login_handle)
        password_recovery_page.transfer_recovery_password_page()

        assert password_recovery_page.get_text_head_recovery_password_first_screen() == Texts.RECOVER_PASSWORD

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_on_recovery_button(self, login_page, password_recovery_page):
        login_page.open_url(Handle.login_handle)
        password_recovery_page.transfer_recovery_password_page()
        password_recovery_page.recover_password(User.EMAIL)

        assert password_recovery_page.get_text_second_screen_placeholder() == Texts.SAVE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_test_visible_and_areas_activity(self, login_page, password_recovery_page):
        login_page.open_url(Handle.login_handle)
        password_recovery_page.transfer_recovery_password_page()
        password_recovery_page.recover_password(User.EMAIL)
        password_recovery_page.toggle_show_password()

        assert password_recovery_page.get_eye_button() == password_recovery_page.assign_parent_class()
