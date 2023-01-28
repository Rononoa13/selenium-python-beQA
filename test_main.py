from selenium import webdriver

from dotenv import load_dotenv
import os

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options)

class Testwebpage:
    load_dotenv()
    
    def test_url(self):
        
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url


    def test_title(self):
        assert self.driver.title == 'Zero - Personal Banking - Loans - Credit Cards', "The expected title was not correct"


    # def test_cleanup(self):
    #     self.driver.quit()