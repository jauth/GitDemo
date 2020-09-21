from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)  # send driver to HomePage.py
        # Click on menu button for shop
        checkout_page = home_page.shop_items()
        log.info("Getting all products")

        # load list of products into a list
        products = checkout_page.get_card_titles()
        # iterate through the list to find the desiredProduct variable and then click on the add to cart button
        i = -1
        for product in products:
            i += 1
            product_text = product.text
            log.info(product_text)
            if "Blackberry" in product_text:
                checkout_page.get_card_footer()[i].click()

        # click on the cart button
        checkout_page.get_cart_button().click()

        # test case to make sure desiredProduct is in the cart
        assert checkout_page.get_product_text().text == "Blackberry"

        # load item total and cart total into variables and then run test case to make sure they match
        assert checkout_page.get_cart_total().text == checkout_page.get_item_total().text

        # click on the checkout button
        confirm_page = checkout_page.get_checkout_button()

        # locate suggestion text box, enter text, and then wait until the suggestions element has loaded
        log.info("Entering country name as unit")
        confirm_page.get_country_element().send_keys('unit')
        self.verify_link_presence("United States of America")
        # click on desired suggestion
        confirm_page.get_country().click()

        # use javascript to click checkbox
        # checkbox = driver.find_element_by_id("checkbox2")
        # driver.execute_script("arguments[0].click();", checkbox)

        # click the checkbox
        confirm_page.get_checkbox().click()

        # click purchase button
        confirm_page.get_purchase_button().click()

        text_match = confirm_page.get_success_alert().text
        log.info("Text received from the application is: "+ text_match)
        # look for success text
        assert "Success" in text_match
        log.info("Text matched")

