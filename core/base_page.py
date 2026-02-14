import logging
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.page.set_default_timeout(30000)
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, path: str = "") -> None:
        url = f"{self.base_url}{path}"
        self.page.goto(url, wait_until="load")
        self.logger.info(f"Навігація до: {url}")

    def open(self, path: str = "") -> None:
        self.navigate(path)

    def wait_for_load(self) -> None:
        self.page.wait_for_load_state("load")

    def take_screenshot(self, name: str) -> None:
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)
