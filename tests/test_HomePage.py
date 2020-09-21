import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("Name is: "+get_data["name"])
        home_page.get_name().send_keys(get_data["name"])
        log.info("Email is:"+get_data["email"])
        home_page.get_email().send_keys(get_data["email"])
        log.info("Password is: "+get_data["password"])
        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        log.info("Gender is: "+get_data["gender"])
        self.select_option_by_text(home_page.get_gender(), get_data["gender"])  # look in BaseClass.py for method
        home_page.get_employment_status().click()
        home_page.get_submit_button().click()

        alert_text = home_page.get_success_message().text
        assert "success" in alert_text
        self.driver.refresh()

    # use excel driven data from get_test_data method
    # @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))  # pull data for parameters from HomePageData.py
    # def get_data(self, request):
    #     return request.param

    # Use hard-coded dictionary
    @pytest.fixture(params=HomePageData.test_homepage_data)  # pull data for parameters from HomePageData.py
    def get_data(self, request):
        return request.param
