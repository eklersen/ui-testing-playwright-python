import allure
from pages.demo_login_page import DemoLoginPage


@allure.title("Demo: Open login page")
def test_demo_open_login_page(page):
    DemoLoginPage(page).open()
    assert "Swag Labs" in page.title()
