import allure
from pages.demo_login_page import DemoLoginPage
from pages.demo_inventory_page import DemoInventoryPage


@allure.title("Demo: All product names should start with 'Sauce Labs'")
def test_demo_product_name_consistency(page):
    DemoLoginPage(page).open().login("standard_user", "secret_sauce")

    inventory = DemoInventoryPage(page)
    product_titles = page.locator(".inventory_item_name")
    count = product_titles.count()

    wrong_titles = []

    for i in range(count):
        title = product_titles.nth(i).inner_text().strip()
        if not title.startswith("Sauce Labs"):
            wrong_titles.append(title)

    assert not wrong_titles, f"Products with invalid titles: {wrong_titles}"
