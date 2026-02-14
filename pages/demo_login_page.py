from playwright.sync_api import Page

from core.base_page import BasePage
from config.settings import BASE_URL_DEMO


class DemoLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=BASE_URL_DEMO)
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self) -> "DemoLoginPage":
        super().open("/")
        return self

    def login(self, user: str, pwd: str) -> None:
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
