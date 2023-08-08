#from selenium import webdriver
import time

class Loginpage:
    """This class holds all the functionalities of login page"""
    username_loc = "id","username"
    password_loc = "name","pwd"
    login_loc = "xpath",'//div[text()="Login "]'
    def __init__(self,driver):
        self.driver = driver
    def enter_username(self,username):
        # entering username in the username textfield
        self.driver.find_element(*self.username_loc).send_keys(username)
        time.sleep(2)
    def enter_password(self,password):
        # Entering password in the password textfield
        self.driver.find_element(*self.password_loc).send_keys(password)
        time.sleep(2)
    def login_btn(self):
        # click on login button
        self.driver.find_element(*self.login_loc).click()
        time.sleep(2)


