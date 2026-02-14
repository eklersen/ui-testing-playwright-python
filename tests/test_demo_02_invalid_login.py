import allure
from pages.demo_login_page import DemoLoginPage


@allure.title("Demo: Invalid login shows error")
def test_demo_invalid_login(page):
    login = DemoLoginPage(page).open()
    login.login("wrong_user", "wrong_pass")
    assert login.error.is_visible()
