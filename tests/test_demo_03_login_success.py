import allure
from pages.demo_login_page import DemoLoginPage
from pages.demo_inventory_page import DemoInventoryPage


@allure.title("Demo: Successful login opens inventory")
def test_demo_login_success(page):
    DemoLoginPage(page).open().login("standard_user", "secret_sauce")
    inventory = DemoInventoryPage(page)
    assert inventory.is_opened()
