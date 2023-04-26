import pytest
import requests
from selene.support.shared import browser
from utils.helper import BaseSession

LOGIN = 'aa@zz.cv'
PASSWORD = '123456'
API_URL = 'https://demowebshop.tricentis.com/'
WEB_URL = 'https://demowebshop.tricentis.com/'

browser.config.base_url = WEB_URL


@pytest.fixture(scope="session")
def webshop():
    with BaseSession(base_url="https://demowebshop.tricentis.com/") as session:
        yield session


@pytest.fixture()
def login(webshop):
    response = webshop.post(
        url='/login',
        params={'Email': LOGIN, 'Password': PASSWORD},
        headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
        allow_redirects=False
    )
    authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("")
