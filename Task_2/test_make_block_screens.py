from page_selectors import *

URL = "https://www.avito.ru/avito-care/eco-impact"


def test_counter_water(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(WATER_COUNTER).screenshot(path='Task_2/output/1.png')


def test_counter_CO2(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(CO2_COUNTER).screenshot(path='Task_2/output/2.png')


def test_counter_energy(browser):
    page = browser.new_page()
    page.goto(URL)
    page.locator(ENERGY_COUNTER).screenshot(path='Task_2/output/3.png')
