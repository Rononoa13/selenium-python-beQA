from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)


@pytest.fixture(autouse=True, scope='class')
def setup(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield

    driver.quit()