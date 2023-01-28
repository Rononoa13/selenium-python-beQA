from selenium.webdriver.common.by import  By

# from selenium import webdriver


class Toolbox:
    def login(self, uname, pword):
        self.driver.find_element(By.ID, 'signin_button').click()
        self.driver.find_element(By.ID, 'user_login').send_keys(uname)
        self.driver.find_element(By.ID, 'user_password').send_keys(pword)
        self.driver.find_element(By.ID, 'user_remember_me').click()
        self.driver.find_element(By.NAME, 'submit').click()