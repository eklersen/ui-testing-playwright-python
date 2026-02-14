import os
import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1400, "height": 900}, locale="uk-UA")
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.passed or report.skipped:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    os.makedirs("artifacts", exist_ok=True)
    name = report.nodeid.replace("::", "__").replace("/", "_").replace("\\", "_")

    try:
        png_path = os.path.join("artifacts", f"{name}.png")
        page.screenshot(path=png_path, full_page=True)
        allure.attach.file(png_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
    except Exception:
        pass

    try:
        html_path = os.path.join("artifacts", f"{name}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page.content())
        allure.attach.file(html_path, name="page_source", attachment_type=allure.attachment_type.HTML)
    except Exception:
        pass
