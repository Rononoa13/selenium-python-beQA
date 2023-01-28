from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dotenv import load_dotenv
import os

from utilibox import Toolbox

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# driver.implicitly_wait(5)



class Testlogin(Toolbox):
    load_dotenv()
    secret_username = os.getenv('UNAME')
    secret_password = os.getenv('PWORD')
    invalid_password = os.getenv('INVALID_PWD')

    def test_url(self):
        
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url


    def test_title(self):
        assert self.driver.title == 'Zero - Personal Banking - Loans - Credit Cards', "The expected title was not correct"

    # Positive test
    def test_login_with_valid_cred(self):
        self.login(self.secret_username, self.secret_password)

        self.driver.back()
        username = self.driver.find_elements(By.CSS_SELECTOR, 'a.dropdown-toggle')[1]
        assert self.secret_username == username.text

    def test_logout(self):
        self.driver.find_elements(By.CSS_SELECTOR, 'a.dropdown-toggle')[1].click()
        self.driver.find_element(By.ID, 'logout_link').click()

    # negative test
    def test_login_with_invalid_cred(self):
        self.login(self.secret_username, self.invalid_password)

    def test_login_error_message(self):
        login_error_message = self.driver.find_element(By.CSS_SELECTOR, 'div.alert.alert-error').text
        assert 'Login and/or password are wrong.' == login_error_message
    