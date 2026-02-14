from playwright.sync_api import Page

from core.base_page import BasePage
from config.settings import BASE_URL_DEMO


class DemoCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=BASE_URL_DEMO)
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def items_count(self) -> int:
        return self.cart_items.count()

    def is_checkout_visible(self) -> bool:
        return self.checkout_button.is_visible()
