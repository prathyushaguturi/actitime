from datetime import datetime
import pytest
from Source_code.login_page import Loginpage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


data = [("admin","manager"),("admin","trainee"),("trainee","trainee")]
@pytest.mark.parametrize("username,password",data)
def test_login(initialize_driver,username,password):
    driver = initialize_driver
    try:
        lp = Loginpage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.login_btn()

        wait_ = WebDriverWait(driver, 10)

    ##validating login through url
    #wait_.until(EC.url_to_be("https://demo.actitime.com/user/submit_tt.do"))

    ##validate through title
        wait_.until(EC.title_is("actiTIME -  Enter Time-Track"))

    except Exception as error_msg:
        # driver.get_screenshot_as_file()
        td = datetime.now()
        path = r"C:\Users\Kishore\PycharmProjects\framework_actitime\Screenshots"
        name = f"{__name__}-{td.day}-{td.month}-{td.year}-{td.hour}-{td.minute}-{td.second}.png"
        driver.save_screenshot(path + name)
        raise error_msg
