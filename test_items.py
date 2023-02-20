import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_addtobasket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(button) > 0, "Button 'Add to Basket' not founded"
