from selenium.webdriver.common.by import By
import time


def test_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Basket button is not present on page!"
