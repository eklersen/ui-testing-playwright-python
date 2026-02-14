from playwright.sync_api import Page
from core.base_page import BasePage
from config.settings import BASE_URL_DEMO


class DemoInventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=BASE_URL_DEMO)
        self.title = page.locator(".title")
        self.first_add_to_cart = page.locator("[data-test^='add-to-cart']").first
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def is_opened(self) -> bool:
        return self.title.is_visible()

    def add_first_item_to_cart(self) -> None:
        self.first_add_to_cart.click()

    def open_cart(self) -> None:
        self.cart_link.click()

    def cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text().strip())
