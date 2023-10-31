from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def explicit_wait(driver,timeout,xpath):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    return element






