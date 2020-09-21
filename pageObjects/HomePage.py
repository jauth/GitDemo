from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[minlength*='2']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employment_radio = (By.ID, "inlineRadio2")
    submit_button = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()  # use * to de-serialize the tuple
        # driver.find_element_by_css_selector("a[href*='shop']")
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_employment_status(self):
        return self.driver.find_element(*HomePage.employment_radio)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.alert)
