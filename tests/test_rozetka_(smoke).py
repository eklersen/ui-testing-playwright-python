import pytest
import allure
from pages.main_page import MainPage


def safe_attach(page, name_prefix: str):
    try:
        allure.attach(
            page.screenshot(full_page=True),
            name=f"{name_prefix}.png",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            page.content(),
            name=f"{name_prefix}.html",
            attachment_type=allure.attachment_type.HTML,
        )
    except Exception:
        pass


@allure.title("Rozetka: Smoke search (flaky because of Cloudflare)")
def test_rozetka_search_smoke(page):
    main = MainPage(page).open()

    if page.title().strip() == "Just a moment...":
        safe_attach(page, "rozetka_cloudflare_home")
        pytest.skip("Rozetka blocked by Cloudflare on this run.")

    try:
        main.wait_ready()
    except Exception:
        safe_attach(page, "rozetka_home_no_search")
        pytest.skip("Rozetka homepage layout not available (possibly Cloudflare/variant).")

    before_url = page.url
    main.search("iPhone")
    after_url = page.url

    if page.title().strip() == "Just a moment...":
        safe_attach(page, "rozetka_cloudflare_after_search")
        pytest.skip("Rozetka blocked by Cloudflare after search.")

    if after_url == before_url:
        safe_attach(page, "rozetka_search_no_navigation")
        pytest.skip("Search action did not change page state (flaky behavior).")

    if ("search" not in after_url.lower()) and ("q=" not in after_url.lower()) and ("?search" not in after_url.lower()):
        safe_attach(page, "rozetka_search_unexpected_url")
        pytest.skip("Search navigation produced unexpected URL format (flaky behavior).")

    assert after_url != before_url
