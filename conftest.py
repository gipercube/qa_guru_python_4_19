import pytest
from selene.support.shared import browser

from utils import attach
from utils.helper import BaseSession

LOGIN = 'aa@zz.cv'
PASSWORD = '123456'
API_URL = 'https://demowebshop.tricentis.com/'
WEB_URL = 'https://demowebshop.tricentis.com/'

browser.config.base_url = WEB_URL


@pytest.fixture(scope="session")
def webshop():
    with BaseSession(base_url="https://demowebshop.tricentis.com/") as session:
        response = session.post(
            url='login',
            params={'Email': LOGIN, 'Password': PASSWORD},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        session.cookies.set('NOPCOMMERCE.AUTH', authorization_cookie)
        browser.open("")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
        yield session

        attach.add_screenshot(browser)


@pytest.fixture(scope="session")
def reqres():
    with BaseSession(base_url="https://reqres.in") as session:
        yield session

        attach.add_screenshot(browser)
