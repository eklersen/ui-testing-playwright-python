import os
import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("GITHUB_ACTIONS", "").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()
    yield page

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

        try:
            allure.attach(
                page.url,
                name="Page URL",
                attachment_type=allure.attachment_type.URI_LIST,
            )
        except Exception:
            pass

    context.close()
