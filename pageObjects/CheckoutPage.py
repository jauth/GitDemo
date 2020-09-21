from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, "div[class=card-body] h4")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    cart_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    product_text = (By.CSS_SELECTOR, "h4[class='media-heading'] a")
    item_total = (By.XPATH, "//td[@class='col-sm-1 col-md-1 text-center'][2]/strong[1]")
    cart_total = (By.CSS_SELECTOR, "h3 strong")
    checkout_button = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)
        # driver.find_elements_by_xpath("//div[@class='card h-100']")

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def get_cart_button(self):
        return self.driver.find_element(*CheckoutPage.cart_button)

    def get_product_text(self):
        return self.driver.find_element(*CheckoutPage.product_text)

    def get_item_total(self):
        return self.driver.find_element(*CheckoutPage.item_total)

    def get_cart_total(self):
        return self.driver.find_element(*CheckoutPage.cart_total)

    def get_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
