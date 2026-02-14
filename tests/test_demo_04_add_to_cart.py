import allure
from pages.demo_login_page import DemoLoginPage
from pages.demo_inventory_page import DemoInventoryPage


@allure.title("Demo: Add first item to cart increases counter")
def test_demo_add_to_cart(page):
    DemoLoginPage(page).open().login("standard_user", "secret_sauce")
    inventory = DemoInventoryPage(page)
    inventory.add_first_item_to_cart()
    assert inventory.cart_count() == 1
