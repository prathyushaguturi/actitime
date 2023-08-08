import pytest
from selenium import webdriver
#from Source_code.login_page import Loginpage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def initialize_driver():
    #Creating chrome sessions
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=opts)

    wait_ = WebDriverWait(driver, 10)
    wait_.until(EC.url_to_be("https://demo.actitime.com/login.do"))

    # Launching the url
    url = "https://demo.actitime.com/login.do"
    driver.get(url)

    yield driver

    # closing the session
    driver.close()