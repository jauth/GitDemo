from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_element = (By.ID, "country")
    country = (By.LINK_TEXT, "United States of America")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_alert = (By.CLASS_NAME, "alert-success")

    def get_country_element(self):
        return self.driver.find_element(*ConfirmPage.country_element)

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_alert(self):
        return self.driver.find_element(*ConfirmPage.success_alert)
