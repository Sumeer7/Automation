import pytest
from page import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def load_web_page():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
        driver.get(url)
        yield driver  # This is where the test runs
        driver.quit()
    except Exception as exe:
        logger.error(f"The error is {exe}", exc_info=True)


def test_table_data_ele_click(load_web_page):
    driver = load_web_page
    click_Table_data_ele(driver)

def test_text_area_field(load_web_page):
    driver = load_web_page
    click_Table_data_ele(driver)
    sending_data_to_text_area(driver)

def test_refrsh_button(load_web_page):
    driver = load_web_page
    click_Table_data_ele(driver)
    sending_data_to_text_area(driver)
    click_on_refresh_button(driver)

def test_assertion_functionality(load_web_page):
    driver = load_web_page
    click_Table_data_ele(driver)
    sending_data_to_text_area(driver)
    click_on_refresh_button(driver)
    assertion_check_for_UI_data(driver)

