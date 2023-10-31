import json
from assertion_data import data
from SeleniumBase import *
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)

# Create a logger
logger = logging.getLogger(__name__)


def click_Table_data_ele(driver):
    try:
        """Explecite wait for element to appeare and then Click on table data element"""
        Table_data_ele = explicit_wait(driver, 10, "//summary[normalize-space()='Table Data']")
        Table_data_ele.click()
    except Exception as exe:
        logger.error(f"The error is {exe}", exc_info=True)

def sending_data_to_text_area(driver):
    try:
        """Finding text area and clearing space to dump the json data"""
        text_area = driver.find_element(By.XPATH, "//textarea[@id='jsondata']")
        text_area.clear()

        # Convert the list to a JSON-formatted string
        json_data = json.dumps(data)
        # Send the JSON-formatted string to the text area
        text_area.send_keys(json_data)
    except Exception as exe:
        logger.error(f"The error is {exe}", exc_info=True)

def click_on_refresh_button(driver):
    try:
        """Finding refresh button and clicking on it"""
        refresh_button = driver.find_element(By.XPATH, "//button[@id='refreshtable']")
        refresh_button.click()
    except Exception as exe:
        logger.error(f"The error is {exe}", exc_info=True)


def assertion_check_for_UI_data(driver):
    try:
        """
        Looping over Web text and assertion data text cell by cell and checking for assertion.
        """
        for r in range (len(data)):
            for c in range (len(data[0])):

                """Looping over web table cells"""
                cell_xpath = driver.find_element(
                    By.XPATH,
                    "(//table[@id='dynamictable']//tr[{}]//td[{}])".format(r+2,c+1)
                )

                """Looping over assertion_data file"""
                colums_names = driver.find_element(
                    By.XPATH,
                    "(//table[@id='dynamictable']//tr[1]//th[{}])".format(c+1)
                ).text

                web_text = cell_xpath.text
                assertion_text = str(data[r].get(colums_names))

                """Finally doing assertion check"""
                assert web_text == assertion_text

    except Exception as exe:
        logger.error(f"The error is {exe}",exc_info=True)
