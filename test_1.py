import re

import pytest
from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_counter_water(browser):
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/1.png')#   t e s t _ n e w  
 