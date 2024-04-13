import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


URL = "https://www.avito.ru/avito-care/eco-impact"


def test_counter_water(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/1.png')


def test_counter_CO2(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path='output/2.png')


def test_counter_energy(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)").screenshot(path='output/3.png')
