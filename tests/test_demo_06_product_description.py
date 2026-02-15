import re
import allure
from pages.demo_login_page import DemoLoginPage

@allure.title("Demo: Product descriptions should not contain technical/code-like text")
def test_demo_product_description_consistency(page):
    DemoLoginPage(page).open().login("standard_user", "secret_sauce")

    descriptions = page.locator(".inventory_item_desc")
    count = descriptions.count()

    bad = []
    code_pattern = re.compile(r"\w+\.\w+|\w+\(.*\)|[\{\}\[\]]")

    for i in range(count):
        text = descriptions.nth(i).inner_text().strip()

        if code_pattern.search(text):
            bad.append(text)

    assert not bad, f"Descriptions contain code-like text: {bad}"
