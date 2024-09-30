import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_history_page import OrderHistoryPage
from pages.orders_feed_page import OrdersFeedPage
from pages.constructor_page import ConstructorPage

from data import Urls, Timeouts

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope='session')
def base_url():
    return Urls.BASE_URL

@pytest.fixture(params=[ 'chrome', 'firefox'])
def setup(request):
    driver = None

    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(Timeouts.MEDIUM)
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(setup, base_url):
    return LoginPage(setup, base_url)

@pytest.fixture()
def password_recovery_page(setup, base_url):
    return PasswordRecoveryPage(setup, base_url)

@pytest.fixture()
def personal_account_page(setup, base_url):
    return PersonalAccountPage(setup, base_url)

@pytest.fixture()
def order_history_page(setup, base_url):
    return OrderHistoryPage(setup, base_url)

@pytest.fixture()
def constructor_page(setup, base_url):
    return ConstructorPage(setup, base_url)

@pytest.fixture()
def orders_feed_page(setup, base_url):
    return OrdersFeedPage(setup, base_url)
