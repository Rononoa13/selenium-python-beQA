from dotenv import load_dotenv
from selenium.webdriver.common.by import  By
import os
# from selenium import webdriver


class Toolbox:
    load_dotenv()
    secret_username = os.getenv('UNAME')
    secret_password = os.getenv('PWORD')
    invalid_password = os.getenv('INVALID_PWD')

    def url(self):
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url

    def login(self, uname, pword):
        self.driver.find_element(By.ID, 'signin_button').click()
        self.driver.find_element(By.ID, 'user_login').send_keys(uname)
        self.driver.find_element(By.ID, 'user_password').send_keys(pword)
        self.driver.find_element(By.ID, 'user_remember_me').click()
        self.driver.find_element(By.NAME, 'submit').click()