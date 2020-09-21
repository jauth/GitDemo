# create browser invocation in conftest python file

import pytest
from selenium import webdriver
driver = None


# create command line option to choose browser for test
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="chrome, firefox, or edge"
    )
    parser.addoption(
        "--environment", action="store", default="qa", help="qa, uat, or prod"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")  # assign the command line option to a variable
    environment = request.config.getoption("environment")
    # if then loop to invoke chosen browser
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Firefox(executable_path="C:\\msedgedriver.exe")

    if environment == "qa":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif environment == "uat":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif environment == "prod":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # request sent to class object
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


