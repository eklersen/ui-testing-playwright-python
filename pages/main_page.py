from playwright.sync_api import Page

from core.base_page import BasePage
from config.settings import BASE_URL_ROZETKA


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=BASE_URL_ROZETKA)
        self.search_input = page.locator(
            "input[name='search'], input[type='search'], input[placeholder*='Пошук'], input[placeholder*='шукаю'], input[placeholder*='Шукаю']"
        ).first

    def open(self) -> "MainPage":
        super().open("/")
        return self

    def wait_ready(self) -> None:
        self.search_input.wait_for(state="visible", timeout=60000)

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")
        self.page.wait_for_load_state("load")
